from core.test_suite import TestSuite

def example_test_suite():
    # Create an instance of the TestSuite
    test_suite = TestSuite()

    # Add new tests to the test suite
    test_suite.add_test("test_addition", [3, 4], [7])
    test_suite.add_test("test_subtraction", [10, 5], [5])

    # Print the tests
    print(test_suite.to_json())

    # Note: Implementing a test runner to run the tests is outside the scope of this example.

if __name__ == "__main__":
    example_test_suite()
