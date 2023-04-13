# Generated from switch.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .switchParser import switchParser
else:
    from switchParser import switchParser

# This class defines a complete listener for a parse tree produced by switchParser.
class switchListener(ParseTreeListener):

    # Enter a parse tree produced by switchParser#switch_file.
    def enterSwitch_file(self, ctx:switchParser.Switch_fileContext):
        pass

    # Exit a parse tree produced by switchParser#switch_file.
    def exitSwitch_file(self, ctx:switchParser.Switch_fileContext):
        pass


    # Enter a parse tree produced by switchParser#while_loop.
    def enterWhile_loop(self, ctx:switchParser.While_loopContext):
        pass

    # Exit a parse tree produced by switchParser#while_loop.
    def exitWhile_loop(self, ctx:switchParser.While_loopContext):
        pass


    # Enter a parse tree produced by switchParser#while_test.
    def enterWhile_test(self, ctx:switchParser.While_testContext):
        pass

    # Exit a parse tree produced by switchParser#while_test.
    def exitWhile_test(self, ctx:switchParser.While_testContext):
        pass


    # Enter a parse tree produced by switchParser#while_block.
    def enterWhile_block(self, ctx:switchParser.While_blockContext):
        pass

    # Exit a parse tree produced by switchParser#while_block.
    def exitWhile_block(self, ctx:switchParser.While_blockContext):
        pass


    # Enter a parse tree produced by switchParser#line.
    def enterLine(self, ctx:switchParser.LineContext):
        pass

    # Exit a parse tree produced by switchParser#line.
    def exitLine(self, ctx:switchParser.LineContext):
        pass


    # Enter a parse tree produced by switchParser#statement.
    def enterStatement(self, ctx:switchParser.StatementContext):
        pass

    # Exit a parse tree produced by switchParser#statement.
    def exitStatement(self, ctx:switchParser.StatementContext):
        pass


    # Enter a parse tree produced by switchParser#return_statement.
    def enterReturn_statement(self, ctx:switchParser.Return_statementContext):
        pass

    # Exit a parse tree produced by switchParser#return_statement.
    def exitReturn_statement(self, ctx:switchParser.Return_statementContext):
        pass


    # Enter a parse tree produced by switchParser#expr.
    def enterExpr(self, ctx:switchParser.ExprContext):
        pass

    # Exit a parse tree produced by switchParser#expr.
    def exitExpr(self, ctx:switchParser.ExprContext):
        pass


    # Enter a parse tree produced by switchParser#function.
    def enterFunction(self, ctx:switchParser.FunctionContext):
        pass

    # Exit a parse tree produced by switchParser#function.
    def exitFunction(self, ctx:switchParser.FunctionContext):
        pass


    # Enter a parse tree produced by switchParser#call.
    def enterCall(self, ctx:switchParser.CallContext):
        pass

    # Exit a parse tree produced by switchParser#call.
    def exitCall(self, ctx:switchParser.CallContext):
        pass


    # Enter a parse tree produced by switchParser#math_op.
    def enterMath_op(self, ctx:switchParser.Math_opContext):
        pass

    # Exit a parse tree produced by switchParser#math_op.
    def exitMath_op(self, ctx:switchParser.Math_opContext):
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