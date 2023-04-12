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
        4,1,19,136,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,
        5,3,43,8,3,10,3,12,3,46,9,3,1,3,1,3,1,4,1,4,3,4,52,8,4,1,4,1,4,1,
        4,1,4,3,4,58,8,4,1,4,1,4,3,4,62,8,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,
        70,8,5,1,6,1,6,1,6,1,6,5,6,76,8,6,10,6,12,6,79,9,6,3,6,81,8,6,1,
        6,1,6,5,6,85,8,6,10,6,12,6,88,9,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,96,
        8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,3,9,107,8,9,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,119,8,10,10,10,12,10,122,
        9,10,1,10,1,10,1,11,1,11,1,11,5,11,129,8,11,10,11,12,11,132,9,11,
        1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,1,2,0,
        1,1,17,19,141,0,29,1,0,0,0,2,34,1,0,0,0,4,37,1,0,0,0,6,40,1,0,0,
        0,8,61,1,0,0,0,10,69,1,0,0,0,12,71,1,0,0,0,14,91,1,0,0,0,16,99,1,
        0,0,0,18,103,1,0,0,0,20,112,1,0,0,0,22,125,1,0,0,0,24,133,1,0,0,
        0,26,28,3,8,4,0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,
        1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,0,0,1,33,1,1,0,0,0,34,
        35,3,4,2,0,35,36,3,6,3,0,36,3,1,0,0,0,37,38,5,11,0,0,38,39,3,10,
        5,0,39,5,1,0,0,0,40,44,5,10,0,0,41,43,3,8,4,0,42,41,1,0,0,0,43,46,
        1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,
        47,48,5,12,0,0,48,7,1,0,0,0,49,52,3,10,5,0,50,52,3,2,1,0,51,49,1,
        0,0,0,51,50,1,0,0,0,52,53,1,0,0,0,53,54,5,0,0,1,54,62,1,0,0,0,55,
        58,3,10,5,0,56,58,3,2,1,0,57,55,1,0,0,0,57,56,1,0,0,0,57,58,1,0,
        0,0,58,59,1,0,0,0,59,62,5,3,0,0,60,62,3,2,1,0,61,51,1,0,0,0,61,57,
        1,0,0,0,61,60,1,0,0,0,62,9,1,0,0,0,63,70,3,24,12,0,64,70,3,14,7,
        0,65,70,3,16,8,0,66,70,3,18,9,0,67,70,3,20,10,0,68,70,3,12,6,0,69,
        63,1,0,0,0,69,64,1,0,0,0,69,65,1,0,0,0,69,66,1,0,0,0,69,67,1,0,0,
        0,69,68,1,0,0,0,70,11,1,0,0,0,71,80,5,13,0,0,72,77,5,19,0,0,73,74,
        5,4,0,0,74,76,5,19,0,0,75,73,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,
        77,78,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,80,72,1,0,0,0,80,81,1,
        0,0,0,81,82,1,0,0,0,82,86,5,10,0,0,83,85,3,8,4,0,84,83,1,0,0,0,85,
        88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,
        0,89,90,5,14,0,0,90,13,1,0,0,0,91,92,5,9,0,0,92,95,3,10,5,0,93,94,
        5,4,0,0,94,96,3,22,11,0,95,93,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,
        0,97,98,5,5,0,0,98,15,1,0,0,0,99,100,5,6,0,0,100,101,3,22,11,0,101,
        102,5,5,0,0,102,17,1,0,0,0,103,106,5,7,0,0,104,107,5,19,0,0,105,
        107,3,20,10,0,106,104,1,0,0,0,106,105,1,0,0,0,107,108,1,0,0,0,108,
        109,5,4,0,0,109,110,3,10,5,0,110,111,5,5,0,0,111,19,1,0,0,0,112,
        113,5,8,0,0,113,114,3,10,5,0,114,115,5,4,0,0,115,120,3,10,5,0,116,
        117,5,4,0,0,117,119,3,10,5,0,118,116,1,0,0,0,119,122,1,0,0,0,120,
        118,1,0,0,0,120,121,1,0,0,0,121,123,1,0,0,0,122,120,1,0,0,0,123,
        124,5,5,0,0,124,21,1,0,0,0,125,130,3,10,5,0,126,127,5,4,0,0,127,
        129,3,10,5,0,128,126,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,
        131,1,0,0,0,131,23,1,0,0,0,132,130,1,0,0,0,133,134,7,0,0,0,134,25,
        1,0,0,0,13,29,44,51,57,61,69,77,80,86,95,106,120,130
    ]

class switchParser ( Parser ):

    grammarFileName = "switch.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'L'", "'n'", 
                     "'l'", "<INVALID>", "'e'", "'i'", "'c'", "'B'", "'W'", 
                     "'w'", "'F'", "'f'", "'S'", "'s'" ]

    symbolicNames = [ "<INVALID>", "STRING", "WHITESPACE", "ENDLINE", "ARG_DELIM", 
                      "END_CALL", "MATH_OPS", "ASSIGNMENT_OP", "ACCESS_OP", 
                      "CALL_OP", "BLOCK_DELIM", "WHILE_LOOP_DELIM", "WHILE_LOOP_END", 
                      "FUNCTION_DELIM", "FUNCTION_END", "STRING_START", 
                      "NEXT_CHAR", "INT", "FLOAT", "NAME" ]

    RULE_switch_file = 0
    RULE_while_loop = 1
    RULE_while_test = 2
    RULE_while_block = 3
    RULE_line = 4
    RULE_expr = 5
    RULE_function = 6
    RULE_call = 7
    RULE_math_op = 8
    RULE_assignment = 9
    RULE_access = 10
    RULE_args = 11
    RULE_prim_expr = 12

    ruleNames =  [ "switch_file", "while_loop", "while_test", "while_block", 
                   "line", "expr", "function", "call", "math_op", "assignment", 
                   "access", "args", "prim_expr" ]

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
    STRING_START=15
    NEXT_CHAR=16
    INT=17
    FLOAT=18
    NAME=19

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
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 928714) != 0):
                self.state = 26
                self.line()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
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
            self.state = 34
            self.while_test()
            self.state = 35
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
            self.state = 37
            self.match(switchParser.WHILE_LOOP_DELIM)
            self.state = 38
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
            self.state = 40
            self.match(switchParser.BLOCK_DELIM)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 928714) != 0):
                self.state = 41
                self.line()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
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

        def EOF(self):
            return self.getToken(switchParser.EOF, 0)

        def while_loop(self):
            return self.getTypedRuleContext(switchParser.While_loopContext,0)


        def expr(self):
            return self.getTypedRuleContext(switchParser.ExprContext,0)


        def ENDLINE(self):
            return self.getToken(switchParser.ENDLINE, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 51
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 6, 7, 8, 9, 13, 17, 18, 19]:
                    self.state = 49
                    self.expr()
                    pass
                elif token in [11]:
                    self.state = 50
                    self.while_loop()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 53
                self.match(switchParser.EOF)
                pass

            elif la_ == 2:
                self.state = 57
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 6, 7, 8, 9, 13, 17, 18, 19]:
                    self.state = 55
                    self.expr()
                    pass
                elif token in [11]:
                    self.state = 56
                    self.while_loop()
                    pass
                elif token in [3]:
                    pass
                else:
                    pass
                self.state = 59
                self.match(switchParser.ENDLINE)
                pass

            elif la_ == 3:
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
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 17, 18, 19]:
                self.state = 63
                self.prim_expr()
                pass
            elif token in [9]:
                self.state = 64
                self.call()
                pass
            elif token in [6]:
                self.state = 65
                self.math_op()
                pass
            elif token in [7]:
                self.state = 66
                self.assignment()
                pass
            elif token in [8]:
                self.state = 67
                self.access()
                pass
            elif token in [13]:
                self.state = 68
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
        self.enterRule(localctx, 12, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(switchParser.FUNCTION_DELIM)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 72
                self.match(switchParser.NAME)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 73
                    self.match(switchParser.ARG_DELIM)
                    self.state = 74
                    self.match(switchParser.NAME)
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 82
            self.match(switchParser.BLOCK_DELIM)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 928714) != 0):
                self.state = 83
                self.line()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
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
        self.enterRule(localctx, 14, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(switchParser.CALL_OP)
            self.state = 92
            self.expr()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 93
                self.match(switchParser.ARG_DELIM)
                self.state = 94
                self.args()


            self.state = 97
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
        self.enterRule(localctx, 16, self.RULE_math_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(switchParser.MATH_OPS)
            self.state = 100
            self.args()
            self.state = 101
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
        self.enterRule(localctx, 18, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(switchParser.ASSIGNMENT_OP)
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.state = 104
                self.match(switchParser.NAME)
                pass
            elif token in [8]:
                self.state = 105
                self.access()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 108
            self.match(switchParser.ARG_DELIM)
            self.state = 109
            self.expr()
            self.state = 110
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
        self.enterRule(localctx, 20, self.RULE_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(switchParser.ACCESS_OP)
            self.state = 113
            self.expr()
            self.state = 114
            self.match(switchParser.ARG_DELIM)
            self.state = 115
            self.expr()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 116
                self.match(switchParser.ARG_DELIM)
                self.state = 117
                self.expr()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
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
        self.enterRule(localctx, 22, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.expr()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 126
                self.match(switchParser.ARG_DELIM)
                self.state = 127
                self.expr()
                self.state = 132
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
        self.enterRule(localctx, 24, self.RULE_prim_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917506) != 0)):
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





