# Generated from switch.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .switchParser import switchParser
else:
    from switchParser import switchParser

# This class defines a complete listener for a parse tree produced by switchParser.
class switchListener(ParseTreeListener):

    # Enter a parse tree produced by switchParser#expr.
    def enterExpr(self, ctx:switchParser.ExprContext):
        pass

    # Exit a parse tree produced by switchParser#expr.
    def exitExpr(self, ctx:switchParser.ExprContext):
        pass


    # Enter a parse tree produced by switchParser#call.
    def enterCall(self, ctx:switchParser.CallContext):
        pass

    # Exit a parse tree produced by switchParser#call.
    def exitCall(self, ctx:switchParser.CallContext):
        pass


    # Enter a parse tree produced by switchParser#m_expr.
    def enterM_expr(self, ctx:switchParser.M_exprContext):
        pass

    # Exit a parse tree produced by switchParser#m_expr.
    def exitM_expr(self, ctx:switchParser.M_exprContext):
        pass


    # Enter a parse tree produced by switchParser#add_sub_expr.
    def enterAdd_sub_expr(self, ctx:switchParser.Add_sub_exprContext):
        pass

    # Exit a parse tree produced by switchParser#add_sub_expr.
    def exitAdd_sub_expr(self, ctx:switchParser.Add_sub_exprContext):
        pass


    # Enter a parse tree produced by switchParser#assignment.
    def enterAssignment(self, ctx:switchParser.AssignmentContext):
        pass

    # Exit a parse tree produced by switchParser#assignment.
    def exitAssignment(self, ctx:switchParser.AssignmentContext):
        pass


    # Enter a parse tree produced by switchParser#access.
    def enterAccess(self, ctx:switchParser.AccessContext):
        pass

    # Exit a parse tree produced by switchParser#access.
    def exitAccess(self, ctx:switchParser.AccessContext):
        pass


    # Enter a parse tree produced by switchParser#comp.
    def enterComp(self, ctx:switchParser.CompContext):
        pass

    # Exit a parse tree produced by switchParser#comp.
    def exitComp(self, ctx:switchParser.CompContext):
        pass


    # Enter a parse tree produced by switchParser#args.
    def enterArgs(self, ctx:switchParser.ArgsContext):
        pass

    # Exit a parse tree produced by switchParser#args.
    def exitArgs(self, ctx:switchParser.ArgsContext):
        pass


    # Enter a parse tree produced by switchParser#prim_expr.
    def enterPrim_expr(self, ctx:switchParser.Prim_exprContext):
        pass

    # Exit a parse tree produced by switchParser#prim_expr.
    def exitPrim_expr(self, ctx:switchParser.Prim_exprContext):
        pass



del switchParser