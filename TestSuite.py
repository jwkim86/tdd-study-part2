class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self):
        results = TestResult()
        for test in self.tests:
            test.run(result)
        return results