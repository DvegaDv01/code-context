import json
from core.code_context import CodeContext

def example_serialization_deserialization():
    # Create and manipulate a CodeContext instance
    code_context = CodeContext(language="Python")
    src_dir = code_context.create_directory("src")
    main_file = code_context.create_file("main.py", parent_path="src")
    main_file.add_variable("x", "int")
    main_file.add_function("main", "def main():")
    code_context.add_dependency("numpy", "1.21.0")

    # Serialize the code context to JSON format
    serialized_context = code_context.to_json()

    # Deserialize JSON to reconstruct the code context
    deserialized_context = CodeContext.from_json(serialized_context)

    # Print the deserialized code context
    print(json.dumps(deserialized_context.to_json(), indent=2))

if __name__ == "__main__":
    example_serialization_deserialization()
