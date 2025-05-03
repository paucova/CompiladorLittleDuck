# Generated from /Users/paulinacovarrubias/Documents/compilador_LittleDuck/littleDuck.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,214,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,0,1,0,3,0,45,8,0,1,0,3,0,48,8,0,1,0,1,0,1,0,1,0,1,1,1,1,4,
        1,56,8,1,11,1,12,1,57,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,5,3,68,8,3,
        10,3,12,3,71,9,3,1,3,1,3,1,3,1,3,1,4,4,4,78,8,4,11,4,12,4,79,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,5,5,89,8,5,10,5,12,5,92,9,5,1,6,1,6,1,6,
        1,6,3,6,98,8,6,1,6,1,6,1,6,3,6,103,8,6,1,6,1,6,1,6,1,6,1,7,4,7,110,
        8,7,11,7,12,7,111,1,8,1,8,1,8,1,8,1,8,3,8,119,8,8,1,9,1,9,1,9,5,
        9,124,8,9,10,9,12,9,127,9,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,3,11,141,8,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,3,13,156,8,13,1,13,1,13,1,
        13,1,14,1,14,1,14,1,14,3,14,165,8,14,1,14,1,14,1,14,3,14,170,8,14,
        5,14,172,8,14,10,14,12,14,175,9,14,1,14,1,14,1,14,1,15,1,15,1,15,
        3,15,183,8,15,1,16,1,16,1,16,5,16,188,8,16,10,16,12,16,191,9,16,
        1,17,1,17,1,17,5,17,196,8,17,10,17,12,17,199,9,17,1,18,3,18,202,
        8,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,3,19,212,8,19,1,19,
        0,0,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,
        5,1,0,4,5,1,0,24,27,1,0,20,21,1,0,22,23,1,0,2,3,218,0,40,1,0,0,0,
        2,53,1,0,0,0,4,61,1,0,0,0,6,63,1,0,0,0,8,77,1,0,0,0,10,81,1,0,0,
        0,12,93,1,0,0,0,14,109,1,0,0,0,16,118,1,0,0,0,18,120,1,0,0,0,20,
        128,1,0,0,0,22,133,1,0,0,0,24,144,1,0,0,0,26,152,1,0,0,0,28,160,
        1,0,0,0,30,179,1,0,0,0,32,184,1,0,0,0,34,192,1,0,0,0,36,201,1,0,
        0,0,38,211,1,0,0,0,40,41,5,13,0,0,41,42,5,34,0,0,42,44,5,17,0,0,
        43,45,3,8,4,0,44,43,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,48,3,
        14,7,0,47,46,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,14,0,0,
        50,51,3,2,1,0,51,52,5,15,0,0,52,1,1,0,0,0,53,55,5,31,0,0,54,56,3,
        16,8,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,
        59,1,0,0,0,59,60,5,30,0,0,60,3,1,0,0,0,61,62,7,0,0,0,62,5,1,0,0,
        0,63,64,5,6,0,0,64,69,5,34,0,0,65,66,5,16,0,0,66,68,5,34,0,0,67,
        65,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,
        0,71,69,1,0,0,0,72,73,5,18,0,0,73,74,3,4,2,0,74,75,5,17,0,0,75,7,
        1,0,0,0,76,78,3,6,3,0,77,76,1,0,0,0,78,79,1,0,0,0,79,77,1,0,0,0,
        79,80,1,0,0,0,80,9,1,0,0,0,81,82,5,34,0,0,82,83,5,18,0,0,83,90,3,
        4,2,0,84,85,5,16,0,0,85,86,5,34,0,0,86,87,5,18,0,0,87,89,3,4,2,0,
        88,84,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,11,1,
        0,0,0,92,90,1,0,0,0,93,94,5,12,0,0,94,95,5,34,0,0,95,97,5,29,0,0,
        96,98,3,10,5,0,97,96,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,100,
        5,28,0,0,100,102,5,33,0,0,101,103,3,8,4,0,102,101,1,0,0,0,102,103,
        1,0,0,0,103,104,1,0,0,0,104,105,3,2,1,0,105,106,5,32,0,0,106,107,
        5,17,0,0,107,13,1,0,0,0,108,110,3,12,6,0,109,108,1,0,0,0,110,111,
        1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,15,1,0,0,0,113,119,3,
        20,10,0,114,119,3,22,11,0,115,119,3,24,12,0,116,119,3,26,13,0,117,
        119,3,28,14,0,118,113,1,0,0,0,118,114,1,0,0,0,118,115,1,0,0,0,118,
        116,1,0,0,0,118,117,1,0,0,0,119,17,1,0,0,0,120,125,3,30,15,0,121,
        122,5,16,0,0,122,124,3,30,15,0,123,121,1,0,0,0,124,127,1,0,0,0,125,
        123,1,0,0,0,125,126,1,0,0,0,126,19,1,0,0,0,127,125,1,0,0,0,128,129,
        5,34,0,0,129,130,5,19,0,0,130,131,3,30,15,0,131,132,5,17,0,0,132,
        21,1,0,0,0,133,134,5,10,0,0,134,135,5,29,0,0,135,136,3,30,15,0,136,
        137,5,28,0,0,137,140,3,2,1,0,138,139,5,11,0,0,139,141,3,2,1,0,140,
        138,1,0,0,0,140,141,1,0,0,0,141,142,1,0,0,0,142,143,5,17,0,0,143,
        23,1,0,0,0,144,145,5,8,0,0,145,146,5,29,0,0,146,147,3,30,15,0,147,
        148,5,28,0,0,148,149,5,9,0,0,149,150,3,2,1,0,150,151,5,17,0,0,151,
        25,1,0,0,0,152,153,5,34,0,0,153,155,5,29,0,0,154,156,3,18,9,0,155,
        154,1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,5,28,0,0,158,
        159,5,17,0,0,159,27,1,0,0,0,160,161,5,7,0,0,161,164,5,29,0,0,162,
        165,5,1,0,0,163,165,3,30,15,0,164,162,1,0,0,0,164,163,1,0,0,0,165,
        173,1,0,0,0,166,169,5,16,0,0,167,170,5,1,0,0,168,170,3,30,15,0,169,
        167,1,0,0,0,169,168,1,0,0,0,170,172,1,0,0,0,171,166,1,0,0,0,172,
        175,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,176,1,0,0,0,175,
        173,1,0,0,0,176,177,5,28,0,0,177,178,5,17,0,0,178,29,1,0,0,0,179,
        182,3,32,16,0,180,181,7,1,0,0,181,183,3,32,16,0,182,180,1,0,0,0,
        182,183,1,0,0,0,183,31,1,0,0,0,184,189,3,34,17,0,185,186,7,2,0,0,
        186,188,3,34,17,0,187,185,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,
        0,189,190,1,0,0,0,190,33,1,0,0,0,191,189,1,0,0,0,192,197,3,38,19,
        0,193,194,7,3,0,0,194,196,3,38,19,0,195,193,1,0,0,0,196,199,1,0,
        0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,35,1,0,0,0,199,197,1,0,0,
        0,200,202,7,2,0,0,201,200,1,0,0,0,201,202,1,0,0,0,202,203,1,0,0,
        0,203,204,7,4,0,0,204,37,1,0,0,0,205,206,5,29,0,0,206,207,3,30,15,
        0,207,208,5,28,0,0,208,212,1,0,0,0,209,212,3,36,18,0,210,212,5,34,
        0,0,211,205,1,0,0,0,211,209,1,0,0,0,211,210,1,0,0,0,212,39,1,0,0,
        0,21,44,47,57,69,79,90,97,102,111,118,125,140,155,164,169,173,182,
        189,197,201,211
    ]

class littleDuckParser ( Parser ):

    grammarFileName = "littleDuck.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'int'", "'float'", "'var'", "'print'", "'while'", 
                     "'do'", "'if'", "'else'", "'void'", "'program'", "'main'", 
                     "'end'", "','", "';'", "':'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'<'", "'>'", "'!='", "'=='", "')'", 
                     "'('", "'}'", "'{'", "']'", "'['" ]

    symbolicNames = [ "<INVALID>", "CTE_STRING", "CTE_INT", "CTE_FLOAT", 
                      "T_INT", "T_FLOAT", "VAR", "PRINT", "WHILE", "DO", 
                      "IF", "ELSE", "VOID", "PROGRAM", "MAIN", "END", "COMMA", 
                      "SEMICOLON", "COLON", "ASSIGN", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "LESS", "GREATER", "NOT_EQUAL", "EQUAL", 
                      "R_PAREN", "L_PAREN", "R_KEY", "L_KEY", "R_BRACKET", 
                      "L_BRACKET", "ID", "IGNORE" ]

    RULE_program = 0
    RULE_body = 1
    RULE_type = 2
    RULE_vars = 3
    RULE_vars_multiple = 4
    RULE_inner_funcs = 5
    RULE_funcs = 6
    RULE_funcs_multiple = 7
    RULE_statement = 8
    RULE_expression_multiple = 9
    RULE_assignment = 10
    RULE_condition = 11
    RULE_cycle = 12
    RULE_f_call = 13
    RULE_print = 14
    RULE_expression = 15
    RULE_exp = 16
    RULE_term = 17
    RULE_num_construct = 18
    RULE_factor = 19

    ruleNames =  [ "program", "body", "type", "vars", "vars_multiple", "inner_funcs", 
                   "funcs", "funcs_multiple", "statement", "expression_multiple", 
                   "assignment", "condition", "cycle", "f_call", "print", 
                   "expression", "exp", "term", "num_construct", "factor" ]

    EOF = Token.EOF
    CTE_STRING=1
    CTE_INT=2
    CTE_FLOAT=3
    T_INT=4
    T_FLOAT=5
    VAR=6
    PRINT=7
    WHILE=8
    DO=9
    IF=10
    ELSE=11
    VOID=12
    PROGRAM=13
    MAIN=14
    END=15
    COMMA=16
    SEMICOLON=17
    COLON=18
    ASSIGN=19
    PLUS=20
    MINUS=21
    MULTIPLY=22
    DIVIDE=23
    LESS=24
    GREATER=25
    NOT_EQUAL=26
    EQUAL=27
    R_PAREN=28
    L_PAREN=29
    R_KEY=30
    L_KEY=31
    R_BRACKET=32
    L_BRACKET=33
    ID=34
    IGNORE=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(littleDuckParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(littleDuckParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(littleDuckParser.SEMICOLON, 0)

        def MAIN(self):
            return self.getToken(littleDuckParser.MAIN, 0)

        def body(self):
            return self.getTypedRuleContext(littleDuckParser.BodyContext,0)


        def END(self):
            return self.getToken(littleDuckParser.END, 0)

        def vars_multiple(self):
            return self.getTypedRuleContext(littleDuckParser.Vars_multipleContext,0)


        def funcs_multiple(self):
            return self.getTypedRuleContext(littleDuckParser.Funcs_multipleContext,0)


        def getRuleIndex(self):
            return littleDuckParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = littleDuckParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(littleDuckParser.PROGRAM)
            self.state = 41
            self.match(littleDuckParser.ID)
            self.state = 42
            self.match(littleDuckParser.SEMICOLON)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 43
                self.vars_multiple()


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 46
                self.funcs_multiple()


            self.state = 49
            self.match(littleDuckParser.MAIN)
            self.state = 50
            self.body()
            self.state = 51
            self.match(littleDuckParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_KEY(self):
            return self.getToken(littleDuckParser.L_KEY, 0)

        def R_KEY(self):
            return self.getToken(littleDuckParser.R_KEY, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(littleDuckParser.StatementContext)
            else:
                return self.getTypedRuleContext(littleDuckParser.StatementContext,i)


        def getRuleIndex(self):
            return littleDuckParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = littleDuckParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(littleDuckParser.L_KEY)
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self.statement()
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17179870592) != 0)):
                    break

            self.state = 59
            self.match(littleDuckParser.R_KEY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_INT(self):
            return self.getToken(littleDuckParser.T_INT, 0)

        def T_FLOAT(self):
            return self.getToken(littleDuckParser.T_FLOAT, 0)

        def getRuleIndex(self):
            return littleDuckParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = littleDuckParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(littleDuckParser.VAR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(littleDuckParser.ID)
            else:
                return self.getToken(littleDuckParser.ID, i)

        def COLON(self):
            return self.getToken(littleDuckParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(littleDuckParser.TypeContext,0)


        def SEMICOLON(self):
            return self.getToken(littleDuckParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(littleDuckParser.COMMA)
            else:
                return self.getToken(littleDuckParser.COMMA, i)

        def getRuleIndex(self):
            return littleDuckParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars" ):
                return visitor.visitVars(self)
            else:
                return visitor.visitChildren(self)




    def vars_(self):

        localctx = littleDuckParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(littleDuckParser.VAR)
            self.state = 64
            self.match(littleDuckParser.ID)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 65
                self.match(littleDuckParser.COMMA)
                self.state = 66
                self.match(littleDuckParser.ID)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(littleDuckParser.COLON)
            self.state = 73
            self.type_()
            self.state = 74
            self.match(littleDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vars_multipleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(littleDuckParser.VarsContext)
            else:
                return self.getTypedRuleContext(littleDuckParser.VarsContext,i)


        def getRuleIndex(self):
            return littleDuckParser.RULE_vars_multiple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars_multiple" ):
                listener.enterVars_multiple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars_multiple" ):
                listener.exitVars_multiple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars_multiple" ):
                return visitor.visitVars_multiple(self)
            else:
                return visitor.visitChildren(self)




    def vars_multiple(self):

        localctx = littleDuckParser.Vars_multipleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vars_multiple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.vars_()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inner_funcsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(littleDuckParser.ID)
            else:
                return self.getToken(littleDuckParser.ID, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(littleDuckParser.COLON)
            else:
                return self.getToken(littleDuckParser.COLON, i)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(littleDuckParser.TypeContext)
            else:
                return self.getTypedRuleContext(littleDuckParser.TypeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(littleDuckParser.COMMA)
            else:
                return self.getToken(littleDuckParser.COMMA, i)

        def getRuleIndex(self):
            return littleDuckParser.RULE_inner_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInner_funcs" ):
                listener.enterInner_funcs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInner_funcs" ):
                listener.exitInner_funcs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInner_funcs" ):
                return visitor.visitInner_funcs(self)
            else:
                return visitor.visitChildren(self)




    def inner_funcs(self):

        localctx = littleDuckParser.Inner_funcsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inner_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(littleDuckParser.ID)
            self.state = 82
            self.match(littleDuckParser.COLON)
            self.state = 83
            self.type_()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 84
                self.match(littleDuckParser.COMMA)
                self.state = 85
                self.match(littleDuckParser.ID)
                self.state = 86
                self.match(littleDuckParser.COLON)
                self.state = 87
                self.type_()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(littleDuckParser.VOID, 0)

        def ID(self):
            return self.getToken(littleDuckParser.ID, 0)

        def L_PAREN(self):
            return self.getToken(littleDuckParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(littleDuckParser.R_PAREN, 0)

        def L_BRACKET(self):
            return self.getToken(littleDuckParser.L_BRACKET, 0)

        def body(self):
            return self.getTypedRuleContext(littleDuckParser.BodyContext,0)


        def R_BRACKET(self):
            return self.getToken(littleDuckParser.R_BRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(littleDuckParser.SEMICOLON, 0)

        def inner_funcs(self):
            return self.getTypedRuleContext(littleDuckParser.Inner_funcsContext,0)


        def vars_multiple(self):
            return self.getTypedRuleContext(littleDuckParser.Vars_multipleContext,0)


        def getRuleIndex(self):
            return littleDuckParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncs" ):
                return visitor.visitFuncs(self)
            else:
                return visitor.visitChildren(self)




    def funcs(self):

        localctx = littleDuckParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(littleDuckParser.VOID)
            self.state = 94
            self.match(littleDuckParser.ID)
            self.state = 95
            self.match(littleDuckParser.L_PAREN)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 96
                self.inner_funcs()


            self.state = 99
            self.match(littleDuckParser.R_PAREN)
            self.state = 100
            self.match(littleDuckParser.L_BRACKET)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 101
                self.vars_multiple()


            self.state = 104
            self.body()
            self.state = 105
            self.match(littleDuckParser.R_BRACKET)
            self.state = 106
            self.match(littleDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcs_multipleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(littleDuckParser.FuncsContext)
            else:
                return self.getTypedRuleContext(littleDuckParser.FuncsContext,i)


        def getRuleIndex(self):
            return littleDuckParser.RULE_funcs_multiple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs_multiple" ):
                listener.enterFuncs_multiple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs_multiple" ):
                listener.exitFuncs_multiple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncs_multiple" ):
                return visitor.visitFuncs_multiple(self)
            else:
                return visitor.visitChildren(self)




    def funcs_multiple(self):

        localctx = littleDuckParser.Funcs_multipleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcs_multiple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 108
                self.funcs()
                self.state = 111 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==12):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(littleDuckParser.AssignmentContext,0)


        def condition(self):
            return self.getTypedRuleContext(littleDuckParser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(littleDuckParser.CycleContext,0)


        def f_call(self):
            return self.getTypedRuleContext(littleDuckParser.F_callContext,0)


        def print_(self):
            return self.getTypedRuleContext(littleDuckParser.PrintContext,0)


        def getRuleIndex(self):
            return littleDuckParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = littleDuckParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 117
                self.print_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_multipleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(littleDuckParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(littleDuckParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(littleDuckParser.COMMA)
            else:
                return self.getToken(littleDuckParser.COMMA, i)

        def getRuleIndex(self):
            return littleDuckParser.RULE_expression_multiple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_multiple" ):
                listener.enterExpression_multiple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_multiple" ):
                listener.exitExpression_multiple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_multiple" ):
                return visitor.visitExpression_multiple(self)
            else:
                return visitor.visitChildren(self)




    def expression_multiple(self):

        localctx = littleDuckParser.Expression_multipleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression_multiple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.expression()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 121
                self.match(littleDuckParser.COMMA)
                self.state = 122
                self.expression()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(littleDuckParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(littleDuckParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(littleDuckParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(littleDuckParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return littleDuckParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = littleDuckParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(littleDuckParser.ID)
            self.state = 129
            self.match(littleDuckParser.ASSIGN)
            self.state = 130
            self.expression()
            self.state = 131
            self.match(littleDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(littleDuckParser.IF, 0)

        def L_PAREN(self):
            return self.getToken(littleDuckParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(littleDuckParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(littleDuckParser.R_PAREN, 0)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(littleDuckParser.BodyContext)
            else:
                return self.getTypedRuleContext(littleDuckParser.BodyContext,i)


        def SEMICOLON(self):
            return self.getToken(littleDuckParser.SEMICOLON, 0)

        def ELSE(self):
            return self.getToken(littleDuckParser.ELSE, 0)

        def getRuleIndex(self):
            return littleDuckParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = littleDuckParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(littleDuckParser.IF)
            self.state = 134
            self.match(littleDuckParser.L_PAREN)
            self.state = 135
            self.expression()
            self.state = 136
            self.match(littleDuckParser.R_PAREN)
            self.state = 137
            self.body()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 138
                self.match(littleDuckParser.ELSE)
                self.state = 139
                self.body()


            self.state = 142
            self.match(littleDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(littleDuckParser.WHILE, 0)

        def L_PAREN(self):
            return self.getToken(littleDuckParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(littleDuckParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(littleDuckParser.R_PAREN, 0)

        def DO(self):
            return self.getToken(littleDuckParser.DO, 0)

        def body(self):
            return self.getTypedRuleContext(littleDuckParser.BodyContext,0)


        def SEMICOLON(self):
            return self.getToken(littleDuckParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return littleDuckParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCycle" ):
                return visitor.visitCycle(self)
            else:
                return visitor.visitChildren(self)




    def cycle(self):

        localctx = littleDuckParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(littleDuckParser.WHILE)
            self.state = 145
            self.match(littleDuckParser.L_PAREN)
            self.state = 146
            self.expression()
            self.state = 147
            self.match(littleDuckParser.R_PAREN)
            self.state = 148
            self.match(littleDuckParser.DO)
            self.state = 149
            self.body()
            self.state = 150
            self.match(littleDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(littleDuckParser.ID, 0)

        def L_PAREN(self):
            return self.getToken(littleDuckParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(littleDuckParser.R_PAREN, 0)

        def SEMICOLON(self):
            return self.getToken(littleDuckParser.SEMICOLON, 0)

        def expression_multiple(self):
            return self.getTypedRuleContext(littleDuckParser.Expression_multipleContext,0)


        def getRuleIndex(self):
            return littleDuckParser.RULE_f_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call" ):
                listener.enterF_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call" ):
                listener.exitF_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF_call" ):
                return visitor.visitF_call(self)
            else:
                return visitor.visitChildren(self)




    def f_call(self):

        localctx = littleDuckParser.F_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_f_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(littleDuckParser.ID)
            self.state = 153
            self.match(littleDuckParser.L_PAREN)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17719885836) != 0):
                self.state = 154
                self.expression_multiple()


            self.state = 157
            self.match(littleDuckParser.R_PAREN)
            self.state = 158
            self.match(littleDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(littleDuckParser.PRINT, 0)

        def L_PAREN(self):
            return self.getToken(littleDuckParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(littleDuckParser.R_PAREN, 0)

        def SEMICOLON(self):
            return self.getToken(littleDuckParser.SEMICOLON, 0)

        def CTE_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(littleDuckParser.CTE_STRING)
            else:
                return self.getToken(littleDuckParser.CTE_STRING, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(littleDuckParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(littleDuckParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(littleDuckParser.COMMA)
            else:
                return self.getToken(littleDuckParser.COMMA, i)

        def getRuleIndex(self):
            return littleDuckParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = littleDuckParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(littleDuckParser.PRINT)
            self.state = 161
            self.match(littleDuckParser.L_PAREN)
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 162
                self.match(littleDuckParser.CTE_STRING)
                pass
            elif token in [2, 3, 20, 21, 29, 34]:
                self.state = 163
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 166
                self.match(littleDuckParser.COMMA)
                self.state = 169
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 167
                    self.match(littleDuckParser.CTE_STRING)
                    pass
                elif token in [2, 3, 20, 21, 29, 34]:
                    self.state = 168
                    self.expression()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self.match(littleDuckParser.R_PAREN)
            self.state = 177
            self.match(littleDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(littleDuckParser.ExpContext)
            else:
                return self.getTypedRuleContext(littleDuckParser.ExpContext,i)


        def LESS(self):
            return self.getToken(littleDuckParser.LESS, 0)

        def GREATER(self):
            return self.getToken(littleDuckParser.GREATER, 0)

        def EQUAL(self):
            return self.getToken(littleDuckParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(littleDuckParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return littleDuckParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = littleDuckParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.exp()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 251658240) != 0):
                self.state = 180
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 251658240) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 181
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(littleDuckParser.TermContext)
            else:
                return self.getTypedRuleContext(littleDuckParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(littleDuckParser.PLUS)
            else:
                return self.getToken(littleDuckParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(littleDuckParser.MINUS)
            else:
                return self.getToken(littleDuckParser.MINUS, i)

        def getRuleIndex(self):
            return littleDuckParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = littleDuckParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.term()
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 185
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 186
                self.term()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(littleDuckParser.FactorContext)
            else:
                return self.getTypedRuleContext(littleDuckParser.FactorContext,i)


        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(littleDuckParser.MULTIPLY)
            else:
                return self.getToken(littleDuckParser.MULTIPLY, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(littleDuckParser.DIVIDE)
            else:
                return self.getToken(littleDuckParser.DIVIDE, i)

        def getRuleIndex(self):
            return littleDuckParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = littleDuckParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.factor()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 193
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 194
                self.factor()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Num_constructContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CTE_INT(self):
            return self.getToken(littleDuckParser.CTE_INT, 0)

        def CTE_FLOAT(self):
            return self.getToken(littleDuckParser.CTE_FLOAT, 0)

        def PLUS(self):
            return self.getToken(littleDuckParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(littleDuckParser.MINUS, 0)

        def getRuleIndex(self):
            return littleDuckParser.RULE_num_construct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum_construct" ):
                listener.enterNum_construct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum_construct" ):
                listener.exitNum_construct(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum_construct" ):
                return visitor.visitNum_construct(self)
            else:
                return visitor.visitChildren(self)




    def num_construct(self):

        localctx = littleDuckParser.Num_constructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_num_construct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20 or _la==21:
                self.state = 200
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 203
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(littleDuckParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(littleDuckParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(littleDuckParser.R_PAREN, 0)

        def num_construct(self):
            return self.getTypedRuleContext(littleDuckParser.Num_constructContext,0)


        def ID(self):
            return self.getToken(littleDuckParser.ID, 0)

        def getRuleIndex(self):
            return littleDuckParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = littleDuckParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_factor)
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(littleDuckParser.L_PAREN)
                self.state = 206
                self.expression()
                self.state = 207
                self.match(littleDuckParser.R_PAREN)
                pass
            elif token in [2, 3, 20, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.num_construct()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.match(littleDuckParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





