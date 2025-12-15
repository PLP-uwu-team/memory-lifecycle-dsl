# error_handler.py

from antlr4.error.ErrorListener import ErrorListener


class DSLSyntaxError(Exception):
    """Raised when DSL has syntax errors."""

    pass


class DSLSemanticError(Exception):
    """Raised when DSL is syntactically valid but semantically invalid."""

    pass


class MemoryPolicyErrorListener(ErrorListener):
    """
    Custom ANTLR error listener for user-friendly DSL syntax errors.
    """

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise DSLSyntaxError(f"[Syntax Error] Line {line}, Column {column}: {msg}")


def validate_policy(policy):
    """
    Semantic validation of parsed MemoryPolicy.
    """

    errors = []

    # 1. Empty policy
    if not policy.allocate and not policy.deallocate and not policy.transfer:
        errors.append("Policy is empty. No memory rules defined.")

    # 2. Allocation without free or transfer
    if policy.allocate and not policy.deallocate and not policy.transfer:
        errors.append(
            "Allocation functions defined without deallocation or transfer ownership."
        )

    # 3. Function appears in multiple roles
    overlap = (
        set(policy.allocate) & set(policy.deallocate)
        | set(policy.allocate) & set(policy.transfer)
        | set(policy.deallocate) & set(policy.transfer)
    )

    if overlap:
        errors.append(
            f"Function(s) defined in multiple roles: {', '.join(sorted(overlap))}"
        )

    # 4. Duplicate entries (optional but nice)
    if len(policy.allocate) != len(set(policy.allocate)):
        errors.append("Duplicate function names in allocate_by.")

    if len(policy.deallocate) != len(set(policy.deallocate)):
        errors.append("Duplicate function names in deallocate_by.")

    if len(policy.transfer) != len(set(policy.transfer)):
        errors.append("Duplicate function names in transfer_ownership.")

    if errors:
        raise DSLSemanticError("[Semantic Error]\n- " + "\n- ".join(errors))
