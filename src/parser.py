from __future__ import print_function

import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup

import os
import yaml


def lambda_handler(event, context):
    response = send_request()

    if True == False:
        with open(os.path.join(os.path.dirname(__file__), ".", "request_fixture_20170611.yml"), 'w') as f:
            f.write(response)

    parsed_xml = BeautifulSoup(response.text, 'lxml-xml')
    meta = Meta(parsed_xml)
    messages = parse_messages(parsed_xml)

    json_response = {
        "title": meta.title,
        "url": meta.url,
        "description": meta.description,
        "messages": messages
    }

    return json_response


def parse_messages(response):
    messages = []
    counter = 1
    for i in response.findAll("item"):
        message = Message(i, counter).as_dict()
        counter = counter + 1
        messages.append(message)

    return messages


class Meta(object):

    def __init__(self, response):
        self.title = response.rss.channel.title.renderContents()
        self.url = response.findAll("link")[2].renderContents()
        self.description = response.rss.channel.description.renderContents()


class Message(object):

    def __init__(self, response, counter):
        self.order = counter
        self.title = response.title.renderContents()
        self.published_date = response.pubDate.renderContents()
        self.file = response.link.renderContents()
        self.date = UrlToDate(self.file).date()

    def as_dict(self):
        return {
            "order": self.order,
            "title": self.title,
            "published_date": self.published_date,
            "date": self.date,
            "file": self.file,
        }


class UrlToDate(object):

    def __init__(self, url):
        self.url = url

    def date(self):
        date_string = re.search('(?=\/(\d{8}))', self.url).group(1)
        date_object = datetime.strptime(date_string, '%Y%m%d')
        return date_object.strftime('%b %d, %Y')


def send_request():

    try:
        feed = requests.get("http://5stoneschurch.libsyn.com/rss")
        return feed
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
