"""Minimal, restricted Code as Action demonstration."""

from __future__ import annotations

import ast
from typing import Any, Dict


OPEN_TAG = "<execute_python>"
CLOSE_TAG = "</execute_python>"
SAFE_BUILTINS = {"len": len, "max": max, "min": min, "sum": sum, "sorted": sorted}
FORBIDDEN_NODES = (ast.Import, ast.ImportFrom, ast.With, ast.Try, ast.ClassDef, ast.FunctionDef)
FORBIDDEN_NAMES = {"open", "eval", "exec", "compile", "__import__", "globals", "locals"}


def extract_code(model_output: str) -> str:
    """Extract exactly one tagged code block."""
    if model_output.count(OPEN_TAG) != 1 or model_output.count(CLOSE_TAG) != 1:
        raise ValueError("Expected exactly one execute_python block")
    start = model_output.index(OPEN_TAG) + len(OPEN_TAG)
    end = model_output.index(CLOSE_TAG)
    if end < start:
        raise ValueError("Closing tag appears before opening tag")
    return model_output[start:end].strip()


def validate_code(code: str) -> None:
    """Reject a small set of clearly unsafe operations before execution."""
    tree = ast.parse(code, mode="exec")
    for node in ast.walk(tree):
        if isinstance(node, FORBIDDEN_NODES):
            raise ValueError(f"Forbidden syntax: {type(node).__name__}")
        if isinstance(node, ast.Name) and node.id in FORBIDDEN_NAMES:
            raise ValueError(f"Forbidden name: {node.id}")
        if isinstance(node, ast.Attribute) and node.attr.startswith("__"):
            raise ValueError("Dunder attribute access is not allowed")


def execute_model_output(model_output: str) -> Dict[str, Any]:
    """Extract, validate, and run a tagged program in a restricted namespace."""
    try:
        code = extract_code(model_output)
        validate_code(code)
        namespace: Dict[str, Any] = {"__builtins__": SAFE_BUILTINS}
        exec(code, namespace, namespace)
        return {"status": "success", "result": namespace.get("answer")}
    except (SyntaxError, ValueError, RuntimeError, TypeError, NameError) as exc:
        return {"status": "error", "error_type": type(exc).__name__, "message": str(exc)}
