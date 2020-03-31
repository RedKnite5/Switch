# Generated from switch.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("U\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\7\7\62\n\7\f\7")
        buf.write("\16\7\65\13\7\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\6\16G\n\16\r\16\16\16H\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\21\6\21R\n\21\r\21\16\21S")
        buf.write("\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\2\23\2\25\n\27")
        buf.write("\13\31\f\33\r\35\16\37\2!\17\3\2\t\5\2\13\f\17\17\"\"")
        buf.write("\4\2QQqq\4\2\\\\||\3\2vx\4\2oorr\5\2iinnss\6\2#\61<B]")
        buf.write("b}\u0080\2U\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2!\3\2\2\2\3#\3\2\2\2\5%\3\2\2\2\7\'\3\2\2\2\t)\3\2")
        buf.write("\2\2\13+\3\2\2\2\r-\3\2\2\2\17\66\3\2\2\2\21:\3\2\2\2")
        buf.write("\23<\3\2\2\2\25>\3\2\2\2\27@\3\2\2\2\31B\3\2\2\2\33F\3")
        buf.write("\2\2\2\35J\3\2\2\2\37N\3\2\2\2!Q\3\2\2\2#$\7e\2\2$\4\3")
        buf.write("\2\2\2%&\7p\2\2&\6\3\2\2\2\'(\7n\2\2(\b\3\2\2\2)*\7g\2")
        buf.write("\2*\n\3\2\2\2+,\7k\2\2,\f\3\2\2\2-.\7U\2\2.\63\5\33\16")
        buf.write("\2/\60\7u\2\2\60\62\5\33\16\2\61/\3\2\2\2\62\65\3\2\2")
        buf.write("\2\63\61\3\2\2\2\63\64\3\2\2\2\64\16\3\2\2\2\65\63\3\2")
        buf.write("\2\2\66\67\t\2\2\2\678\3\2\2\289\b\b\2\29\20\3\2\2\2:")
        buf.write(";\t\3\2\2;\22\3\2\2\2<=\t\4\2\2=\24\3\2\2\2>?\t\5\2\2")
        buf.write("?\26\3\2\2\2@A\t\6\2\2A\30\3\2\2\2BC\t\7\2\2C\32\3\2\2")
        buf.write("\2DG\5\21\t\2EG\5\23\n\2FD\3\2\2\2FE\3\2\2\2GH\3\2\2\2")
        buf.write("HF\3\2\2\2HI\3\2\2\2I\34\3\2\2\2JK\5\33\16\2KL\7f\2\2")
        buf.write("LM\5\33\16\2M\36\3\2\2\2NO\t\b\2\2O \3\2\2\2PR\5\37\20")
        buf.write("\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\"\3\2\2\2")
        buf.write("\7\2\63FHS\3\b\2\2")
        return buf.getvalue()


class switchLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    STRING = 6
    WHITESPACE = 7
    MATH_OPS_M = 8
    MATH_OPS_A = 9
    COMPARISON_OPS = 10
    INT = 11
    FLOAT = 12
    NAME = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'c'", "'n'", "'l'", "'e'", "'i'" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "WHITESPACE", "MATH_OPS_M", "MATH_OPS_A", "COMPARISON_OPS", 
            "INT", "FLOAT", "NAME" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "STRING", "WHITESPACE", 
                  "ONE", "ZERO", "MATH_OPS_M", "MATH_OPS_A", "COMPARISON_OPS", 
                  "INT", "FLOAT", "CHAR", "NAME" ]

    grammarFileName = "switch.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


