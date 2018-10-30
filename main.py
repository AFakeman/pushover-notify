#! /usr/bin/env python3

import requests
import sys
import argparse

from config import API_KEY, DEVICE_KEY


API_HANDLE = 'https://api.pushover.net/1/messages.json'

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--title', dest='title', help='title')
parser.add_argument('-m', '--message', dest='message', help='message', nargs='+')

namespace = parser.parse_args()

if namespace.message:
    message = " ".join(namespace.message)
else:
    message = sys.stdin.read().strip()

data = {
    'token': API_KEY,
    'user': DEVICE_KEY,
    'message': message,
}

if namespace.title:
    data['title'] = namespace.title

req = requests.post(API_HANDLE, json=data)
print(req.json(), file=sys.stderr)
req.raise_for_status()
