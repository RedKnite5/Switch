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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("B\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\34")
        buf.write("\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\5\6-\n\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\7\t;\n\t\f\t\16\t>\13\t\3\n\3\n\3\n\2\2")
        buf.write("\13\2\4\6\b\n\f\16\20\22\2\3\4\2\b\b\r\17\2@\2\33\3\2")
        buf.write("\2\2\4\35\3\2\2\2\6#\3\2\2\2\b&\3\2\2\2\n)\3\2\2\2\f\61")
        buf.write("\3\2\2\2\16\64\3\2\2\2\20\67\3\2\2\2\22?\3\2\2\2\24\34")
        buf.write("\5\22\n\2\25\34\5\4\3\2\26\34\5\6\4\2\27\34\5\b\5\2\30")
        buf.write("\34\5\n\6\2\31\34\5\f\7\2\32\34\5\16\b\2\33\24\3\2\2\2")
        buf.write("\33\25\3\2\2\2\33\26\3\2\2\2\33\27\3\2\2\2\33\30\3\2\2")
        buf.write("\2\33\31\3\2\2\2\33\32\3\2\2\2\34\3\3\2\2\2\35\36\7\3")
        buf.write("\2\2\36\37\5\2\2\2\37 \7\4\2\2 !\5\20\t\2!\"\7\5\2\2\"")
        buf.write("\5\3\2\2\2#$\7\n\2\2$%\5\20\t\2%\7\3\2\2\2&\'\7\13\2\2")
        buf.write("\'(\5\20\t\2(\t\3\2\2\2),\7\6\2\2*-\7\17\2\2+-\5\f\7\2")
        buf.write(",*\3\2\2\2,+\3\2\2\2-.\3\2\2\2./\7\4\2\2/\60\5\2\2\2\60")
        buf.write("\13\3\2\2\2\61\62\7\7\2\2\62\63\5\20\t\2\63\r\3\2\2\2")
        buf.write("\64\65\7\f\2\2\65\66\5\20\t\2\66\17\3\2\2\2\67<\5\2\2")
        buf.write("\289\7\4\2\29;\5\2\2\2:8\3\2\2\2;>\3\2\2\2<:\3\2\2\2<")
        buf.write("=\3\2\2\2=\21\3\2\2\2><\3\2\2\2?@\t\2\2\2@\23\3\2\2\2")
        buf.write("\5\33,<")
        return buf.getvalue()


class switchParser ( Parser ):

    grammarFileName = "switch.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'c'", "'n'", "'l'", "'e'", "'i'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "WHITESPACE", 
                      "MATH_OPS_M", "MATH_OPS_A", "COMPARISON_OPS", "INT", 
                      "FLOAT", "NAME" ]

    RULE_expr = 0
    RULE_call = 1
    RULE_m_expr = 2
    RULE_add_sub_expr = 3
    RULE_assignment = 4
    RULE_access = 5
    RULE_comp = 6
    RULE_args = 7
    RULE_prim_expr = 8

    ruleNames =  [ "expr", "call", "m_expr", "add_sub_expr", "assignment", 
                   "access", "comp", "args", "prim_expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    STRING=6
    WHITESPACE=7
    MATH_OPS_M=8
    MATH_OPS_A=9
    COMPARISON_OPS=10
    INT=11
    FLOAT=12
    NAME=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_expr(self):
            return self.getTypedRuleContext(switchParser.Prim_exprContext,0)


        def call(self):
            return self.getTypedRuleContext(switchParser.CallContext,0)


        def m_expr(self):
            return self.getTypedRuleContext(switchParser.M_exprContext,0)


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
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [switchParser.STRING, switchParser.INT, switchParser.FLOAT, switchParser.NAME]:
                self.state = 18
                self.prim_expr()
                pass
            elif token in [switchParser.T__0]:
                self.state = 19
                self.call()
                pass
            elif token in [switchParser.MATH_OPS_M]:
                self.state = 20
                self.m_expr()
                pass
            elif token in [switchParser.MATH_OPS_A]:
                self.state = 21
                self.add_sub_expr()
                pass
            elif token in [switchParser.T__3]:
                self.state = 22
                self.assignment()
                pass
            elif token in [switchParser.T__4]:
                self.state = 23
                self.access()
                pass
            elif token in [switchParser.COMPARISON_OPS]:
                self.state = 24
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
        self.enterRule(localctx, 2, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(switchParser.T__0)
            self.state = 28
            self.expr()
            self.state = 29
            self.match(switchParser.T__1)
            self.state = 30
            self.args()
            self.state = 31
            self.match(switchParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class M_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MATH_OPS_M(self):
            return self.getToken(switchParser.MATH_OPS_M, 0)

        def args(self):
            return self.getTypedRuleContext(switchParser.ArgsContext,0)


        def getRuleIndex(self):
            return switchParser.RULE_m_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterM_expr" ):
                listener.enterM_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitM_expr" ):
                listener.exitM_expr(self)




    def m_expr(self):

        localctx = switchParser.M_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_m_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(switchParser.MATH_OPS_M)
            self.state = 34
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
        self.enterRule(localctx, 6, self.RULE_add_sub_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(switchParser.MATH_OPS_A)
            self.state = 37
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
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(switchParser.T__3)
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [switchParser.NAME]:
                self.state = 40
                self.match(switchParser.NAME)
                pass
            elif token in [switchParser.T__4]:
                self.state = 41
                self.access()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 44
            self.match(switchParser.T__1)
            self.state = 45
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
        self.enterRule(localctx, 10, self.RULE_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(switchParser.T__4)
            self.state = 48
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
        self.enterRule(localctx, 12, self.RULE_comp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(switchParser.COMPARISON_OPS)
            self.state = 51
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
        self.enterRule(localctx, 14, self.RULE_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.expr()
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 54
                    self.match(switchParser.T__1)
                    self.state = 55
                    self.expr() 
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_prim_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
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





