# Generated from switch.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("o\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\3\2\7\2!\n\2\f\2\16\2$\13\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\7\5\60\n\5\f\5\16\5\63")
        buf.write("\13\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6;\n\6\3\6\5\6>\n\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7G\n\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\5\13X\n")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\7\16h\n\16\f\16\16\16k\13\16\3\17\3\17\3\17")
        buf.write("\2\2\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\3\4\2\n")
        buf.write("\n\21\23\2m\2\"\3\2\2\2\4\'\3\2\2\2\6*\3\2\2\2\b-\3\2")
        buf.write("\2\2\n=\3\2\2\2\fF\3\2\2\2\16H\3\2\2\2\20N\3\2\2\2\22")
        buf.write("Q\3\2\2\2\24T\3\2\2\2\26\\\3\2\2\2\30a\3\2\2\2\32d\3\2")
        buf.write("\2\2\34l\3\2\2\2\36!\5\n\6\2\37!\5\4\3\2 \36\3\2\2\2 ")
        buf.write("\37\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2")
        buf.write("$\"\3\2\2\2%&\7\2\2\3&\3\3\2\2\2\'(\5\6\4\2()\5\b\5\2")
        buf.write(")\5\3\2\2\2*+\7\3\2\2+,\5\f\7\2,\7\3\2\2\2-\61\7\4\2\2")
        buf.write(".\60\5\n\6\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62")
        buf.write("\3\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2\64\65\7\5\2\2\65")
        buf.write("\t\3\2\2\2\66\67\5\f\7\2\678\7\2\2\38>\3\2\2\29;\5\f\7")
        buf.write("\2:9\3\2\2\2:;\3\2\2\2;<\3\2\2\2<>\7\f\2\2=\66\3\2\2\2")
        buf.write("=:\3\2\2\2>\13\3\2\2\2?G\5\34\17\2@G\5\16\b\2AG\5\20\t")
        buf.write("\2BG\5\22\n\2CG\5\24\13\2DG\5\26\f\2EG\5\30\r\2F?\3\2")
        buf.write("\2\2F@\3\2\2\2FA\3\2\2\2FB\3\2\2\2FC\3\2\2\2FD\3\2\2\2")
        buf.write("FE\3\2\2\2G\r\3\2\2\2HI\7\6\2\2IJ\5\f\7\2JK\7\r\2\2KL")
        buf.write("\5\32\16\2LM\7\7\2\2M\17\3\2\2\2NO\7\16\2\2OP\5\32\16")
        buf.write("\2P\21\3\2\2\2QR\7\17\2\2RS\5\32\16\2S\23\3\2\2\2TW\7")
        buf.write("\b\2\2UX\7\23\2\2VX\5\26\f\2WU\3\2\2\2WV\3\2\2\2XY\3\2")
        buf.write("\2\2YZ\7\r\2\2Z[\5\f\7\2[\25\3\2\2\2\\]\7\t\2\2]^\5\f")
        buf.write("\7\2^_\7\r\2\2_`\5\32\16\2`\27\3\2\2\2ab\7\20\2\2bc\5")
        buf.write("\32\16\2c\31\3\2\2\2di\5\f\7\2ef\7\r\2\2fh\5\f\7\2ge\3")
        buf.write("\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2j\33\3\2\2\2ki\3\2")
        buf.write("\2\2lm\t\2\2\2m\35\3\2\2\2\n \"\61:=FWi")
        return buf.getvalue()


class switchParser ( Parser ):

    grammarFileName = "switch.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'W'", "'Wb'", "'w'", "'c'", "'l'", "'e'", 
                     "'i'", "<INVALID>", "<INVALID>", "'L'", "'n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "STRING", "WHITESPACE", "ENDLINE", "ARG_DELIM", "MATH_OPS_M", 
                      "MATH_OPS_A", "COMPARISON_OPS", "INT", "FLOAT", "NAME" ]

    RULE_switch_file = 0
    RULE_while_loop = 1
    RULE_while_test = 2
    RULE_while_block = 3
    RULE_line = 4
    RULE_expr = 5
    RULE_call = 6
    RULE_mult = 7
    RULE_add_sub_expr = 8
    RULE_assignment = 9
    RULE_access = 10
    RULE_comp = 11
    RULE_args = 12
    RULE_prim_expr = 13

    ruleNames =  [ "switch_file", "while_loop", "while_test", "while_block", 
                   "line", "expr", "call", "mult", "add_sub_expr", "assignment", 
                   "access", "comp", "args", "prim_expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    STRING=8
    WHITESPACE=9
    ENDLINE=10
    ARG_DELIM=11
    MATH_OPS_M=12
    MATH_OPS_A=13
    COMPARISON_OPS=14
    INT=15
    FLOAT=16
    NAME=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Switch_fileContext(ParserRuleContext):

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


        def while_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(switchParser.While_loopContext)
            else:
                return self.getTypedRuleContext(switchParser.While_loopContext,i)


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
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << switchParser.T__0) | (1 << switchParser.T__3) | (1 << switchParser.T__5) | (1 << switchParser.T__6) | (1 << switchParser.STRING) | (1 << switchParser.ENDLINE) | (1 << switchParser.MATH_OPS_M) | (1 << switchParser.MATH_OPS_A) | (1 << switchParser.COMPARISON_OPS) | (1 << switchParser.INT) | (1 << switchParser.FLOAT) | (1 << switchParser.NAME))) != 0):
                self.state = 30
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [switchParser.T__3, switchParser.T__5, switchParser.T__6, switchParser.STRING, switchParser.ENDLINE, switchParser.MATH_OPS_M, switchParser.MATH_OPS_A, switchParser.COMPARISON_OPS, switchParser.INT, switchParser.FLOAT, switchParser.NAME]:
                    self.state = 28
                    self.line()
                    pass
                elif token in [switchParser.T__0]:
                    self.state = 29
                    self.while_loop()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(switchParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):

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
            self.state = 37
            self.while_test()
            self.state = 38
            self.while_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_testContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            self.state = 40
            self.match(switchParser.T__0)
            self.state = 41
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            self.state = 43
            self.match(switchParser.T__1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << switchParser.T__3) | (1 << switchParser.T__5) | (1 << switchParser.T__6) | (1 << switchParser.STRING) | (1 << switchParser.ENDLINE) | (1 << switchParser.MATH_OPS_M) | (1 << switchParser.MATH_OPS_A) | (1 << switchParser.COMPARISON_OPS) | (1 << switchParser.INT) | (1 << switchParser.FLOAT) | (1 << switchParser.NAME))) != 0):
                self.state = 44
                self.line()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(switchParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(switchParser.ExprContext,0)


        def EOF(self):
            return self.getToken(switchParser.EOF, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 52
                self.expr()
                self.state = 53
                self.match(switchParser.EOF)
                pass

            elif la_ == 2:
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << switchParser.T__3) | (1 << switchParser.T__5) | (1 << switchParser.T__6) | (1 << switchParser.STRING) | (1 << switchParser.MATH_OPS_M) | (1 << switchParser.MATH_OPS_A) | (1 << switchParser.COMPARISON_OPS) | (1 << switchParser.INT) | (1 << switchParser.FLOAT) | (1 << switchParser.NAME))) != 0):
                    self.state = 55
                    self.expr()


                self.state = 58
                self.match(switchParser.ENDLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_expr(self):
            return self.getTypedRuleContext(switchParser.Prim_exprContext,0)


        def call(self):
            return self.getTypedRuleContext(switchParser.CallContext,0)


        def mult(self):
            return self.getTypedRuleContext(switchParser.MultContext,0)


        def add_sub_expr(self):
            return self.getTypedRuleContext(switchParser.Add_sub_exprContext,0)


        def assignment(self):
            return self.getTypedRuleContext(switchParser.AssignmentContext,0)


        def access(self):
            return self.getTypedRuleContext(switchParser.AccessContext,0)


        def comp(self):
            return self.getTypedRuleContext(switchParser.CompContext,0)


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
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [switchParser.STRING, switchParser.INT, switchParser.FLOAT, switchParser.NAME]:
                self.state = 61
                self.prim_expr()
                pass
            elif token in [switchParser.T__3]:
                self.state = 62
                self.call()
                pass
            elif token in [switchParser.MATH_OPS_M]:
                self.state = 63
                self.mult()
                pass
            elif token in [switchParser.MATH_OPS_A]:
                self.state = 64
                self.add_sub_expr()
                pass
            elif token in [switchParser.T__5]:
                self.state = 65
                self.assignment()
                pass
            elif token in [switchParser.T__6]:
                self.state = 66
                self.access()
                pass
            elif token in [switchParser.COMPARISON_OPS]:
                self.state = 67
                self.comp()
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


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(switchParser.ExprContext,0)


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
        self.enterRule(localctx, 12, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(switchParser.T__3)
            self.state = 71
            self.expr()
            self.state = 72
            self.match(switchParser.ARG_DELIM)
            self.state = 73
            self.args()
            self.state = 74
            self.match(switchParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MATH_OPS_M(self):
            return self.getToken(switchParser.MATH_OPS_M, 0)

        def args(self):
            return self.getTypedRuleContext(switchParser.ArgsContext,0)


        def getRuleIndex(self):
            return switchParser.RULE_mult

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)




    def mult(self):

        localctx = switchParser.MultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mult)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(switchParser.MATH_OPS_M)
            self.state = 77
            self.args()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_sub_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MATH_OPS_A(self):
            return self.getToken(switchParser.MATH_OPS_A, 0)

        def args(self):
            return self.getTypedRuleContext(switchParser.ArgsContext,0)


        def getRuleIndex(self):
            return switchParser.RULE_add_sub_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_sub_expr" ):
                listener.enterAdd_sub_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_sub_expr" ):
                listener.exitAdd_sub_expr(self)




    def add_sub_expr(self):

        localctx = switchParser.Add_sub_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_add_sub_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(switchParser.MATH_OPS_A)
            self.state = 80
            self.args()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARG_DELIM(self):
            return self.getToken(switchParser.ARG_DELIM, 0)

        def expr(self):
            return self.getTypedRuleContext(switchParser.ExprContext,0)


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
            self.state = 82
            self.match(switchParser.T__5)
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [switchParser.NAME]:
                self.state = 83
                self.match(switchParser.NAME)
                pass
            elif token in [switchParser.T__6]:
                self.state = 84
                self.access()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 87
            self.match(switchParser.ARG_DELIM)
            self.state = 88
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(switchParser.ExprContext,0)


        def ARG_DELIM(self):
            return self.getToken(switchParser.ARG_DELIM, 0)

        def args(self):
            return self.getTypedRuleContext(switchParser.ArgsContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(switchParser.T__6)
            self.state = 91
            self.expr()
            self.state = 92
            self.match(switchParser.ARG_DELIM)
            self.state = 93
            self.args()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPARISON_OPS(self):
            return self.getToken(switchParser.COMPARISON_OPS, 0)

        def args(self):
            return self.getTypedRuleContext(switchParser.ArgsContext,0)


        def getRuleIndex(self):
            return switchParser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)




    def comp(self):

        localctx = switchParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(switchParser.COMPARISON_OPS)
            self.state = 96
            self.args()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):

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
        self.enterRule(localctx, 24, self.RULE_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.expr()
            self.state = 103
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 99
                    self.match(switchParser.ARG_DELIM)
                    self.state = 100
                    self.expr() 
                self.state = 105
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prim_exprContext(ParserRuleContext):

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
        self.enterRule(localctx, 26, self.RULE_prim_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << switchParser.STRING) | (1 << switchParser.INT) | (1 << switchParser.FLOAT) | (1 << switchParser.NAME))) != 0)):
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





