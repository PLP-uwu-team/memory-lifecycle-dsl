from antlr4 import CommonTokenStream, FileStream
from MemoryPolicyLexer import MemoryPolicyLexer
from MemoryPolicyParser import MemoryPolicyParser
from policy_loader import PolicyLoader


def load_policy(path):
    input_stream = FileStream(path)
    lexer = MemoryPolicyLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MemoryPolicyParser(tokens)
    tree = parser.policy()

    loader = PolicyLoader()
    loader.visit(tree)
    return loader


if __name__ == "__main__":
    policy = load_policy("../../examples/e1.policy")

    print("ALLOCATE:", policy.allocate)
    print("DEALLOCATE:", policy.deallocate)
    print("TRANSFER:", policy.transfer)
