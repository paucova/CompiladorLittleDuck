from antlr4 import *
from gen.littleDuckLexer import littleDuckLexer
from gen.littleDuckParser import littleDuckParser
from casosPrueba import casos_prueba

if __name__ == '__main__':
    texto_input = casos_prueba["errores_sintacticos"][0]
    # crear el lexer
    lexer = littleDuckLexer(InputStream(texto_input))
    stream = CommonTokenStream(lexer)
    stream.fill()

    parser = littleDuckParser(stream)
    tree = parser.program()
    #print(tree.toStringTree(recog=parser))

    #
    # for token in stream.tokens:
    #     print(f"Lexema: {token.text} \tCategoría: {token.type}")
        #aquí te trae los números, entonces queremos mas bien el nombre asociado a cada categoría

    #
    # for token in stream.tokens:
    #     print(f"Lexema: {token.text} \tCategoría: {lexer.symbolicNames[token.type]}")

