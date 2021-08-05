# Generated from Json.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("`\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17")
        buf.write("\3\20\3\20\3\21\6\21Q\n\21\r\21\16\21R\3\22\6\22V\n\22")
        buf.write("\r\22\16\22W\3\23\6\23[\n\23\r\23\16\23\\\3\23\3\23\2")
        buf.write("\2\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\3\2\5\4\2C\\c|")
        buf.write("\3\2\62;\5\2\13\f\17\17\"\"\2b\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5)\3")
        buf.write("\2\2\2\7+\3\2\2\2\t-\3\2\2\2\13/\3\2\2\2\r\61\3\2\2\2")
        buf.write("\17\63\3\2\2\2\21\65\3\2\2\2\23\67\3\2\2\2\25<\3\2\2\2")
        buf.write("\27B\3\2\2\2\31G\3\2\2\2\33I\3\2\2\2\35K\3\2\2\2\37M\3")
        buf.write("\2\2\2!P\3\2\2\2#U\3\2\2\2%Z\3\2\2\2\'(\7.\2\2(\4\3\2")
        buf.write("\2\2)*\7}\2\2*\6\3\2\2\2+,\7\177\2\2,\b\3\2\2\2-.\7$\2")
        buf.write("\2.\n\3\2\2\2/\60\7<\2\2\60\f\3\2\2\2\61\62\7-\2\2\62")
        buf.write("\16\3\2\2\2\63\64\7]\2\2\64\20\3\2\2\2\65\66\7_\2\2\66")
        buf.write("\22\3\2\2\2\678\7v\2\289\7t\2\29:\7w\2\2:;\7g\2\2;\24")
        buf.write("\3\2\2\2<=\7h\2\2=>\7c\2\2>?\7n\2\2?@\7u\2\2@A\7g\2\2")
        buf.write("A\26\3\2\2\2BC\7p\2\2CD\7w\2\2DE\7n\2\2EF\7n\2\2F\30\3")
        buf.write("\2\2\2GH\7*\2\2H\32\3\2\2\2IJ\7+\2\2J\34\3\2\2\2KL\7&")
        buf.write("\2\2L\36\3\2\2\2MN\7\60\2\2N \3\2\2\2OQ\t\2\2\2PO\3\2")
        buf.write("\2\2QR\3\2\2\2RP\3\2\2\2RS\3\2\2\2S\"\3\2\2\2TV\t\3\2")
        buf.write("\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2X$\3\2\2\2Y")
        buf.write("[\t\4\2\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]")
        buf.write("^\3\2\2\2^_\b\23\2\2_&\3\2\2\2\6\2RW\\\3\b\2\2")
        return buf.getvalue()


class JsonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    STRING = 16
    NUMBER = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'{'", "'}'", "'\"'", "':'", "'+'", "'['", "']'", "'true'", 
            "'false'", "'null'", "'('", "')'", "'$'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "STRING", "NUMBER", "WS" ]

    grammarFileName = "Json.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


