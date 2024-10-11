#/usr/bin/python3
import requests
import sys

url = 'http://web0x01.hbtn/a1/hijack_session'
response = requests.get(url)


times = sys.argv[1]

for i in range(int(times)):
    print(requests.get(url).cookies.get_dict()['hijack_session'])
