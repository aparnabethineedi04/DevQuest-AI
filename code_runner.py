
import ast
import os
import subprocess
import sys
import tempfile
from pathlib import Path


def run_python_tests(code, test_cases, timeout=3):
    """
    Run a Python solution against test cases.

    Each test case must contain:
      - input: text passed to stdin
      - expected: expected stdout text

    This is a local learning/demo runner, not a secure sandbox.
    Do not use it to execute untrusted code on a public server.
    """
    if not isinstance(code, str) or not code.strip():
        return {
            "passed": 0,
            "total": len(test_cases),
            "results": [],
            "error": "Please enter a Python solution.",
        }

    try:
        # Reject obvious syntax errors before launching the process.
        ast.parse(code)
    except SyntaxError as exc:
        return {
            "passed": 0,
            "total": len(test_cases),
            "results": [],
            "error": f"Syntax error on line {exc.lineno}: {exc.msg}",
        }

    results = []
    passed = 0

    with tempfile.TemporaryDirectory(prefix="devquest_") as temp_dir:
        script_path = Path(temp_dir) / "solution.py"
        script_path.write_text(code, encoding="utf-8")

        for index, case in enumerate(test_cases, start=1):
            try:
                process = subprocess.run(
                    [sys.executable, "-I", str(script_path)],
                    input=str(case.get("input", "")),
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    cwd=temp_dir,
                    env={
                        "PATH": os.environ.get("PATH", ""),
                        "PYTHONIOENCODING": "utf-8",
                    },
                    check=False,
                )

                actual = process.stdout.strip()
                expected = str(case.get("expected", "")).strip()

                if process.returncode != 0:
                    results.append({
                        "test": index,
                        "passed": False,
                        "expected": expected,
                        "actual": actual,
                        "error": process.stderr.strip() or
                                 f"Process exited with code {process.returncode}.",
                    })
                else:
                    is_passed = actual == expected
                    passed += int(is_passed)
                    results.append({
                        "test": index,
                        "passed": is_passed,
                        "expected": expected,
                        "actual": actual,
                        "error": "",
                    })

            except subprocess.TimeoutExpired:
                results.append({
                    "test": index,
                    "passed": False,
                    "expected": str(case.get("expected", "")).strip(),
                    "actual": "",
                    "error": f"Timed out after {timeout} seconds.",
                })

    return {
        "passed": passed,
        "total": len(test_cases),
        "results": results,
        "error": "",
    }
