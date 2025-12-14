# Generated from MemoryPolicy.g4 by ANTLR 4.13.2
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
        4,1,12,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,3,
        0,14,8,0,1,0,3,0,17,8,0,1,0,3,0,20,8,0,1,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,41,8,4,10,
        4,12,4,44,9,4,3,4,46,8,4,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,49,0,10,
        1,0,0,0,2,24,1,0,0,0,4,28,1,0,0,0,6,32,1,0,0,0,8,36,1,0,0,0,10,11,
        5,1,0,0,11,13,5,2,0,0,12,14,3,2,1,0,13,12,1,0,0,0,13,14,1,0,0,0,
        14,16,1,0,0,0,15,17,3,4,2,0,16,15,1,0,0,0,16,17,1,0,0,0,17,19,1,
        0,0,0,18,20,3,6,3,0,19,18,1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,
        22,5,3,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,25,5,4,0,0,25,26,5,5,0,
        0,26,27,3,8,4,0,27,3,1,0,0,0,28,29,5,6,0,0,29,30,5,5,0,0,30,31,3,
        8,4,0,31,5,1,0,0,0,32,33,5,7,0,0,33,34,5,5,0,0,34,35,3,8,4,0,35,
        7,1,0,0,0,36,45,5,8,0,0,37,42,5,11,0,0,38,39,5,9,0,0,39,41,5,11,
        0,0,40,38,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,46,
        1,0,0,0,44,42,1,0,0,0,45,37,1,0,0,0,45,46,1,0,0,0,46,47,1,0,0,0,
        47,48,5,10,0,0,48,9,1,0,0,0,5,13,16,19,42,45
    ]

class MemoryPolicyParser ( Parser ):

    grammarFileName = "MemoryPolicy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'track_memory'", "'{'", "'}'", "'allocate_by'", 
                     "':'", "'deallocate_by'", "'transfer_ownership'", "'['", 
                     "','", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STRING", "WS" ]

    RULE_policy = 0
    RULE_allocateBlock = 1
    RULE_deallocateBlock = 2
    RULE_transferBlock = 3
    RULE_list = 4

    ruleNames =  [ "policy", "allocateBlock", "deallocateBlock", "transferBlock", 
                   "list" ]

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
    STRING=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PolicyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MemoryPolicyParser.EOF, 0)

        def allocateBlock(self):
            return self.getTypedRuleContext(MemoryPolicyParser.AllocateBlockContext,0)


        def deallocateBlock(self):
            return self.getTypedRuleContext(MemoryPolicyParser.DeallocateBlockContext,0)


        def transferBlock(self):
            return self.getTypedRuleContext(MemoryPolicyParser.TransferBlockContext,0)


        def getRuleIndex(self):
            return MemoryPolicyParser.RULE_policy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolicy" ):
                listener.enterPolicy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolicy" ):
                listener.exitPolicy(self)

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
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 12
                self.allocateBlock()


            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 15
                self.deallocateBlock()


            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 18
                self.transferBlock()


            self.state = 21
            self.match(MemoryPolicyParser.T__2)
            self.state = 22
            self.match(MemoryPolicyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AllocateBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(MemoryPolicyParser.ListContext,0)


        def getRuleIndex(self):
            return MemoryPolicyParser.RULE_allocateBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllocateBlock" ):
                listener.enterAllocateBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllocateBlock" ):
                listener.exitAllocateBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllocateBlock" ):
                return visitor.visitAllocateBlock(self)
            else:
                return visitor.visitChildren(self)




    def allocateBlock(self):

        localctx = MemoryPolicyParser.AllocateBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_allocateBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(MemoryPolicyParser.T__3)
            self.state = 25
            self.match(MemoryPolicyParser.T__4)
            self.state = 26
            self.list_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeallocateBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(MemoryPolicyParser.ListContext,0)


        def getRuleIndex(self):
            return MemoryPolicyParser.RULE_deallocateBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeallocateBlock" ):
                listener.enterDeallocateBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeallocateBlock" ):
                listener.exitDeallocateBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeallocateBlock" ):
                return visitor.visitDeallocateBlock(self)
            else:
                return visitor.visitChildren(self)




    def deallocateBlock(self):

        localctx = MemoryPolicyParser.DeallocateBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_deallocateBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(MemoryPolicyParser.T__5)
            self.state = 29
            self.match(MemoryPolicyParser.T__4)
            self.state = 30
            self.list_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransferBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(MemoryPolicyParser.ListContext,0)


        def getRuleIndex(self):
            return MemoryPolicyParser.RULE_transferBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransferBlock" ):
                listener.enterTransferBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransferBlock" ):
                listener.exitTransferBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransferBlock" ):
                return visitor.visitTransferBlock(self)
            else:
                return visitor.visitChildren(self)




    def transferBlock(self):

        localctx = MemoryPolicyParser.TransferBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_transferBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(MemoryPolicyParser.T__6)
            self.state = 33
            self.match(MemoryPolicyParser.T__4)
            self.state = 34
            self.list_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
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
            return MemoryPolicyParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = MemoryPolicyParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(MemoryPolicyParser.T__7)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 37
                self.match(MemoryPolicyParser.STRING)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 38
                    self.match(MemoryPolicyParser.T__8)
                    self.state = 39
                    self.match(MemoryPolicyParser.STRING)
                    self.state = 44
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 47
            self.match(MemoryPolicyParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





