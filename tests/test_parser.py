import unittest
import yaml
import os

from src.parser import *

def response_fixture():
    with open(os.path.join(os.path.dirname(__file__), "request_fixture.yml"), 'r') as f:
        return yaml.load(f.read())


class ResponseFixtureTest(unittest.TestCase):

    def setUp(self):
        self.fixture = response_fixture()

    def tearDown(self):
        del self.fixture

    def test_response_type(self):
        self.assertIsInstance(self.fixture, requests.models.Response)


class LambdaHandlerTest(unittest.TestCase):

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


class MessageTest(unittest.TestCase):

    def setUp(self):
        self.fixture = Message("")

    def tearDown(self):
        del self.fixture

    def test_response(self):
        self.assertEquals(self.fixture.order, 1)
        self.assertEquals(self.fixture.title, "Doors - Part 1")
        self.assertEquals(self.fixture.published_date, "Sun, 05 Mar 2017 20:15:44 +0000")
        self.assertEquals(self.fixture.date, "MAR 05, 2017")
        self.assertEquals(self.fixture.file, "http://traffic.libsyn.com/5stoneschurch/20170305_-_Doors_Part_1.mp3")
        self.assertEquals(self.fixture.length, "28:10")

    def test_as_dict(self):
        assertion = {
            "order": self.fixture.order,
            "title": self.fixture.title,
            "published_date": self.fixture.published_date,
            "date": self.fixture.date,
            "file": self.fixture.file,
            "length": self.fixture.length
        }
        self.assertEquals(self.fixture.as_dict(), assertion)


class MetaTest(unittest.TestCase):

    def setUp(self):
        self.fixture = Meta("")

    def tearDown(self):
        del self.fixture

    def test_response(self):
        self.assertEquals(self.fixture.title, "5 Stones Church  - Weekend Messages")
        self.assertEquals(self.fixture.url, "http://www.5stoneschurch.com")
        self.assertEquals(self.fixture.email, "media@5stoneschurch.com")
        self.assertEquals(self.fixture.description, "A life-giving church in Franklin, TN. Follow Jesus - Experience Freedom - Discover Purpose - Make a Difference. 10 AM - Freedom Intermediate School")


class ParseMessagesTest(unittest.TestCase):

    def setUp(self):
        result = parse_messages("")
        self.fixture = result

    def tearDown(self):
        del self.fixture

    def test_response(self):
        expectation = {
            "order": 1,
            "title": "Doors - Part 1",
            "published_date": "Sun, 05 Mar 2017 20:15:44 +0000",
            "date": "MAR 05, 2017",
            "file": "http://traffic.libsyn.com/5stoneschurch/20170305_-_Doors_Part_1.mp3",
            "length": "28:10"
        }
        self.assertEquals(self.fixture[0], expectation)
        self.assertIsInstance(self.fixture, list)


if __name__ == '__main__':
    unittest.main()