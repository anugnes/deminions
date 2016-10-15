#!/usr/local/bin/python
from Libraries.gmail_utils import generate_google_service, send_message
from Libraries.utils import create_message
import time
import requests
import json
import os


__author__ = 'anugnes'


def main():
    path = os.path.dirname(os.path.abspath(__file__))

    with open(path + '/Config/settings.json') as conf:
        settings = json.load(conf)

    gmail_service = generate_google_service(settings)
    start_time = time.time()

    r = requests.get('http://beta.cmile.co.uk/#!/guest/login')

    if not r.status_code == 200:

        message = create_message(
            settings['sender'],
            settings['receiver'],
            "ALERT: Cmile did not respond correctly",
            "Latest response code while fetching Cmile: %s \n\n Duration: %s"
            %
            (r.status_code, time.time() - start_time))

        send_message(gmail_service, settings['sender'], message)

if __name__ == '__main__':
    print main()
