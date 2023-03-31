from core.dependencies import Dependencies

def example_dependencies():
    # Create an instance of the Dependencies
    dependencies = Dependencies()

    # Add new dependencies
    dependencies.add_dependency("numpy", "1.21.0")
    dependencies.add_dependency("pandas", "1.3.5")

    # Print the dependencies
    print(dependencies.to_json())

    # Note: Demonstrating how dependency information might be used for installation is outside the scope of this example.

if __name__ == "__main__":
    example_dependencies()
