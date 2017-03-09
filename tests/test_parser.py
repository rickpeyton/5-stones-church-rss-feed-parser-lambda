import unittest

from src.parser import *

class LambdaHanderTest(unittest.TestCase):

    def setUp(self):
        result = lambda_handler("", "")
        self.fixture = result

    def tearDown(self):
        del self.fixture

    def test_response_type(self):
        self.assertIsInstance(self.fixture, dict)

    def test_response_title_type(self):
        self.assertIsInstance(self.fixture["title"], str)

    def test_response_url_type(self):
        self.assertIsInstance(self.fixture["url"], str)

    def test_response_email_type(self):
        self.assertIsInstance(self.fixture["email"], str)

    def test_response_description_type(self):
        self.assertIsInstance(self.fixture["description"], str)

    def test_response_messages_type(self):
        self.assertIsInstance(self.fixture["messages"], list)

    def test_response_message_order_type(self):
        self.assertIsInstance(self.fixture["messages"][0]["order"], int)

    def test_response_message_title_type(self):
        self.assertIsInstance(self.fixture["messages"][0]["title"], str)

    def test_response_message_published_date_type(self):
        self.assertIsInstance(self.fixture["messages"][0]["published_date"], str)

    def test_response_message_date_type(self):
        self.assertIsInstance(self.fixture["messages"][0]["date"], str)

    def test_response_message_file_type(self):
        self.assertIsInstance(self.fixture["messages"][0]["file"], str)

    def test_response_message_length_type(self):
        self.assertIsInstance(self.fixture["messages"][0]["length"], str)

if __name__ == '__main__':
    unittest.main()