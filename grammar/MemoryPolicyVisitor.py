# Generated from ../../grammar/MemoryPolicy.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MemoryPolicyParser import MemoryPolicyParser
else:
    from MemoryPolicyParser import MemoryPolicyParser

# This class defines a complete generic visitor for a parse tree produced by MemoryPolicyParser.

class MemoryPolicyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MemoryPolicyParser#policy.
    def visitPolicy(self, ctx:MemoryPolicyParser.PolicyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemoryPolicyParser#policyRule.
    def visitPolicyRule(self, ctx:MemoryPolicyParser.PolicyRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemoryPolicyParser#pairRule.
    def visitPairRule(self, ctx:MemoryPolicyParser.PairRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemoryPolicyParser#transferRule.
    def visitTransferRule(self, ctx:MemoryPolicyParser.TransferRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MemoryPolicyParser#functionList.
    def visitFunctionList(self, ctx:MemoryPolicyParser.FunctionListContext):
        return self.visitChildren(ctx)



del MemoryPolicyParser