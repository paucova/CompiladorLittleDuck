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
        4,1,35,208,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        0,3,0,43,8,0,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,1,0,1,0,1,0,1,1,
        1,1,4,1,57,8,1,11,1,12,1,58,1,1,1,1,1,2,1,2,1,3,1,3,4,3,67,8,3,11,
        3,12,3,68,1,4,1,4,1,4,5,4,74,8,4,10,4,12,4,77,9,4,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,90,8,5,10,5,12,5,93,9,5,1,6,1,
        6,1,6,1,6,3,6,99,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,
        1,7,3,7,113,8,7,1,8,1,8,1,8,5,8,118,8,8,10,8,12,8,121,9,8,1,9,1,
        9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,135,8,10,1,
        10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,3,
        12,150,8,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,3,13,159,8,13,1,13,
        1,13,1,13,3,13,164,8,13,5,13,166,8,13,10,13,12,13,169,9,13,1,13,
        1,13,1,13,1,14,1,14,1,14,3,14,177,8,14,1,15,1,15,1,15,5,15,182,8,
        15,10,15,12,15,185,9,15,1,16,1,16,1,16,5,16,190,8,16,10,16,12,16,
        193,9,16,1,17,3,17,196,8,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,
        18,3,18,206,8,18,1,18,0,0,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,0,5,1,0,4,5,1,0,24,27,1,0,20,21,1,0,22,23,1,0,2,3,
        211,0,38,1,0,0,0,2,54,1,0,0,0,4,62,1,0,0,0,6,64,1,0,0,0,8,70,1,0,
        0,0,10,82,1,0,0,0,12,94,1,0,0,0,14,112,1,0,0,0,16,114,1,0,0,0,18,
        122,1,0,0,0,20,127,1,0,0,0,22,138,1,0,0,0,24,146,1,0,0,0,26,154,
        1,0,0,0,28,173,1,0,0,0,30,178,1,0,0,0,32,186,1,0,0,0,34,195,1,0,
        0,0,36,205,1,0,0,0,38,39,5,13,0,0,39,40,5,34,0,0,40,42,5,17,0,0,
        41,43,3,6,3,0,42,41,1,0,0,0,42,43,1,0,0,0,43,47,1,0,0,0,44,46,3,
        12,6,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,
        50,1,0,0,0,49,47,1,0,0,0,50,51,5,14,0,0,51,52,3,2,1,0,52,53,5,15,
        0,0,53,1,1,0,0,0,54,56,5,31,0,0,55,57,3,14,7,0,56,55,1,0,0,0,57,
        58,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,60,1,0,0,0,60,61,5,30,
        0,0,61,3,1,0,0,0,62,63,7,0,0,0,63,5,1,0,0,0,64,66,5,6,0,0,65,67,
        3,8,4,0,66,65,1,0,0,0,67,68,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,
        69,7,1,0,0,0,70,75,5,34,0,0,71,72,5,16,0,0,72,74,5,34,0,0,73,71,
        1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,
        77,75,1,0,0,0,78,79,5,18,0,0,79,80,3,4,2,0,80,81,5,17,0,0,81,9,1,
        0,0,0,82,83,5,34,0,0,83,84,5,18,0,0,84,91,3,4,2,0,85,86,5,16,0,0,
        86,87,5,34,0,0,87,88,5,18,0,0,88,90,3,4,2,0,89,85,1,0,0,0,90,93,
        1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,11,1,0,0,0,93,91,1,0,0,0,
        94,95,5,12,0,0,95,96,5,34,0,0,96,98,5,29,0,0,97,99,3,10,5,0,98,97,
        1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,5,28,0,0,101,102,5,
        33,0,0,102,103,3,6,3,0,103,104,3,2,1,0,104,105,5,32,0,0,105,106,
        5,17,0,0,106,13,1,0,0,0,107,113,3,18,9,0,108,113,3,20,10,0,109,113,
        3,22,11,0,110,113,3,24,12,0,111,113,3,26,13,0,112,107,1,0,0,0,112,
        108,1,0,0,0,112,109,1,0,0,0,112,110,1,0,0,0,112,111,1,0,0,0,113,
        15,1,0,0,0,114,119,3,28,14,0,115,116,5,16,0,0,116,118,3,28,14,0,
        117,115,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,
        120,17,1,0,0,0,121,119,1,0,0,0,122,123,5,34,0,0,123,124,5,19,0,0,
        124,125,3,28,14,0,125,126,5,17,0,0,126,19,1,0,0,0,127,128,5,10,0,
        0,128,129,5,29,0,0,129,130,3,28,14,0,130,131,5,28,0,0,131,134,3,
        2,1,0,132,133,5,11,0,0,133,135,3,2,1,0,134,132,1,0,0,0,134,135,1,
        0,0,0,135,136,1,0,0,0,136,137,5,17,0,0,137,21,1,0,0,0,138,139,5,
        8,0,0,139,140,5,29,0,0,140,141,3,28,14,0,141,142,5,28,0,0,142,143,
        5,9,0,0,143,144,3,2,1,0,144,145,5,17,0,0,145,23,1,0,0,0,146,147,
        5,34,0,0,147,149,5,29,0,0,148,150,3,16,8,0,149,148,1,0,0,0,149,150,
        1,0,0,0,150,151,1,0,0,0,151,152,5,28,0,0,152,153,5,17,0,0,153,25,
        1,0,0,0,154,155,5,7,0,0,155,158,5,29,0,0,156,159,5,1,0,0,157,159,
        3,28,14,0,158,156,1,0,0,0,158,157,1,0,0,0,159,167,1,0,0,0,160,163,
        5,16,0,0,161,164,5,1,0,0,162,164,3,28,14,0,163,161,1,0,0,0,163,162,
        1,0,0,0,164,166,1,0,0,0,165,160,1,0,0,0,166,169,1,0,0,0,167,165,
        1,0,0,0,167,168,1,0,0,0,168,170,1,0,0,0,169,167,1,0,0,0,170,171,
        5,28,0,0,171,172,5,17,0,0,172,27,1,0,0,0,173,176,3,30,15,0,174,175,
        7,1,0,0,175,177,3,30,15,0,176,174,1,0,0,0,176,177,1,0,0,0,177,29,
        1,0,0,0,178,183,3,32,16,0,179,180,7,2,0,0,180,182,3,32,16,0,181,
        179,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,
        31,1,0,0,0,185,183,1,0,0,0,186,191,3,36,18,0,187,188,7,3,0,0,188,
        190,3,36,18,0,189,187,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,
        192,1,0,0,0,192,33,1,0,0,0,193,191,1,0,0,0,194,196,7,2,0,0,195,194,
        1,0,0,0,195,196,1,0,0,0,196,197,1,0,0,0,197,198,7,4,0,0,198,35,1,
        0,0,0,199,200,5,29,0,0,200,201,3,28,14,0,201,202,5,28,0,0,202,206,
        1,0,0,0,203,206,3,34,17,0,204,206,5,34,0,0,205,199,1,0,0,0,205,203,
        1,0,0,0,205,204,1,0,0,0,206,37,1,0,0,0,19,42,47,58,68,75,91,98,112,
        119,134,149,158,163,167,176,183,191,195,205
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
    RULE_var_group = 4
    RULE_inner_funcs = 5
    RULE_funcs = 6
    RULE_statement = 7
    RULE_expression_multiple = 8
    RULE_assignment = 9
    RULE_condition = 10
    RULE_cycle = 11
    RULE_f_call = 12
    RULE_print = 13
    RULE_expression = 14
    RULE_exp = 15
    RULE_term = 16
    RULE_num_construct = 17
    RULE_factor = 18

    ruleNames =  [ "program", "body", "type", "vars", "var_group", "inner_funcs", 
                   "funcs", "statement", "expression_multiple", "assignment", 
                   "condition", "cycle", "f_call", "print", "expression", 
                   "exp", "term", "num_construct", "factor" ]

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

        def vars_(self):
            return self.getTypedRuleContext(littleDuckParser.VarsContext,0)


        def funcs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(littleDuckParser.FuncsContext)
            else:
                return self.getTypedRuleContext(littleDuckParser.FuncsContext,i)


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
            self.state = 38
            self.match(littleDuckParser.PROGRAM)
            self.state = 39
            self.match(littleDuckParser.ID)
            self.state = 40
            self.match(littleDuckParser.SEMICOLON)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 41
                self.vars_()


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 44
                self.funcs()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(littleDuckParser.MAIN)
            self.state = 51
            self.body()
            self.state = 52
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
            self.state = 54
            self.match(littleDuckParser.L_KEY)
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.statement()
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17179870592) != 0)):
                    break

            self.state = 60
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
            self.state = 62
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

        def var_group(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(littleDuckParser.Var_groupContext)
            else:
                return self.getTypedRuleContext(littleDuckParser.Var_groupContext,i)


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
            self.state = 64
            self.match(littleDuckParser.VAR)
            self.state = 66 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 65
                self.var_group()
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==34):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_groupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return littleDuckParser.RULE_var_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_group" ):
                listener.enterVar_group(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_group" ):
                listener.exitVar_group(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_group" ):
                return visitor.visitVar_group(self)
            else:
                return visitor.visitChildren(self)




    def var_group(self):

        localctx = littleDuckParser.Var_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(littleDuckParser.ID)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 71
                self.match(littleDuckParser.COMMA)
                self.state = 72
                self.match(littleDuckParser.ID)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(littleDuckParser.COLON)
            self.state = 79
            self.type_()
            self.state = 80
            self.match(littleDuckParser.SEMICOLON)
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
            self.state = 82
            self.match(littleDuckParser.ID)
            self.state = 83
            self.match(littleDuckParser.COLON)
            self.state = 84
            self.type_()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 85
                self.match(littleDuckParser.COMMA)
                self.state = 86
                self.match(littleDuckParser.ID)
                self.state = 87
                self.match(littleDuckParser.COLON)
                self.state = 88
                self.type_()
                self.state = 93
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

        def vars_(self):
            return self.getTypedRuleContext(littleDuckParser.VarsContext,0)


        def body(self):
            return self.getTypedRuleContext(littleDuckParser.BodyContext,0)


        def R_BRACKET(self):
            return self.getToken(littleDuckParser.R_BRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(littleDuckParser.SEMICOLON, 0)

        def inner_funcs(self):
            return self.getTypedRuleContext(littleDuckParser.Inner_funcsContext,0)


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
            self.state = 94
            self.match(littleDuckParser.VOID)
            self.state = 95
            self.match(littleDuckParser.ID)
            self.state = 96
            self.match(littleDuckParser.L_PAREN)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 97
                self.inner_funcs()


            self.state = 100
            self.match(littleDuckParser.R_PAREN)
            self.state = 101
            self.match(littleDuckParser.L_BRACKET)
            self.state = 102
            self.vars_()
            self.state = 103
            self.body()
            self.state = 104
            self.match(littleDuckParser.R_BRACKET)
            self.state = 105
            self.match(littleDuckParser.SEMICOLON)
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
        self.enterRule(localctx, 14, self.RULE_statement)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 110
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 111
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
        self.enterRule(localctx, 16, self.RULE_expression_multiple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.expression()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 115
                self.match(littleDuckParser.COMMA)
                self.state = 116
                self.expression()
                self.state = 121
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
        self.enterRule(localctx, 18, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(littleDuckParser.ID)
            self.state = 123
            self.match(littleDuckParser.ASSIGN)
            self.state = 124
            self.expression()
            self.state = 125
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
        self.enterRule(localctx, 20, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(littleDuckParser.IF)
            self.state = 128
            self.match(littleDuckParser.L_PAREN)
            self.state = 129
            self.expression()
            self.state = 130
            self.match(littleDuckParser.R_PAREN)
            self.state = 131
            self.body()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 132
                self.match(littleDuckParser.ELSE)
                self.state = 133
                self.body()


            self.state = 136
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
        self.enterRule(localctx, 22, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(littleDuckParser.WHILE)
            self.state = 139
            self.match(littleDuckParser.L_PAREN)
            self.state = 140
            self.expression()
            self.state = 141
            self.match(littleDuckParser.R_PAREN)
            self.state = 142
            self.match(littleDuckParser.DO)
            self.state = 143
            self.body()
            self.state = 144
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
        self.enterRule(localctx, 24, self.RULE_f_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(littleDuckParser.ID)
            self.state = 147
            self.match(littleDuckParser.L_PAREN)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17719885836) != 0):
                self.state = 148
                self.expression_multiple()


            self.state = 151
            self.match(littleDuckParser.R_PAREN)
            self.state = 152
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
        self.enterRule(localctx, 26, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(littleDuckParser.PRINT)
            self.state = 155
            self.match(littleDuckParser.L_PAREN)
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 156
                self.match(littleDuckParser.CTE_STRING)
                pass
            elif token in [2, 3, 20, 21, 29, 34]:
                self.state = 157
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 160
                self.match(littleDuckParser.COMMA)
                self.state = 163
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 161
                    self.match(littleDuckParser.CTE_STRING)
                    pass
                elif token in [2, 3, 20, 21, 29, 34]:
                    self.state = 162
                    self.expression()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self.match(littleDuckParser.R_PAREN)
            self.state = 171
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
        self.enterRule(localctx, 28, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.exp()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 251658240) != 0):
                self.state = 174
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 251658240) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 175
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
        self.enterRule(localctx, 30, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.term()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 179
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 180
                self.term()
                self.state = 185
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
        self.enterRule(localctx, 32, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.factor()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 187
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 188
                self.factor()
                self.state = 193
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
        self.enterRule(localctx, 34, self.RULE_num_construct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20 or _la==21:
                self.state = 194
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 197
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
        self.enterRule(localctx, 36, self.RULE_factor)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.match(littleDuckParser.L_PAREN)
                self.state = 200
                self.expression()
                self.state = 201
                self.match(littleDuckParser.R_PAREN)
                pass
            elif token in [2, 3, 20, 21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.num_construct()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
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





