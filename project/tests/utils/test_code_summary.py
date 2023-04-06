def test_code_summary():
    # Import relevant classes
    from project.core.code_context import CodeContext
    from project.utils.code_summary import CodeSummary
    
    # Test: Create CodeSummary instance
    code_summary = CodeSummary()
    assert isinstance(code_summary, CodeSummary)
    
    # Test: Add and remove variables, functions, and classes
    code_summary.add_variable("x", "int", "Python")
    code_summary.add_function("foo", "int foo()", "Python")
    code_summary.add_class("Bar", ["x", "y"], "Python")
    assert "x" in code_summary.summary["variables"]
    assert "foo" in code_summary.summary["functions"]
    assert "Bar" in code_summary.summary["classes"]
    code_summary.remove_variable("x")
    code_summary.remove_function("foo")
    code_summary.remove_class("Bar")
    assert "x" not in code_summary.summary["variables"]
    assert "foo" not in code_summary.summary["functions"]
    assert "Bar" not in code_summary.summary["classes"]
    
    # Test: Update code context
    code_context = CodeContext(language="Python")
    code_summary.add_variable("x", "int", "Python")
    code_summary.add_function("foo", "int foo()", "Python")
    code_summary.add_class("Bar", ["x", "y"], "Python")
    code_summary.update_code_context(code_context)
    lang_context = code_context.get_language_context("Python")
    assert lang_context.get_variable("x") == {"data_type": "int"}
    assert lang_context.get_function("foo") == {"signature": "int foo()"}
    assert lang_context.get_class("Bar") == {"members": ["x", "y"]}
