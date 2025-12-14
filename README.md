# Memory Lifecycle DSL

A domain-specific language (DSL) for **Static Memory Lifecycle Validation**. This DSL allows you to formally specify which functions in your codebase allocate, deallocate, and transfer ownership of heap memory. The goal is to enable static analysis tools to detect memory management errors, such as leaks, double frees, use-after-free, and invalid frees, by analyzing control flow paths without executing the code.

---

## Domain

This DSL models the validation of static memory lifecycles. It operates during the **implementation (coding)** and **verification** phases, helping developers and tools enforce policies that every pointer receiving heap allocation must be properly deallocated on all possible execution paths (including exceptions).

## Entities

- **HeapMemory**: Represents an unmanaged block of heap memory. Its state changes during execution.
- **MemoryPointer**: A concrete variable in code (e.g., `void* ptr`) that references `HeapMemory`. The analysis tool tracks these pointers.

### HeapMemory States

1. **UNALLOCATED**: Initial state.
2. **ALLOCATED**: After allocation function is called.
3. **FREED**: After deallocation function is called.

## DSL Syntax

The DSL uses a simple block structure to declare which functions perform allocation, deallocation, and ownership transfer:

```policy
track_memory {
  allocate_by: ["malloc", "calloc"]
  deallocate_by: ["free"]
  transfer_ownership: ["StorePointerInGlobalList"]
}
```

### Grammar

See [`grammar/MemoryPolicy.g4`](grammar/MemoryPolicy.g4) for the ANTLR grammar.

## Rules Enforced by the Tool

These rules are hardcoded in the analysis tool, not written in the DSL:

1. **Memory Leak**: If a pointer is `ALLOCATED` at end-of-scope without passing through a deallocation function, it's a violation.
2. **Double Free**: If a pointer already `FREED` is passed again to a deallocation function.
3. **Use After Free**: If a pointer already `FREED` is accessed (read/written).
4. **Invalid Free**: If a pointer in `UNALLOCATED` state is passed to a deallocation function.

## Example Policy

See [`examples/e1.policy`](examples/e1.policy):

```policy
track_memory {
  allocate_by: ["malloc", "calloc"]
  deallocate_by: ["free"]
  transfer_ownership: ["StorePointerInGlobalList"]
}
```

## Usage

### Loading a Policy

Use the provided Python loader to parse a policy file:

```python
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
    policy = load_policy("../../examples/x.policy")

    print("ALLOCATE:", policy.allocate)
    print("DEALLOCATE:", policy.deallocate)
    print("TRANSFER:", policy.transfer)
```

See [`src/python/run_example.py`](src/python/run_example.py) for a runnable example.

## Project Structure

- `grammar/MemoryPolicy.g4`: ANTLR grammar for the DSL.
- `src/python/policy_loader.py`: Python visitor to extract policy info.
- `src/python/run_example.py`: Example script to load and print a policy.
- `examples/`: Example policy files.
