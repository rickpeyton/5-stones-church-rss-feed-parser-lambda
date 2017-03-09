from __future__ import print_function

import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    response = send_request()
    parsed_xml = BeautifulSoup(response.text, 'lxml-xml')

    return parsed_xml

def send_request():

    try:
        feed = requests.get("http://5stoneschurch.libsyn.com/rss")
        return feed
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
