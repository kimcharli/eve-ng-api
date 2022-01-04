#!python

import requests
import urllib3
import json

eve_api_url = "https://10.85.192.7/api"
eve_login_data = {
    "username": "admin",
    "password": "eve",
    "html5": -1
 }

cookies = {}
headers = {"Content-Type": "application/json"}

urllib3.disable_warnings()
session = requests.Session()

resp = session.post(f"{eve_api_url}/auth/login", cookies=cookies, json=eve_login_data, verify=False)
print(f"login_resp: {resp.json()}")

resp = session.get(f"{eve_api_url}/labs/Users/lab1/JL3V-LAB1.unl/nodes/status", cookies=cookies, verify=False)
print(f"nodes_resp: {resp.json()['data']}")





