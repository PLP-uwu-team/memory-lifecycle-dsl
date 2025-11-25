from antlr4 import *
from MemoryPolicyLexer import MemoryPolicyLexer
from MemoryPolicyParser import MemoryPolicyParser
from MemoryPolicyVisitor import MemoryPolicyVisitor


class PolicyLoader(MemoryPolicyVisitor):
    def __init__(self):
        self.allocate = []
        self.deallocate = []
        self.transfer = []

    def visitAllocateBlock(self, ctx):
        self.allocate = [s.getText().strip('"') for s in ctx.list().STRING()]

    def visitDeallocateBlock(self, ctx):
        self.deallocate = [s.getText().strip('"') for s in ctx.list().STRING()]

    def visitTransferBlock(self, ctx):
        self.transfer = [s.getText().strip('"') for s in ctx.list().STRING()]
