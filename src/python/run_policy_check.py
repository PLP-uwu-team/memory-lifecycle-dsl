from antlr4 import CommonTokenStream, FileStream
from callgrind_policy_checker import check_policy_with_callgrind
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
    policy_path = "../../examples/e2.policy"
    binary_path = "./test2"

    policy = load_policy(policy_path)

    print("=== POLICY ===")
    print("ALLOCATE:", policy.allocate)
    print("DEALLOCATE:", policy.deallocate)
    print("TRANSFER:", policy.transfer)

    print("\n=== CALLGRIND CHECK ===")
    results = check_policy_with_callgrind(binary_path, policy)

    for r in results:
        icon = {
            "OK": "[OK]",
            "WARNING": "[WARN]",
            "ERROR": "[ERR]",
        }[r["severity"]]

        print(f"{icon} {r['function']}: {r['status']}")
