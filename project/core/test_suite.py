class TestSuite:
    def __init__(self):
        self.tests = []
        
    def add_test(self, test_name, inputs, expected_outputs):
        if not test_name or not inputs or not expected_outputs:
            return None  # Invalid input
        test = {"test_name": test_name, "inputs": inputs, "expected_outputs": expected_outputs}
        self.tests.append(test)
    
    def to_json(self):
        return self.tests

    @classmethod
    def from_json(cls, tests_json):
        test_suite = cls()
        test_suite.tests = tests_json
        return test_suite
