# Generated from /Users/paulinacovarrubias/Documents/compilador_LittleDuck/littleDuck.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .littleDuckParser import littleDuckParser
else:
    from littleDuckParser import littleDuckParser

# This class defines a complete generic visitor for a parse tree produced by littleDuckParser.

class littleDuckVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by littleDuckParser#program.
    def visitProgram(self, ctx:littleDuckParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#body.
    def visitBody(self, ctx:littleDuckParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#type.
    def visitType(self, ctx:littleDuckParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#vars.
    def visitVars(self, ctx:littleDuckParser.VarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#var_group.
    def visitVar_group(self, ctx:littleDuckParser.Var_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#inner_funcs.
    def visitInner_funcs(self, ctx:littleDuckParser.Inner_funcsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#funcs.
    def visitFuncs(self, ctx:littleDuckParser.FuncsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#statement.
    def visitStatement(self, ctx:littleDuckParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#expression_multiple.
    def visitExpression_multiple(self, ctx:littleDuckParser.Expression_multipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#assignment.
    def visitAssignment(self, ctx:littleDuckParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#condition.
    def visitCondition(self, ctx:littleDuckParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#cycle.
    def visitCycle(self, ctx:littleDuckParser.CycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#f_call.
    def visitF_call(self, ctx:littleDuckParser.F_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#print.
    def visitPrint(self, ctx:littleDuckParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#expression.
    def visitExpression(self, ctx:littleDuckParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#exp.
    def visitExp(self, ctx:littleDuckParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#term.
    def visitTerm(self, ctx:littleDuckParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#num_construct.
    def visitNum_construct(self, ctx:littleDuckParser.Num_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by littleDuckParser#factor.
    def visitFactor(self, ctx:littleDuckParser.FactorContext):
        return self.visitChildren(ctx)



del littleDuckParser