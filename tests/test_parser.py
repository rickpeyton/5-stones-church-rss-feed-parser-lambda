import unittest
import yaml
import os

from src.parser import *

def response_fixture():
    with open(os.path.join(os.path.dirname(__file__), "request_fixture_20171113.yml"), 'r') as f:
        return yaml.load(f.read())


def parsed_fixture():
    response = response_fixture()
    response = BeautifulSoup(response.text, 'lxml-xml')
    return response

class FullRun(unittest.TestCase):

    def setUp(self):
        if True == False:
            lambda_handler("", "")

    def test_response_type(self):
        self.assertEquals(1, 1)


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

    def test_response_message_file_type(self):
        self.assertIsInstance(self.fixture["messages"][0]["image"], str)

class MessageTest(unittest.TestCase):

    def setUp(self):
        message = parsed_fixture().findAll("item")[0]
        counter = 1
        self.fixture = Message(message, 1)

    def tearDown(self):
        del self.fixture

    def test_response(self):
        self.assertEquals(self.fixture.order, 1)
        self.assertEquals(self.fixture.title, "Philippians - Part 4")
        self.assertEquals(self.fixture.published_date, "Sun, 12 Nov 2017 18:39:03 +0000")
        self.assertEquals(self.fixture.date, "Nov 12, 2017")
        self.assertEquals(self.fixture.file, "http://traffic.libsyn.com/5stoneschurch/20171112_-_Philippians_-_Part_4.mp3")
        self.assertEquals(self.fixture.image, "http://static.libsyn.com/p/assets/5/3/1/1/5311ea82ffe57b25/philippians-1x1.jpg")

    def test_as_dict(self):
        assertion = {
            "order": self.fixture.order,
            "title": self.fixture.title,
            "published_date": self.fixture.published_date,
            "date": self.fixture.date,
            "file": self.fixture.file,
            "image": self.fixture.image
        }
        self.assertEquals(self.fixture.as_dict(), assertion)


class UrlToDateTest(unittest.TestCase):
    def setUp(self):
        url = "http://traffic.libsyn.com/5stoneschurch/20170305_-_Doors_Part_1.mp3"
        self.fixture = UrlToDate(url).date()

    def tearDown(self):
        del self.fixture

    def test_conversion(self):
        self.assertEquals(self.fixture, "Mar 05, 2017")


class MetaTest(unittest.TestCase):

    def setUp(self):
        self.fixture = Meta(parsed_fixture())

    def tearDown(self):
        del self.fixture

    def test_response(self):
        print(dir(self.fixture))
        self.assertEquals(self.fixture.title, "5 Stones Church  - Weekend Messages")
        self.assertEquals(self.fixture.url, "http://www.5stoneschurch.com")
        self.assertEquals(self.fixture.description, "A life-giving church in Franklin, TN. Follow Jesus - Experience Freedom - Discover Purpose - Make a Difference. 10 AM - Freedom Intermediate School")


class ParseMessagesTest(unittest.TestCase):

    def setUp(self):
        result = parse_messages(parsed_fixture())
        self.fixture = result

    def tearDown(self):
        del self.fixture

    def test_response(self):
        expectation = {
            "order": 1,
            "title": "Philippians - Part 4",
            "published_date": "Sun, 12 Nov 2017 18:39:03 +0000",
            "date": "Nov 12, 2017",
            "file": "http://traffic.libsyn.com/5stoneschurch/20171112_-_Philippians_-_Part_4.mp3",
            "image": "http://static.libsyn.com/p/assets/5/3/1/1/5311ea82ffe57b25/philippians-1x1.jpg"
        }
        self.assertEquals(self.fixture[0], expectation)
        self.assertIsInstance(self.fixture, list)

class LastMessageTest(unittest.TestCase):

    def setUp(self):
        result = parse_messages(parsed_fixture())
        self.fixture = result

    def tearDown(self):
        del self.fixture

    def test_response(self):
        self.assertNotEquals(self.fixture[-1]["title"], "Love Strong - Part 1")
        self.assertEquals(self.fixture[-1]["title"], "The Voice - Part 1")

if __name__ == '__main__':
    unittest.main()
