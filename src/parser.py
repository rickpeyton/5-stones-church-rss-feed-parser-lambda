from __future__ import print_function

import requests
from bs4 import BeautifulSoup

fake = {
    "title": "5 Stones Church  - Weekend Messages",
    "url": "http://www.5stoneschurch.com",
    "email": "media@5stoneschurch.com",
    "description": "A life-giving church in Franklin, TN. Follow Jesus - Experience Freedom - Discover Purpose - Make a Difference. 10 AM - Freedom Intermediate School",
    "messages": [{
        "order": 1,
        "title": "Doors - Part 1",
        "published_date": "Sun, 05 Mar 2017 20:15:44 +0000",
        "date": "MAR 05, 2017",
        "file": "http://traffic.libsyn.com/5stoneschurch/20170305_-_Doors_Part_1.mp3",
        "length": "28:10"
    }, {
        "order": 2,
        "title": "Love Strong - Part 4",
        "published_date": "Sun, 05 Mar 2017 20:14:29 +0000",
        "date": "FEB 26, 2017",
        "file": "http://traffic.libsyn.com/5stoneschurch/20170226_-_Love_Strong_Part_4.mp3",
        "length": "32:48"
    }]
}


def lambda_handler(event, context):
    response = send_request()
    parsed_xml = BeautifulSoup(response.text, 'lxml-xml')
    meta = Meta(parsed_xml)
    messages = parse_messages(parsed_xml)

    return fake


def parse_messages(response):
    messages = []
    messages.append()

    return [message]


class Meta(object):

    def __init__(self, response):
        self.title = "5 Stones Church  - Weekend Messages"
        self.url = "http://www.5stoneschurch.com"
        self.email = "media@5stoneschurch.com"
        self.description = "A life-giving church in Franklin, TN. Follow Jesus - Experience Freedom - Discover Purpose - Make a Difference. 10 AM - Freedom Intermediate School"


class Message(object):

    def __init__(self, response):
        self.order = 1
        self.title = "Doors - Part 1"
        self.published_date = "Sun, 05 Mar 2017 20:15:44 +0000"
        self.date = "MAR 05, 2017"
        self.file = "http://traffic.libsyn.com/5stoneschurch/20170305_-_Doors_Part_1.mp3"
        self.length = "28:10"

    def as_dict(self):
        return {
            "order": self.order,
            "title": self.title,
            "published_date": self.published_date, 05 Mar 2017 20:15:44 +0000",
            "date": self.date, 2017",
            "file": self.file,
            "length": self.length
        }


def send_request():

    try:
        feed = requests.get("http://5stoneschurch.libsyn.com/rss")
        return feed
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
