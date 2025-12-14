from antlr4 import CommonTokenStream, FileStream
from callgrind_policy_checker import check_policy_with_callgrind
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
    policy_path = "../../examples/e1.policy"
    binary_path = "./example_valgrind"

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
