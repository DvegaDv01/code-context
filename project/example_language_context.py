from core.code_context import CodeContext

def example_language_context():
    # Create an instance of the CodeContext
    code_context = CodeContext(language="Python")

    # Create language contexts for different programming languages
    python_context = code_context.create_language_context("Python")
    javascript_context = code_context.create_language_context("JavaScript")

    # Add code elements to specific language contexts
    python_context.add_variable("x", "int")
    python_context.add_function("main", "def main():")

    javascript_context.add_variable("count", "number")
    javascript_context.add_function("printCount", "function printCount():")

    # Print the language contexts
    print(code_context.serialize())

if __name__ == "__main__":
    example_language_context()
