from core.code_context import CodeContext

def example_directory_file_structure():
    # Create an instance of the CodeContext
    code_context = CodeContext(language="Python")

    # Create subdirectories and nested subdirectories
    src_dir = code_context.create_directory("src")
    utils_dir = code_context.create_directory("utils", parent_path="src")

    # Add files to specific directories
    main_file = code_context.create_file("main.py", parent_path="src")
    helper_file = code_context.create_file("helper.py", parent_path="src/utils")

    # Add code elements (variables, functions, classes) to files
    main_file.add_variable("x", "int")
    main_file.add_function("main", "def main():")
    main_file.add_class("MyClass", ["method1", "method2"])

    helper_file.add_variable("y", "float")
    helper_file.add_function("helper_func", "def helper_func():")
    helper_file.add_class("HelperClass", ["methodA", "methodB"])

    # Print the directory and file structure
    print(code_context.directories.to_json())

if __name__ == "__main__":
    example_directory_file_structure()
