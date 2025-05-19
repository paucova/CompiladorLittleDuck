from antlr4 import *
from gen.littleDuckLexer import littleDuckLexer
from gen.littleDuckParser import littleDuckParser
from casos_prueba.casosPrueba import casos_prueba
from semantic_helpers.custom_visitor import CustomVisitor
from semantic_helpers.symbolTable import FunctionsSymbol

if __name__ == '__main__':
    archivo_quack = "casos_prueba/semantico/variables/validar_declaracion_previa.quack"
    input_stream = FileStream(archivo_quack)
    lexer = littleDuckLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = littleDuckParser(tokens)
    tree = parser.program()

    visitor = CustomVisitor()

    try:
        visitor.visit(tree)
        for scope in visitor.symbol_table.all_scopes:
            print(f"Scope: {scope.name}")
            print("-" * 50)
            for name, symbol in scope.symbols.items():
                print(f"Nombre: {name}")
                print(f"Tipo: {symbol.type}")
                print(f"Ámbito: {symbol.scope.name if symbol.scope else 'Global'}")
                if hasattr(symbol, 'line') and symbol.line:
                    print(f"Línea: {symbol.line}")
                if hasattr(symbol, 'param_position'):
                    print(f"Pos: {symbol.param_position}")

                if isinstance(symbol, FunctionsSymbol):
                    print("Parámetros:")
                    for i, param in enumerate(symbol.parameters, 1):
                        print(
                            f"  {i}. {param.name}: {param.type} (línea: {param.line if hasattr(param, 'line') else 'N/A'})")
                print("-" * 50)
    except Exception as ex:
        print(f"Oops, hubo un error: {ex}")


