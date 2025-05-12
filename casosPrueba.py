casos_prueba = {"completo": ['''
                            program programaCool1;
                            var 
                            num5, num6: float;
                            x_, y_ : int;
                            
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
                        '''],
                "errores_sintacticos": ['''
                                            program programaCool1;
                                            var 
                                            num5, num6: float;
                                            x_, y_ : string;
                                            
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
                                        ''',
                                        '''
                                               program programaCool1;
                                               var 
                                               num5, num6: float;
                                               x_, y_ : int;
                                       
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
                                                       while(x_<y_)
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
                                           ''',
                                        '''
                                               program programaCool1;
                                               var 
                                               num5, num6: float;
                                               x_, y_ : int;
                                       
                                               void quacking(numPatos: int, tamano:float)[
                                               var patitos: int; 
                                               {patitos = numPatos;
                                               print("Tengo", patitos, "patitos de tamano", tamano);
                                               }];
                                       
                                               main {
                                                   num5 = 40.04;
                                                   x_ = -5
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
                                           ''',
                                        '''
                                               program programaCool1;
                                               var 
                                               num5, num6: float;
                                               x_, y_ : int;
                                       
                                               void quacking(numPatos: int, tamano:float)[
                                               var patitos: int; 
                                               {patitos = numPatos;
                                               print("Tengo", patitos, "patitos de tamano", tamano);
                                               }];
                                       
                                               main {
                                                   num5 = 40.04;
                                                   x_ = -5;
                                                   y_ = 6;
                                                   if x_<y_{
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
                                           '''
                                        ],
                "errores_lexicos": ['''
        program programaCool1;
        var 
        num5, num6: float;
        2x_, y_ : int;
        
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
    ''']

                }
