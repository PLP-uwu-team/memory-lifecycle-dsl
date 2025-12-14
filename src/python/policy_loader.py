from MemoryPolicyParser import MemoryPolicyParser
from MemoryPolicyVisitor import MemoryPolicyVisitor

class PolicyLoader(MemoryPolicyVisitor):
    def __init__(self):
        self.pairs = {}       
        self.transfer = []

    def visitPolicy(self, ctx):
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))

    def visitPairRule(self, ctx):
        if ctx.allocator and ctx.deallocator:
            alloc_name = ctx.allocator.text.strip('"')
            dealloc_name = ctx.deallocator.text.strip('"')
            self.pairs[alloc_name] = dealloc_name

    def visitTransferRule(self, ctx):
        # PERUBAHAN DI SINI:
        # Dulu ctx.list(), sekarang ctx.functionList()
        if ctx.functionList():
            raw_text = ctx.functionList().getText()
            content = raw_text.strip("[]")
            if content:
                clean_list = [s.strip().strip('"') for s in content.split(',')]
                self.transfer = clean_list