#!/usr/bin/python3
"""
Script that fetches url content of https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    req = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as r:
        html = r.read()
    print("Body response:\n"
          "\t- type: {}\n"
          "\t- content: {}\n"
          "\t- utf8 content: {}".
          format(type(html), html, html.decode('utf-8'))
          )
