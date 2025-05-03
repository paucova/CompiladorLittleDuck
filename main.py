from antlr4 import *
from gen.littleDuckLexer import littleDuckLexer
from gen.littleDuckParser import littleDuckParser


if __name__ == '__main__':
    texto_input = '''
        program programaCool1;
        var num5, num6: float;
        var x_, y_ : int;
        
        void quacking(numPatos: int, tamano:float)[
        var patitos: int; 
        {patitos = numPatos;
        print("Tengo", patitos, "patitos de tamano", tamano);
        }];
        
        main {
            num5 = 40.04;
            x_ = -5;
            y_ = 6;
            if (x_<y_){
                while(x_<y_) do 
                    {
                        x_ = (x_ * y_);
                        y_ = y_ - 1;
                    };
                print("hace calor");
            }
            else
            {
                print("hace frio");
                y_ = 4;
            };
        
        quacking(x_, num5);
        }
        end
        
        "este es un string"
        3
        4.3
        int var float print while do if else void program main end
        (4 + 3) / (5 - 2)
        [3 + 2 - 1]
    '''
    # crear el lexer
    lexer = littleDuckLexer(InputStream(texto_input))
    stream = CommonTokenStream(lexer)
    stream.fill()

    # parser = littleDuckParser(stream)
    # tree = parser.program()
    # print(tree.toStringTree(recog=parser))

    #
    # for token in stream.tokens:
    #     print(f"Lexema: {token.text} \tCategoría: {token.type}")
        # aquí te trae los números, entonces queremos mas bien el nombre asociado a cada categoría


    for token in stream.tokens:
        print(f"Lexema: {token.text} \tCategoría: {lexer.symbolicNames[token.type]}")

