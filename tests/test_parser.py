import unittest

from src.parser import *

class LambdaHanderTest(unittest.TestCase):

    def setUp(self):
        result = lambda_handler("", "")
        self.fixture = result

    def tearDown(self):
        del self.fixture

    def test_response_type(self):
        self.assertIsInstance(self.fixture, str)

    def test_response_value(self):
        self.assertEqual(self.fixture, "Got Here")

if __name__ == '__main__':
    unittest.main()
