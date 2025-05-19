# esta clase incluye ambos variables y funciones
class Symbol:
    def __init__(self, name, type_=None, line=None):
        self.name = name  # nombre de símbolo
        self.type = type_  # el tipo - int, void, float
        self.scope = None
        self.line = line


# esta clase hereda de Symbol y es para variables
class VariablesSymbol(Symbol):
    def __init__(self, name, type_, line=None):
        super().__init__(name, type_, line)


# esta clase hereda de Symbol y es para funciones
class FunctionsSymbol(Symbol):
    def __init__(self, name, return_t=None, line=None):
        super().__init__(name, return_t, line)
        self.parameters = []  # parámetros de la función

    def set_param(self, param):
        self.parameters.append(param)

    def check_match_call(self, param_types):
        if len(param_types) != len(self.parameters):
            return False
        for i in range(len(param_types)):
            if param_types[i] != self.parameters[i].type:
                return False
        return True

class Scope:
    def __init__(self, name, container=None):
        self.name = name
        self.symbols = {}  # aquí vamos a guardar los symbols que vayan dentro del scope
        self.container = container
        self.is_param = False
        self.param_position = None
        self.initialized = False

    # método para definir dentro del scope un symbol
    def define(self, symbol):
        symbol.scope = self  # asignar el scope del symbol
        self.symbols[symbol.name] = symbol  # como el symbol esta en este scope, entonces se guarda en los symbols

    # método para buscar un symbol dentro del scope
    def find(self, name):
        if name in self.symbols:
            return self.symbols[name]  # buscar en el scope actual si se encuentra
        if self.container:
            return self.container.find(name)  # si no lo encuentro en el actual, buscar en el papá
        return None  # si no lo encuentro

class SymbolTable:
    def __init__(self):
        self.scope_now = Scope("global") # entramos primero al global
        self.global_scope = self.scope_now
        self.all_scopes = [self.scope_now]

    # entrar a "name" scope
    def enter_scope(self, name):
        new_scope = Scope(name, self.scope_now)
        self.scope_now = new_scope
        self.all_scopes.append(new_scope)

    # subir del scope actual al scope padre
    def exit_scope(self):
        if self.scope_now.container is not None:
            self.scope_now = self.scope_now.container

    def define(self, symbol):
        # agregar un símbolo al scope (o sea a donde estoy)
        self.scope_now.define(symbol)

    def find(self, name):
        return self.scope_now.find(name)
