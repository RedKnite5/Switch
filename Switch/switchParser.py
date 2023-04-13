# Generated from switch.g4 by ANTLR 4.12.0
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
        4,1,20,145,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,1,0,1,1,1,1,1,1,1,
        2,1,2,1,2,1,3,1,3,5,3,47,8,3,10,3,12,3,50,9,3,1,3,1,3,1,4,1,4,1,
        4,1,4,3,4,58,8,4,1,4,1,4,3,4,62,8,4,1,5,1,5,1,5,3,5,67,8,5,1,6,1,
        6,3,6,71,8,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,79,8,7,1,8,1,8,1,8,1,8,
        5,8,85,8,8,10,8,12,8,88,9,8,3,8,90,8,8,1,8,1,8,5,8,94,8,8,10,8,12,
        8,97,9,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,105,8,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,11,1,11,1,11,3,11,116,8,11,1,11,1,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,1,12,5,12,128,8,12,10,12,12,12,131,9,12,1,12,1,
        12,1,13,1,13,1,13,5,13,138,8,13,10,13,12,13,141,9,13,1,14,1,14,1,
        14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,1,2,0,1,1,18,
        20,149,0,33,1,0,0,0,2,38,1,0,0,0,4,41,1,0,0,0,6,44,1,0,0,0,8,61,
        1,0,0,0,10,66,1,0,0,0,12,68,1,0,0,0,14,78,1,0,0,0,16,80,1,0,0,0,
        18,100,1,0,0,0,20,108,1,0,0,0,22,112,1,0,0,0,24,121,1,0,0,0,26,134,
        1,0,0,0,28,142,1,0,0,0,30,32,3,8,4,0,31,30,1,0,0,0,32,35,1,0,0,0,
        33,31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,0,36,37,5,
        0,0,1,37,1,1,0,0,0,38,39,3,4,2,0,39,40,3,6,3,0,40,3,1,0,0,0,41,42,
        5,11,0,0,42,43,3,14,7,0,43,5,1,0,0,0,44,48,5,10,0,0,45,47,3,8,4,
        0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,
        1,0,0,0,50,48,1,0,0,0,51,52,5,12,0,0,52,7,1,0,0,0,53,54,3,10,5,0,
        54,55,5,0,0,1,55,62,1,0,0,0,56,58,3,10,5,0,57,56,1,0,0,0,57,58,1,
        0,0,0,58,59,1,0,0,0,59,62,5,3,0,0,60,62,3,2,1,0,61,53,1,0,0,0,61,
        57,1,0,0,0,61,60,1,0,0,0,62,9,1,0,0,0,63,67,3,14,7,0,64,67,3,2,1,
        0,65,67,3,12,6,0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,11,
        1,0,0,0,68,70,5,15,0,0,69,71,3,14,7,0,70,69,1,0,0,0,70,71,1,0,0,
        0,71,13,1,0,0,0,72,79,3,28,14,0,73,79,3,18,9,0,74,79,3,20,10,0,75,
        79,3,22,11,0,76,79,3,24,12,0,77,79,3,16,8,0,78,72,1,0,0,0,78,73,
        1,0,0,0,78,74,1,0,0,0,78,75,1,0,0,0,78,76,1,0,0,0,78,77,1,0,0,0,
        79,15,1,0,0,0,80,89,5,13,0,0,81,86,5,20,0,0,82,83,5,4,0,0,83,85,
        5,20,0,0,84,82,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,
        87,90,1,0,0,0,88,86,1,0,0,0,89,81,1,0,0,0,89,90,1,0,0,0,90,91,1,
        0,0,0,91,95,5,10,0,0,92,94,3,8,4,0,93,92,1,0,0,0,94,97,1,0,0,0,95,
        93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,99,5,14,
        0,0,99,17,1,0,0,0,100,101,5,9,0,0,101,104,3,14,7,0,102,103,5,4,0,
        0,103,105,3,26,13,0,104,102,1,0,0,0,104,105,1,0,0,0,105,106,1,0,
        0,0,106,107,5,5,0,0,107,19,1,0,0,0,108,109,5,6,0,0,109,110,3,26,
        13,0,110,111,5,5,0,0,111,21,1,0,0,0,112,115,5,7,0,0,113,116,5,20,
        0,0,114,116,3,24,12,0,115,113,1,0,0,0,115,114,1,0,0,0,116,117,1,
        0,0,0,117,118,5,4,0,0,118,119,3,14,7,0,119,120,5,5,0,0,120,23,1,
        0,0,0,121,122,5,8,0,0,122,123,3,14,7,0,123,124,5,4,0,0,124,129,3,
        14,7,0,125,126,5,4,0,0,126,128,3,14,7,0,127,125,1,0,0,0,128,131,
        1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,132,1,0,0,0,131,129,
        1,0,0,0,132,133,5,5,0,0,133,25,1,0,0,0,134,139,3,14,7,0,135,136,
        5,4,0,0,136,138,3,14,7,0,137,135,1,0,0,0,138,141,1,0,0,0,139,137,
        1,0,0,0,139,140,1,0,0,0,140,27,1,0,0,0,141,139,1,0,0,0,142,143,7,
        0,0,0,143,29,1,0,0,0,14,33,48,57,61,66,70,78,86,89,95,104,115,129,
        139
    ]

class switchParser ( Parser ):

    grammarFileName = "switch.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'L'", "'n'", 
                     "'l'", "<INVALID>", "'e'", "'i'", "'c'", "'B'", "'W'", 
                     "'w'", "'F'", "'f'", "'R'", "'S'", "'s'" ]

    symbolicNames = [ "<INVALID>", "STRING", "WHITESPACE", "ENDLINE", "ARG_DELIM", 
                      "END_CALL", "MATH_OPS", "ASSIGNMENT_OP", "ACCESS_OP", 
                      "CALL_OP", "BLOCK_DELIM", "WHILE_LOOP_DELIM", "WHILE_LOOP_END", 
                      "FUNCTION_DELIM", "FUNCTION_END", "FUNCTION_RETURN", 
                      "STRING_START", "NEXT_CHAR", "INT", "FLOAT", "NAME" ]

    RULE_switch_file = 0
    RULE_while_loop = 1
    RULE_while_test = 2
    RULE_while_block = 3
    RULE_line = 4
    RULE_statement = 5
    RULE_return_statement = 6
    RULE_expr = 7
    RULE_function = 8
    RULE_call = 9
    RULE_math_op = 10
    RULE_assignment = 11
    RULE_access = 12
    RULE_args = 13
    RULE_prim_expr = 14

    ruleNames =  [ "switch_file", "while_loop", "while_test", "while_block", 
                   "line", "statement", "return_statement", "expr", "function", 
                   "call", "math_op", "assignment", "access", "args", "prim_expr" ]

    EOF = Token.EOF
    STRING=1
    WHITESPACE=2
    ENDLINE=3
    ARG_DELIM=4
    END_CALL=5
    MATH_OPS=6
    ASSIGNMENT_OP=7
    ACCESS_OP=8
    CALL_OP=9
    BLOCK_DELIM=10
    WHILE_LOOP_DELIM=11
    WHILE_LOOP_END=12
    FUNCTION_DELIM=13
    FUNCTION_END=14
    FUNCTION_RETURN=15
    STRING_START=16
    NEXT_CHAR=17
    INT=18
    FLOAT=19
    NAME=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Switch_fileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(switchParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(switchParser.LineContext)
            else:
                return self.getTypedRuleContext(switchParser.LineContext,i)


        def getRuleIndex(self):
            return switchParser.RULE_switch_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_file" ):
                listener.enterSwitch_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_file" ):
                listener.exitSwitch_file(self)




    def switch_file(self):

        localctx = switchParser.Switch_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_switch_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1878986) != 0):
                self.state = 30
                self.line()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(switchParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def while_test(self):
            return self.getTypedRuleContext(switchParser.While_testContext,0)


        def while_block(self):
            return self.getTypedRuleContext(switchParser.While_blockContext,0)


        def getRuleIndex(self):
            return switchParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)




    def while_loop(self):

        localctx = switchParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.while_test()
            self.state = 39
            self.while_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_testContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE_LOOP_DELIM(self):
            return self.getToken(switchParser.WHILE_LOOP_DELIM, 0)

        def expr(self):
            return self.getTypedRuleContext(switchParser.ExprContext,0)


        def getRuleIndex(self):
            return switchParser.RULE_while_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_test" ):
                listener.enterWhile_test(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_test" ):
                listener.exitWhile_test(self)




    def while_test(self):

        localctx = switchParser.While_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_while_test)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(switchParser.WHILE_LOOP_DELIM)
            self.state = 42
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCK_DELIM(self):
            return self.getToken(switchParser.BLOCK_DELIM, 0)

        def WHILE_LOOP_END(self):
            return self.getToken(switchParser.WHILE_LOOP_END, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(switchParser.LineContext)
            else:
                return self.getTypedRuleContext(switchParser.LineContext,i)


        def getRuleIndex(self):
            return switchParser.RULE_while_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_block" ):
                listener.enterWhile_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_block" ):
                listener.exitWhile_block(self)




    def while_block(self):

        localctx = switchParser.While_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_while_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(switchParser.BLOCK_DELIM)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1878986) != 0):
                self.state = 45
                self.line()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(switchParser.WHILE_LOOP_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(switchParser.StatementContext,0)


        def EOF(self):
            return self.getToken(switchParser.EOF, 0)

        def ENDLINE(self):
            return self.getToken(switchParser.ENDLINE, 0)

        def while_loop(self):
            return self.getTypedRuleContext(switchParser.While_loopContext,0)


        def getRuleIndex(self):
            return switchParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = switchParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.statement()
                self.state = 54
                self.match(switchParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1878978) != 0):
                    self.state = 56
                    self.statement()


                self.state = 59
                self.match(switchParser.ENDLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.while_loop()
                pass


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

        def expr(self):
            return self.getTypedRuleContext(switchParser.ExprContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(switchParser.While_loopContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(switchParser.Return_statementContext,0)


        def getRuleIndex(self):
            return switchParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = switchParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 6, 7, 8, 9, 13, 18, 19, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.expr()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.while_loop()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.return_statement()
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


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_RETURN(self):
            return self.getToken(switchParser.FUNCTION_RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(switchParser.ExprContext,0)


        def getRuleIndex(self):
            return switchParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = switchParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(switchParser.FUNCTION_RETURN)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1844162) != 0):
                self.state = 69
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_expr(self):
            return self.getTypedRuleContext(switchParser.Prim_exprContext,0)


        def call(self):
            return self.getTypedRuleContext(switchParser.CallContext,0)


        def math_op(self):
            return self.getTypedRuleContext(switchParser.Math_opContext,0)


        def assignment(self):
            return self.getTypedRuleContext(switchParser.AssignmentContext,0)


        def access(self):
            return self.getTypedRuleContext(switchParser.AccessContext,0)


        def function(self):
            return self.getTypedRuleContext(switchParser.FunctionContext,0)


        def getRuleIndex(self):
            return switchParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = switchParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 18, 19, 20]:
                self.state = 72
                self.prim_expr()
                pass
            elif token in [9]:
                self.state = 73
                self.call()
                pass
            elif token in [6]:
                self.state = 74
                self.math_op()
                pass
            elif token in [7]:
                self.state = 75
                self.assignment()
                pass
            elif token in [8]:
                self.state = 76
                self.access()
                pass
            elif token in [13]:
                self.state = 77
                self.function()
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


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_DELIM(self):
            return self.getToken(switchParser.FUNCTION_DELIM, 0)

        def BLOCK_DELIM(self):
            return self.getToken(switchParser.BLOCK_DELIM, 0)

        def FUNCTION_END(self):
            return self.getToken(switchParser.FUNCTION_END, 0)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(switchParser.NAME)
            else:
                return self.getToken(switchParser.NAME, i)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(switchParser.LineContext)
            else:
                return self.getTypedRuleContext(switchParser.LineContext,i)


        def ARG_DELIM(self, i:int=None):
            if i is None:
                return self.getTokens(switchParser.ARG_DELIM)
            else:
                return self.getToken(switchParser.ARG_DELIM, i)

        def getRuleIndex(self):
            return switchParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = switchParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(switchParser.FUNCTION_DELIM)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 81
                self.match(switchParser.NAME)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 82
                    self.match(switchParser.ARG_DELIM)
                    self.state = 83
                    self.match(switchParser.NAME)
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 91
            self.match(switchParser.BLOCK_DELIM)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1878986) != 0):
                self.state = 92
                self.line()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(switchParser.FUNCTION_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL_OP(self):
            return self.getToken(switchParser.CALL_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(switchParser.ExprContext,0)


        def END_CALL(self):
            return self.getToken(switchParser.END_CALL, 0)

        def ARG_DELIM(self):
            return self.getToken(switchParser.ARG_DELIM, 0)

        def args(self):
            return self.getTypedRuleContext(switchParser.ArgsContext,0)


        def getRuleIndex(self):
            return switchParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = switchParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(switchParser.CALL_OP)
            self.state = 101
            self.expr()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 102
                self.match(switchParser.ARG_DELIM)
                self.state = 103
                self.args()


            self.state = 106
            self.match(switchParser.END_CALL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Math_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MATH_OPS(self):
            return self.getToken(switchParser.MATH_OPS, 0)

        def args(self):
            return self.getTypedRuleContext(switchParser.ArgsContext,0)


        def END_CALL(self):
            return self.getToken(switchParser.END_CALL, 0)

        def getRuleIndex(self):
            return switchParser.RULE_math_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_op" ):
                listener.enterMath_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_op" ):
                listener.exitMath_op(self)




    def math_op(self):

        localctx = switchParser.Math_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_math_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(switchParser.MATH_OPS)
            self.state = 109
            self.args()
            self.state = 110
            self.match(switchParser.END_CALL)
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

        def ASSIGNMENT_OP(self):
            return self.getToken(switchParser.ASSIGNMENT_OP, 0)

        def ARG_DELIM(self):
            return self.getToken(switchParser.ARG_DELIM, 0)

        def expr(self):
            return self.getTypedRuleContext(switchParser.ExprContext,0)


        def END_CALL(self):
            return self.getToken(switchParser.END_CALL, 0)

        def NAME(self):
            return self.getToken(switchParser.NAME, 0)

        def access(self):
            return self.getTypedRuleContext(switchParser.AccessContext,0)


        def getRuleIndex(self):
            return switchParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = switchParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(switchParser.ASSIGNMENT_OP)
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 113
                self.match(switchParser.NAME)
                pass
            elif token in [8]:
                self.state = 114
                self.access()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 117
            self.match(switchParser.ARG_DELIM)
            self.state = 118
            self.expr()
            self.state = 119
            self.match(switchParser.END_CALL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACCESS_OP(self):
            return self.getToken(switchParser.ACCESS_OP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(switchParser.ExprContext)
            else:
                return self.getTypedRuleContext(switchParser.ExprContext,i)


        def ARG_DELIM(self, i:int=None):
            if i is None:
                return self.getTokens(switchParser.ARG_DELIM)
            else:
                return self.getToken(switchParser.ARG_DELIM, i)

        def END_CALL(self):
            return self.getToken(switchParser.END_CALL, 0)

        def getRuleIndex(self):
            return switchParser.RULE_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccess" ):
                listener.enterAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccess" ):
                listener.exitAccess(self)




    def access(self):

        localctx = switchParser.AccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(switchParser.ACCESS_OP)
            self.state = 122
            self.expr()
            self.state = 123
            self.match(switchParser.ARG_DELIM)
            self.state = 124
            self.expr()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 125
                self.match(switchParser.ARG_DELIM)
                self.state = 126
                self.expr()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self.match(switchParser.END_CALL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(switchParser.ExprContext)
            else:
                return self.getTypedRuleContext(switchParser.ExprContext,i)


        def ARG_DELIM(self, i:int=None):
            if i is None:
                return self.getTokens(switchParser.ARG_DELIM)
            else:
                return self.getToken(switchParser.ARG_DELIM, i)

        def getRuleIndex(self):
            return switchParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = switchParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.expr()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 135
                self.match(switchParser.ARG_DELIM)
                self.state = 136
                self.expr()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prim_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(switchParser.INT, 0)

        def FLOAT(self):
            return self.getToken(switchParser.FLOAT, 0)

        def NAME(self):
            return self.getToken(switchParser.NAME, 0)

        def STRING(self):
            return self.getToken(switchParser.STRING, 0)

        def getRuleIndex(self):
            return switchParser.RULE_prim_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrim_expr" ):
                listener.enterPrim_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrim_expr" ):
                listener.exitPrim_expr(self)




    def prim_expr(self):

        localctx = switchParser.Prim_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_prim_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835010) != 0)):
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





