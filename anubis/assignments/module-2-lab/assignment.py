"""Anubis autograde tests for AINS6302 Module 2 (Attack-Path Modeling and Breach Forecasting).

This file runs inside the Anubis pipeline. Student code is in the
current working directory. Never run student code directly —
always go through ``exec_as_student``.
"""
from utils import (
    register_build,
    register_test,
    exec_as_student,
    BuildResult,
    TestResult,
    verify_expected,
)


@register_build
def build(build_result: BuildResult) -> None:
    """Python-only lab — nothing to compile."""
    build_result.stdout = "Skipped (pure Python)"
    build_result.passed = True


@register_test("notebook executes cleanly")
def test_notebook_runs(test_result: TestResult) -> None:
    stdout, code = exec_as_student(
        "jupyter nbconvert --to script "
        "notebooks/module-2-lab.ipynb --stdout | python -"
    )
    test_result.stdout = stdout
    test_result.passed = code == 0
    test_result.message = (
        "Notebook converted and executed without raising."
        if code == 0 else
        "Notebook raised on execution; see stdout."
    )


@register_test("baseline function is defined")
def test_baseline_defined(test_result: TestResult) -> None:
    stdout, code = exec_as_student(
        "python -c "
        "'import runpy, sys; "
        "ns = runpy.run_path(\"notebooks/module-2-lab.ipynb\"); "
        "sys.exit(0 if callable(ns.get(\"baseline\")) else 1)'"
    )
    test_result.stdout = stdout
    test_result.passed = code == 0
    test_result.message = "Expected a callable `baseline(x)`."


@register_test("improved function is defined")
def test_improved_defined(test_result: TestResult) -> None:
    stdout, code = exec_as_student(
        "python -c "
        "'import runpy, sys; "
        "ns = runpy.run_path(\"notebooks/module-2-lab.ipynb\"); "
        "sys.exit(0 if callable(ns.get(\"improved\")) else 1)'"
    )
    test_result.stdout = stdout
    test_result.passed = code == 0
    test_result.message = "Expected a callable `improved(x)`."


# Additional module-specific tests should be added here during
# course development. Use verify_expected / search_lines from
# utils for output-style tests.
