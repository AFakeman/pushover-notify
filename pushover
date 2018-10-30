#! /usr/bin/env python3

import requests
import sys
import argparse
import json

import os

config_dir = os.environ.get('XDG_CONFIG_HOME', '~/.config')

API_HANDLE = 'https://api.pushover.net/1/messages.json'

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--title', dest='title', help='title')
parser.add_argument('-m', '--message', dest='message', help='message', nargs='+')
parser.add_argument('-v', '--verbose', dest='verbose',
        help='print server response', nargs='+')
parser.add_argument('-c', '--client', dest='client', help='client to send the notification to')

namespace = parser.parse_args()

with open(os.path.join(config_dir, 'pushover.json')) as f:
    config = json.load(f)

api_key = config['apiKey']
if namespace.client:
    client = namespace.client
else:
    client = config['defaultClient']

if namespace.message:
    message = " ".join(namespace.message)
else:
    message = sys.stdin.read().strip()

data = {
    'token': api_key,
    'user': client,
    'message': message,
}

if namespace.title:
    data['title'] = namespace.title

req = requests.post(API_HANDLE, json=data)

if namespace.verbose:
    print(req.json(), file=sys.stderr)
try:
    req.raise_for_status()
except:
    print(req.json(), file=sys.stderr)
    raise
