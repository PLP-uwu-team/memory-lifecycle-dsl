# Generated from MemoryPolicy.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MemoryPolicyParser import MemoryPolicyParser
else:
    from MemoryPolicyParser import MemoryPolicyParser

# This class defines a complete generic visitor for a parse tree produced by MemoryPolicyParser.

class MemoryPolicyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MemoryPolicyParser#policy.
    def visitPolicy(self, ctx:MemoryPolicyParser.PolicyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemoryPolicyParser#allocateBlock.
    def visitAllocateBlock(self, ctx:MemoryPolicyParser.AllocateBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemoryPolicyParser#deallocateBlock.
    def visitDeallocateBlock(self, ctx:MemoryPolicyParser.DeallocateBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemoryPolicyParser#transferBlock.
    def visitTransferBlock(self, ctx:MemoryPolicyParser.TransferBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemoryPolicyParser#list.
    def visitList(self, ctx:MemoryPolicyParser.ListContext):
        return self.visitChildren(ctx)



del MemoryPolicyParser