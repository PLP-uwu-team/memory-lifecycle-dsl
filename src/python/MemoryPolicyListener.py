# Generated from MemoryPolicy.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MemoryPolicyParser import MemoryPolicyParser
else:
    from MemoryPolicyParser import MemoryPolicyParser

# This class defines a complete listener for a parse tree produced by MemoryPolicyParser.
class MemoryPolicyListener(ParseTreeListener):

    # Enter a parse tree produced by MemoryPolicyParser#policy.
    def enterPolicy(self, ctx:MemoryPolicyParser.PolicyContext):
        pass

    # Exit a parse tree produced by MemoryPolicyParser#policy.
    def exitPolicy(self, ctx:MemoryPolicyParser.PolicyContext):
        pass


    # Enter a parse tree produced by MemoryPolicyParser#allocateBlock.
    def enterAllocateBlock(self, ctx:MemoryPolicyParser.AllocateBlockContext):
        pass

    # Exit a parse tree produced by MemoryPolicyParser#allocateBlock.
    def exitAllocateBlock(self, ctx:MemoryPolicyParser.AllocateBlockContext):
        pass


    # Enter a parse tree produced by MemoryPolicyParser#deallocateBlock.
    def enterDeallocateBlock(self, ctx:MemoryPolicyParser.DeallocateBlockContext):
        pass

    # Exit a parse tree produced by MemoryPolicyParser#deallocateBlock.
    def exitDeallocateBlock(self, ctx:MemoryPolicyParser.DeallocateBlockContext):
        pass


    # Enter a parse tree produced by MemoryPolicyParser#transferBlock.
    def enterTransferBlock(self, ctx:MemoryPolicyParser.TransferBlockContext):
        pass

    # Exit a parse tree produced by MemoryPolicyParser#transferBlock.
    def exitTransferBlock(self, ctx:MemoryPolicyParser.TransferBlockContext):
        pass


    # Enter a parse tree produced by MemoryPolicyParser#list.
    def enterList(self, ctx:MemoryPolicyParser.ListContext):
        pass

    # Exit a parse tree produced by MemoryPolicyParser#list.
    def exitList(self, ctx:MemoryPolicyParser.ListContext):
        pass



del MemoryPolicyParser