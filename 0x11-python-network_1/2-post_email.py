#!/usr/bin/python3
""" script takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    rawdata = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(rawdata)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as r:
        print(r.read().decode("utf-8", "replace"))
