from __future__ import print_function

import requests
from bs4 import BeautifulSoup


def lambda_handler(event, context):
    response = send_request()
    parsed_xml = BeautifulSoup(response.text, 'lxml-xml')
    meta = Meta(parsed_xml)
    messages = parse_messages(parsed_xml)

    json_response = {
        "title": meta.title,
        "url": meta.url,
        "email": meta.email,
        "description": meta.description,
        "messages": messages
    }

    return json_response


def parse_messages(response):
    messages = []
    message = Message(response).as_dict()
    messages.append(message)

    return messages


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
            "published_date": self.published_date,
            "date": self.date,
            "file": self.file,
            "length": self.length
        }


def send_request():

    try:
        feed = requests.get("http://5stoneschurch.libsyn.com/rss")
        return feed
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
