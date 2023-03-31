import json
from core.code_context import CodeContext
from core.issue_tracker import IssueTracker
from core.test_suite import TestSuite

def example_create_code_context():
    # Example 1: Create and manipulate a CodeContext instance
    code_context = CodeContext(language="Python")
    src_dir = code_context.create_directory("src")
    main_file = code_context.create_file("main.py", parent_path="src")
    main_file.add_variable("x", "int")
    main_file.add_function("main", "def main():")
    code_context.project_config.set_compiler_options("python3")
    code_context.version_control.create_branch("feature1")
    code_context.version_control.commit_changes("Initial commit")
    issue_tracker = IssueTracker()
    issue_tracker.create_issue("Bug fix", "Fixing a bug", "Bug")
    test_suite = TestSuite()
    test_suite.add_test("test_addition", [3, 4], [7])
    code_context.add_dependency("numpy", "1.21.0")
    print(code_context.project_config.to_json())

def example_deserialize_code_context():
    # Example 2: Deserialize an existing code context JSON and manipulate it
    code_context_json_str = """
    {
        "language": "Python",
        "directories": {
            "name": "src",
            "subdirectories": [],
            "files": [
                {
                    "name": "main.py",
                    "variables": [{"name": "x", "data_type": "int"}],
                    "functions": [{"name": "main", "signature": "def main():"}],
                    "classes": [{"name": "MyClass", "members": ["method1", "method2"]}]
                }
            ]
        },
        "project_config": {
            "compiler_options": "python3",
            "build_targets": "build",
            "settings": {}
        },
        "version_control": {
            "branches": [{"name": "main", "commits": [{"message": "Initial commit", "timestamp": 1648653552.0}]}],
            "current_branch": "main"
        },
        "dependencies": [{"library": "numpy", "version": "1.21.0"}]
    }
    """
    code_context_json_dict = json.loads(code_context_json_str)
    code_context = CodeContext.from_json(code_context_json_dict)
    language = code_context.language
    directories = code_context.directories
    project_config = code_context.project_config
    version_control = code_context.version_control
    dependencies = code_context.dependencies
    src_dir = directories.get_subdirectory("src")
    main_file = src_dir.files["main.py"]
    main_variables = main_file.variables
    main_functions = main_file.functions
    main_classes = main_file.classes
    print(project_config.to_json())
    code_context.add_dependency("pandas", "1.3.5")
    code_context.version_control.commit_changes("Update dependencies")
    print(dependencies.to_json())

def main():
    # Prompt the user to select the example they want to run
    print("Select an example to run:")
    print("1. Create and manipulate a CodeContext instance")
    print("2. Deserialize an existing code context JSON and manipulate it")
    
    # Get user input for example selection
    try:
        selection = int(input("Enter the example number (1 or 2): "))
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        return

    # Run the selected example
    if selection == 1:
        example_create_code_context()
    elif selection == 2:
        example_deserialize_code_context()
    else:
        print("Invalid selection. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
