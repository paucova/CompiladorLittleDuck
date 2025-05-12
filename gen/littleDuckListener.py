# Generated from /Users/paulinacovarrubias/Documents/compilador_LittleDuck/littleDuck.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .littleDuckParser import littleDuckParser
else:
    from littleDuckParser import littleDuckParser

# This class defines a complete listener for a parse tree produced by littleDuckParser.
class littleDuckListener(ParseTreeListener):

    # Enter a parse tree produced by littleDuckParser#program.
    def enterProgram(self, ctx:littleDuckParser.ProgramContext):
        pass

    # Exit a parse tree produced by littleDuckParser#program.
    def exitProgram(self, ctx:littleDuckParser.ProgramContext):
        pass


    # Enter a parse tree produced by littleDuckParser#body.
    def enterBody(self, ctx:littleDuckParser.BodyContext):
        pass

    # Exit a parse tree produced by littleDuckParser#body.
    def exitBody(self, ctx:littleDuckParser.BodyContext):
        pass


    # Enter a parse tree produced by littleDuckParser#type.
    def enterType(self, ctx:littleDuckParser.TypeContext):
        pass

    # Exit a parse tree produced by littleDuckParser#type.
    def exitType(self, ctx:littleDuckParser.TypeContext):
        pass


    # Enter a parse tree produced by littleDuckParser#vars.
    def enterVars(self, ctx:littleDuckParser.VarsContext):
        pass

    # Exit a parse tree produced by littleDuckParser#vars.
    def exitVars(self, ctx:littleDuckParser.VarsContext):
        pass


    # Enter a parse tree produced by littleDuckParser#inner_funcs.
    def enterInner_funcs(self, ctx:littleDuckParser.Inner_funcsContext):
        pass

    # Exit a parse tree produced by littleDuckParser#inner_funcs.
    def exitInner_funcs(self, ctx:littleDuckParser.Inner_funcsContext):
        pass


    # Enter a parse tree produced by littleDuckParser#funcs.
    def enterFuncs(self, ctx:littleDuckParser.FuncsContext):
        pass

    # Exit a parse tree produced by littleDuckParser#funcs.
    def exitFuncs(self, ctx:littleDuckParser.FuncsContext):
        pass


    # Enter a parse tree produced by littleDuckParser#statement.
    def enterStatement(self, ctx:littleDuckParser.StatementContext):
        pass

    # Exit a parse tree produced by littleDuckParser#statement.
    def exitStatement(self, ctx:littleDuckParser.StatementContext):
        pass


    # Enter a parse tree produced by littleDuckParser#expression_multiple.
    def enterExpression_multiple(self, ctx:littleDuckParser.Expression_multipleContext):
        pass

    # Exit a parse tree produced by littleDuckParser#expression_multiple.
    def exitExpression_multiple(self, ctx:littleDuckParser.Expression_multipleContext):
        pass


    # Enter a parse tree produced by littleDuckParser#assignment.
    def enterAssignment(self, ctx:littleDuckParser.AssignmentContext):
        pass

    # Exit a parse tree produced by littleDuckParser#assignment.
    def exitAssignment(self, ctx:littleDuckParser.AssignmentContext):
        pass


    # Enter a parse tree produced by littleDuckParser#condition.
    def enterCondition(self, ctx:littleDuckParser.ConditionContext):
        pass

    # Exit a parse tree produced by littleDuckParser#condition.
    def exitCondition(self, ctx:littleDuckParser.ConditionContext):
        pass


    # Enter a parse tree produced by littleDuckParser#cycle.
    def enterCycle(self, ctx:littleDuckParser.CycleContext):
        pass

    # Exit a parse tree produced by littleDuckParser#cycle.
    def exitCycle(self, ctx:littleDuckParser.CycleContext):
        pass


    # Enter a parse tree produced by littleDuckParser#f_call.
    def enterF_call(self, ctx:littleDuckParser.F_callContext):
        pass

    # Exit a parse tree produced by littleDuckParser#f_call.
    def exitF_call(self, ctx:littleDuckParser.F_callContext):
        pass


    # Enter a parse tree produced by littleDuckParser#print.
    def enterPrint(self, ctx:littleDuckParser.PrintContext):
        pass

    # Exit a parse tree produced by littleDuckParser#print.
    def exitPrint(self, ctx:littleDuckParser.PrintContext):
        pass


    # Enter a parse tree produced by littleDuckParser#expression.
    def enterExpression(self, ctx:littleDuckParser.ExpressionContext):
        pass

    # Exit a parse tree produced by littleDuckParser#expression.
    def exitExpression(self, ctx:littleDuckParser.ExpressionContext):
        pass


    # Enter a parse tree produced by littleDuckParser#exp.
    def enterExp(self, ctx:littleDuckParser.ExpContext):
        pass

    # Exit a parse tree produced by littleDuckParser#exp.
    def exitExp(self, ctx:littleDuckParser.ExpContext):
        pass


    # Enter a parse tree produced by littleDuckParser#term.
    def enterTerm(self, ctx:littleDuckParser.TermContext):
        pass

    # Exit a parse tree produced by littleDuckParser#term.
    def exitTerm(self, ctx:littleDuckParser.TermContext):
        pass


    # Enter a parse tree produced by littleDuckParser#num_construct.
    def enterNum_construct(self, ctx:littleDuckParser.Num_constructContext):
        pass

    # Exit a parse tree produced by littleDuckParser#num_construct.
    def exitNum_construct(self, ctx:littleDuckParser.Num_constructContext):
        pass


    # Enter a parse tree produced by littleDuckParser#factor.
    def enterFactor(self, ctx:littleDuckParser.FactorContext):
        pass

    # Exit a parse tree produced by littleDuckParser#factor.
    def exitFactor(self, ctx:littleDuckParser.FactorContext):
        pass



del littleDuckParser