from gen.littleDuckParser import littleDuckParser
from gen.littleDuckVisitor import littleDuckVisitor
from .symbolTable import SymbolTable, VariablesSymbol, FunctionsSymbol
from .semantic_cube import SemanticCube
from antlr4.tree.Tree import TerminalNodeImpl
from coding_logic.quadruples import CodeGenerator


# hereda del visitor generado por ANTLR
class CustomVisitor(littleDuckVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.semantic_cube = SemanticCube()
        self.code_gen = CodeGenerator()
        self.operand_stack = []
        self.operator_stack = []
        self.type_stack = []
        self.next_stack = []

    def visitVars(self, ctx: littleDuckParser.VarsContext):
        """
        Declaración de variables. Validación de tipo, repetición de declaraciones
        Recordemos que la estructura es:
        vars : VAR var_group+;
        var_group : ID (COMMA ID)* COLON type SEMICOLON;
        """

        # tenemos los grupos de variables - por ejemplo cuando declaramos varios bloques
        for group in ctx.var_group():
            line = group.type_().start.line
            # el tipo de la variable va a ser el tipo asignado al grupo
            var_type = group.type_().getText()
            # VALIDACIÓN DE TIPO
            if var_type not in ['int', 'float']:
                raise Exception(f"Linea {line}: El tipo {var_type} no es válido para declarar una variable")

            # ahora si, dentro del grupo podemos tener más de 1 variable:
            for var_name in group.ID():
                name = var_name.getText()
                line = var_name.getSymbol().line
                # VALIDACIÓN DE NO SER DECLARADA DOS VECES
                if self.symbol_table.find(name) and self.symbol_table.find(name).scope == self.symbol_table.scope_now:
                    raise Exception(f"Linea {line}: Ya se declaró la variable {var_name} en este scope")
                # declaramos el símbolo para la tabla :) y llenamos todos los parámetros
                var_symbol = VariablesSymbol(
                    name=var_name.getText(),
                    type_=var_type,
                    line=var_name.getSymbol().line
                )
                self.symbol_table.define(var_symbol)

    def visitAssignment(self, ctx: littleDuckParser.AssignmentContext):
        """
        Asignación de variables. Validación de tipo, declaración previa, símbolo
        Recordemos que la estructura es:
        assignment : ID ASSIGN expression SEMICOLON;
        """
        var_name = ctx.ID().getText()
        var_symbol = self.symbol_table.find(var_name)
        line = ctx.ID().getSymbol().line
        var_type = self.visit(ctx.expression())

        # VALIDACIÓN DE DECLARACIÓN PREVIA
        if not self.symbol_table.find(var_name):
            raise Exception(f"Linea {line}: Variable {var_name} no ha sido declarada.")

        # VALIDACIÓN DE SÍMBOLO
        if not isinstance(var_symbol, VariablesSymbol):
            raise Exception(f"Linea {line}: Variable {var_name} no es válida.")

        # VALIDACIÓN DE PARÁMETROS
        if getattr(var_symbol, 'is_param', False):
            raise Exception(f"Línea {line}: No se puede asignar al parámetro '{var_name}'")

        # VALIDACIÓN DE TIPO
        if var_symbol.type != var_type:
            raise Exception(f"Linea {line}: La asignación de la variable no corresponde con el tipo en declaración.")

    def visitInner_funcs(self, ctx: littleDuckParser.Inner_funcsContext):
        """
        Recordemos que la estructura es:
        inner_funcs : ID COLON type (COMMA ID COLON type)*;
        """
        params = []
        for i in range(len(ctx.ID())):
            param_name = ctx.ID(i).getText()
            param_type = ctx.type_(i).getText()
            param_line = ctx.ID(i).getSymbol().line
            # creamos un símbolo en nuestra tabla de símbolos
            param = VariablesSymbol(param_name, param_type, param_line)
            # para indicar que es parámetro
            param.is_param = True
            param.param_position = i + 1
            params.append(param)
            # retornamos el arreglo con los parámetros ya como símbolos
        return params

    def visitFuncs(self, ctx: littleDuckParser.FuncsContext):
        """
        Recordemos que la estructura es:
        funcs : VOID ID L_PAREN inner_funcs? R_PAREN L_BRACKET vars body R_BRACKET SEMICOLON;
        """
        func_name = ctx.ID().getText()
        # VALIDAR DOBLE DECLARACIÓN
        if self.symbol_table.find(func_name) and isinstance(self.symbol_table.find(func_name), FunctionsSymbol):
            raise Exception(f"{func_name} ya fue declarada")

        # crear el símbolo para nuestra tabla de símbolos
        func_symbol = FunctionsSymbol(func_name,
                                      'void',
                                      ctx.ID().getSymbol().line)
        # nos metemos en el scope interior de la función
        self.symbol_table.enter_scope(f"func_{func_name}")
        # si vemos que existe algo declarado en el inner funcs (o sea parámetros)
        if ctx.inner_funcs():
            params = self.visit(ctx.inner_funcs())
            if params:
                # vamos a - dentro de nuestra tabla de símbolos, definir los parámetros dentro del scope de la función
                for param in params:
                    self.symbol_table.define(param)
                    # también dentro del símbolo de función
                    func_symbol.set_param(param)
        # checar si hay variables declaradas de forma local
        if ctx.vars_():
            self.visit(ctx.vars_())
        self.visit(ctx.body())
        # nos salimos del scope
        self.symbol_table.exit_scope()
        self.symbol_table.define(func_symbol)

    def visitF_call(self, ctx: littleDuckParser.F_callContext):
        """
        Recordemos que la estructura es:
        f_call : ID L_PAREN expression_multiple? R_PAREN SEMICOLON;
        """
        function_name = ctx.ID().getText()
        function_symbol = self.symbol_table.find(function_name)

        # VALIDAR que exista función antes de llamar
        if not function_symbol:
            raise Exception(f"La función {function_name} no existe")
        # VALIDAR que un símbolo esté declarado como función
        if not isinstance(function_symbol, FunctionsSymbol):
            raise Exception(f"Verificar que {function_name} esté declarada como función")

        # agregar los parámetros de la función
        params_func = []
        if ctx.expression_multiple():
            for expre in ctx.expression_multiple().expression():
                params_func.append(self.visit(expre))

        # VALIDAR que los parámetros del call coincidan con los parámetros de la declaración
        if not function_symbol.check_match_call(params_func):
            expected_params = [par.type for par in function_symbol.parameters]
            raise Exception(f"en la función {function_name}, se espera {expected_params}, has declarado {params_func}")

        return function_symbol.type

    # podemos también explorar:

    def visitExpression(self, ctx: littleDuckParser.ExpressionContext):
        """
        Recordemos que la estructura es:
        expression : exp ((LESS | GREATER | EQUAL | NOT_EQUAL) exp)?;
        """
        # podemos tener solamente un exp
        first_type = self.visit(ctx.exp(0))
        first_operand = self.operand_stack[-1] if self.operand_stack else None
        # o la comparación que se evalúa en un booleano
        if ctx.getChildCount() > 1:
            operator = ctx.getChild(1).getText()
            second_type = self.visit(ctx.exp(1))
            second_operand = self.operand_stack[-1] if self.operand_stack else None
            result_type = self.semantic_cube.get_type_operator(first_type, second_type, operator)

            # VALIDAR si no coincide con el cubo semántico (realmente aquí es dificil no tener coincidencia porque siempre se consideran)
            if not result_type:
                raise Exception(f"No se puede llevar a cabo la operación {first_type} {operator} {second_type}")
            temp = self.code_gen.temp_new()
            self.code_gen.create_quadruple(operator, first_operand, second_operand, temp)
            self.operand_stack.pop()
            self.operand_stack[-1] = temp

            return result_type
        return first_type

    def visitExp(self, ctx: littleDuckParser.ExpContext):
        """
        Recordemos que la estructura es:
        exp : term ((PLUS | MINUS) term)*;
        """
        first_type = self.visit(ctx.term(0))
        first_operand = self.operand_stack[-1] if self.operand_stack else None

        # podemos sumar o restar x cantidad de veces
        for i in range(1, len(ctx.term())):
            operator = ctx.getChild(2 * i - 1).getText()
            next_type = self.visit(ctx.term(i))
            next_operand = self.operand_stack[-1] if self.operand_stack else None
            result_type = self.semantic_cube.get_type_operator(first_type, next_type, operator)

            # VALIDAR si no coincide con el cubo semántico (realmente aquí es dificil no tener coincidencia porque siempre se consideran)
            if not result_type:
                raise Exception(f"Tipos incompatibles en operación: {first_type} {operator} {next_type}")

            temp = self.code_gen.temp_new()
            self.code_gen.create_quadruple(operator, first_operand, next_operand, temp)
            self.operand_stack.pop()
            self.operand_stack[-1] = temp
            first_operand = temp
            first_type = result_type

        return first_type

    def visitTerm(self, ctx: littleDuckParser.TermContext):
        """
        Recordemos que la estructura es:
        term : factor ((MULTIPLY | DIVIDE) factor)*;
        """
        # podemos tener solamente un factor
        first_type = self.visit(ctx.factor(0))
        first_operand = self.operand_stack[-1] if self.operand_stack else None

        # podemos multiplicar o dividir x cantidad de veces
        for i in range(1, len(ctx.factor())):
            operator = ctx.getChild(2 * i - 1).getText()
            next_type = self.visit(ctx.factor(i))
            next_operand = self.operand_stack[-1] if self.operand_stack else None

            result_type = self.semantic_cube.get_type_operator(first_type, next_type, operator)
            # VALIDAR si no coincide con el cubo semántico (realmente aquí es dificil no tener coincidencia porque siempre se consideran)
            if not result_type:
                raise Exception(f"Tipos incompatibles en operación: {first_type} {operator} {next_type}")

            temp = self.code_gen.temp_new()
            self.code_gen.create_quadruple(operator, first_operand, next_operand, temp)
            self.operand_stack.pop()
            self.operand_stack[-1] = temp
            first_operand = temp
            first_type = result_type
        return first_type

    def visitFactor(self, ctx: littleDuckParser.FactorContext):
        """
        Recordemos que la estructura es:
        factor : L_PAREN expression R_PAREN | num_construct | ID;
        """
        if ctx.L_PAREN():
            return self.visit(ctx.expression())
        elif ctx.num_construct():
            num_node = ctx.num_construct()
            num_text = num_node.getText()
            self.operand_stack.append(num_text)
            if '.' in num_text or 'e' in num_text.lower():
                return 'float'
            return 'int'
        elif ctx.ID():
            var_name = ctx.ID().getText()
            var_symbol = self.symbol_table.find(var_name)
            if not var_symbol:
                # VALIDAR que el factor haya sido declarado
                raise Exception(f"Variable no declarada: {var_name}")
            if not isinstance(var_symbol, VariablesSymbol):
                # VALIDAR que sea una variable
                raise Exception(f"{var_name} no es una variable")
            self.operand_stack.append(var_name)
            return var_symbol.type
        raise Exception("Factor inválido: estructura no reconocida")

    # ACCIONES

    def visitPrint(self, ctx: littleDuckParser.PrintContext):
        """
        Estructura:
        PRINT L_PAREN (CTE_STRING|expression) (COMMA (CTE_STRING|expression))* R_PAREN SEMICOLON;
        """
        printables = []
        in_args = False

        for child in ctx.getChildren():
            text = child.getText()
            if text == '(':
                in_args = True
                continue
            elif text == ')':
                in_args = False
                continue
            if in_args and text != ',':
                printables.append(child)

        for item in printables:
            if isinstance(item, TerminalNodeImpl) and item.getSymbol().type == littleDuckParser.CTE_STRING:
                continue
            expr_type = self.visit(item)
            if expr_type is None:
                raise Exception(f"Línea {item.getSymbol().line}: Expresión no válida en print")
            if expr_type not in ['int', 'float', 'bool']:
                raise Exception(
                    f"Línea {item.getSymbol().line}: No se puede imprimir valores de tipo {expr_type}, "
                    f"Solo se permiten int, float, bool o strings"
                )

    def visitCondition(self, ctx: littleDuckParser.ConditionContext):
        """
        Estructura:
        condition : IF L_PAREN expression R_PAREN body (ELSE body)? SEMICOLON;
        """
        cond_type = self.visit(ctx.expression())
        if cond_type != 'bool':
            raise Exception(
                f"Línea {ctx.expression().start.line}: La condición del if debe ser booleana. "
                f"Tipo recibido: '{cond_type}'"
            )
        self.visit(ctx.body(0))
        if ctx.ELSE():
            self.visit(ctx.body(1))

    def visitCycle(self, ctx: littleDuckParser.CycleContext):
        cond_type = self.visit(ctx.expression())
        if cond_type != 'bool':
            # VALIDAR que la condición sea correcta (booleana) en el while
            raise Exception(f"Línea {ctx.expression().start.line}: La condición del while debe ser booleana")
        self.visit(ctx.body())

    def visitProgram(self, ctx: littleDuckParser.ProgramContext):
        #declaraciones primero
        if ctx.vars_():
            self.visit(ctx.vars_())
        # luego vienen las funciones
        for func in ctx.funcs():
            self.visit(func)
        # luego el main
        self.visit(ctx.MAIN())
        # el body
        self.visit(ctx.body())
        # cuádruplo que indica fin del programa
        self.code_gen.create_quadruple('ENDPROG', None, None, None)

