from antlr4 import CommonTokenStream, FileStream
from error_handler import (
    DSLSemanticError,
    DSLSyntaxError,
    MemoryPolicyErrorListener,
    validate_policy,
)
from MemoryPolicyLexer import MemoryPolicyLexer
from MemoryPolicyParser import MemoryPolicyParser
from policy_loader import PolicyLoader


def load_policy(path):
    try:
        input_stream = FileStream(path)
        lexer = MemoryPolicyLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = MemoryPolicyParser(tokens)

        # Pasang custom error handler
        parser.removeErrorListeners()
        parser.addErrorListener(MemoryPolicyErrorListener())

        tree = parser.policy()

        loader = PolicyLoader()
        loader.visit(tree)

        # Semantic validation
        validate_policy(loader)

        return loader

    except (DSLSyntaxError, DSLSemanticError) as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    policy = load_policy("../../examples/e1.policy")

    print("ALLOCATE:", policy.allocate)
    print("DEALLOCATE:", policy.deallocate)
    print("TRANSFER:", policy.transfer)
