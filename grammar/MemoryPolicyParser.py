# Generated from ../../grammar/MemoryPolicy.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("\67\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3")
        buf.write("\2\7\2\20\n\2\f\2\16\2\23\13\2\3\2\3\2\3\2\3\3\3\3\5\3")
        buf.write("\32\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6.\n\6\f\6\16\6\61\13\6\5")
        buf.write("\6\63\n\6\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\2\2\65\2\f\3\2")
        buf.write("\2\2\4\31\3\2\2\2\6\33\3\2\2\2\b%\3\2\2\2\n)\3\2\2\2\f")
        buf.write("\r\7\3\2\2\r\21\7\4\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20")
        buf.write("\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\24\3\2\2\2")
        buf.write("\23\21\3\2\2\2\24\25\7\5\2\2\25\26\7\2\2\3\26\3\3\2\2")
        buf.write("\2\27\32\5\6\4\2\30\32\5\b\5\2\31\27\3\2\2\2\31\30\3\2")
        buf.write("\2\2\32\5\3\2\2\2\33\34\7\6\2\2\34\35\7\4\2\2\35\36\7")
        buf.write("\7\2\2\36\37\7\b\2\2\37 \7\16\2\2 !\7\t\2\2!\"\7\b\2\2")
        buf.write("\"#\7\16\2\2#$\7\5\2\2$\7\3\2\2\2%&\7\n\2\2&\'\7\b\2\2")
        buf.write("\'(\5\n\6\2(\t\3\2\2\2)\62\7\13\2\2*/\7\16\2\2+,\7\f\2")
        buf.write("\2,.\7\16\2\2-+\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2")
        buf.write("\2\2\60\63\3\2\2\2\61/\3\2\2\2\62*\3\2\2\2\62\63\3\2\2")
        buf.write("\2\63\64\3\2\2\2\64\65\7\r\2\2\65\13\3\2\2\2\6\21\31/")
        buf.write("\62")
        return buf.getvalue()


class MemoryPolicyParser ( Parser ):

    grammarFileName = "MemoryPolicy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'track_memory'", "'{'", "'}'", "'pair'", 
                     "'allocator'", "':'", "'deallocator'", "'transfer_ownership'", 
                     "'['", "','", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "STRING", "COMMENT", "WS" ]

    RULE_policy = 0
    RULE_policyRule = 1
    RULE_pairRule = 2
    RULE_transferRule = 3
    RULE_functionList = 4

    ruleNames =  [ "policy", "policyRule", "pairRule", "transferRule", "functionList" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    STRING=12
    COMMENT=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PolicyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MemoryPolicyParser.EOF, 0)

        def policyRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MemoryPolicyParser.PolicyRuleContext)
            else:
                return self.getTypedRuleContext(MemoryPolicyParser.PolicyRuleContext,i)


        def getRuleIndex(self):
            return MemoryPolicyParser.RULE_policy

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolicy" ):
                return visitor.visitPolicy(self)
            else:
                return visitor.visitChildren(self)




    def policy(self):

        localctx = MemoryPolicyParser.PolicyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_policy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(MemoryPolicyParser.T__0)
            self.state = 11
            self.match(MemoryPolicyParser.T__1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MemoryPolicyParser.T__3 or _la==MemoryPolicyParser.T__7:
                self.state = 12
                self.policyRule()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(MemoryPolicyParser.T__2)
            self.state = 19
            self.match(MemoryPolicyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PolicyRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pairRule(self):
            return self.getTypedRuleContext(MemoryPolicyParser.PairRuleContext,0)


        def transferRule(self):
            return self.getTypedRuleContext(MemoryPolicyParser.TransferRuleContext,0)


        def getRuleIndex(self):
            return MemoryPolicyParser.RULE_policyRule

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolicyRule" ):
                return visitor.visitPolicyRule(self)
            else:
                return visitor.visitChildren(self)




    def policyRule(self):

        localctx = MemoryPolicyParser.PolicyRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_policyRule)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MemoryPolicyParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.pairRule()
                pass
            elif token in [MemoryPolicyParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.transferRule()
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


    class PairRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.allocator = None # Token
            self.deallocator = None # Token

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MemoryPolicyParser.STRING)
            else:
                return self.getToken(MemoryPolicyParser.STRING, i)

        def getRuleIndex(self):
            return MemoryPolicyParser.RULE_pairRule

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPairRule" ):
                return visitor.visitPairRule(self)
            else:
                return visitor.visitChildren(self)




    def pairRule(self):

        localctx = MemoryPolicyParser.PairRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pairRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(MemoryPolicyParser.T__3)
            self.state = 26
            self.match(MemoryPolicyParser.T__1)
            self.state = 27
            self.match(MemoryPolicyParser.T__4)
            self.state = 28
            self.match(MemoryPolicyParser.T__5)
            self.state = 29
            localctx.allocator = self.match(MemoryPolicyParser.STRING)
            self.state = 30
            self.match(MemoryPolicyParser.T__6)
            self.state = 31
            self.match(MemoryPolicyParser.T__5)
            self.state = 32
            localctx.deallocator = self.match(MemoryPolicyParser.STRING)
            self.state = 33
            self.match(MemoryPolicyParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransferRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionList(self):
            return self.getTypedRuleContext(MemoryPolicyParser.FunctionListContext,0)


        def getRuleIndex(self):
            return MemoryPolicyParser.RULE_transferRule

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransferRule" ):
                return visitor.visitTransferRule(self)
            else:
                return visitor.visitChildren(self)




    def transferRule(self):

        localctx = MemoryPolicyParser.TransferRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_transferRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(MemoryPolicyParser.T__7)
            self.state = 36
            self.match(MemoryPolicyParser.T__5)
            self.state = 37
            self.functionList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MemoryPolicyParser.STRING)
            else:
                return self.getToken(MemoryPolicyParser.STRING, i)

        def getRuleIndex(self):
            return MemoryPolicyParser.RULE_functionList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionList" ):
                return visitor.visitFunctionList(self)
            else:
                return visitor.visitChildren(self)




    def functionList(self):

        localctx = MemoryPolicyParser.FunctionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(MemoryPolicyParser.T__8)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MemoryPolicyParser.STRING:
                self.state = 40
                self.match(MemoryPolicyParser.STRING)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MemoryPolicyParser.T__9:
                    self.state = 41
                    self.match(MemoryPolicyParser.T__9)
                    self.state = 42
                    self.match(MemoryPolicyParser.STRING)
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 50
            self.match(MemoryPolicyParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





