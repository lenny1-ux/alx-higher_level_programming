#!/usr/bin/python3
"""
The script that requests content from `https://intranet.hbtn.io/status`
"""

import urllib.request

if __name__ == "__main__":
    req = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content: {}'.format(body.decode('utf8')))
