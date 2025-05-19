class SemanticCube:
    def __init__(self):
        self.cube = {
            "int": {
                    "int": {"+": "int",
                            "-": "int",
                            "*": "int",
                            "/": "float",
                            ">": "bool",
                            "<": "bool",
                            "==": "bool",
                            "!=": "bool"},
                    "float": {"+": "float",
                              "-": "float",
                              "*": "float",
                              "/": "float",
                              ">": "bool",
                              "<": "bool",
                              "==": "bool",
                              "!=": "bool"},
            },
            "float": {
                    "int": {"+": "float",
                            "-": "float",
                            "*": "float",
                            "/": "float",
                            ">": "bool",
                            "<": "bool",
                            "==": "bool",
                            "!=": "bool"},
                    "float": {"+": "float",
                              "-": "float",
                              "*": "float",
                              "/": "float",
                              ">": "bool",
                              "<": "bool",
                              "==": "bool",
                              "!=": "bool"},
            }
        }
    def get_type_operator(self, left, right, operator):
        try:
            return self.cube[left][right][operator]
        except:
            return None