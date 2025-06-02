class Quadruples:
    def __init__(self, operator, arg1, arg2, result):
        self.operator = operator
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __str__(self):
        return f"{self.operator, self.arg1, self.arg2, self.result}"

class CodeGenerator:
    def __init__(self):
        self.quadruples = []
        self.temporales = 0
        self.etiquetas = 0
        self.func_directory = {}

    def create_quadruple(self, operator, arg1, arg2, result):
        self.quadruples.append(Quadruples(operator, arg1, arg2, result))

    #las temporales (los resultados intermedios)
    def temp_new(self):
        temp = f"t{self.temporales}"
        self.temporales += 1
        return temp

    #etiquetas para los saltos
    def label_new(self):
        et = f"t{self.etiquetas}"
        self.etiquetas += 1
        return et

    def print_quadruples(self):
        for i, quadruple in enumerate(self.quadruples):
            print(f"{i}:\t{quadruple}")
