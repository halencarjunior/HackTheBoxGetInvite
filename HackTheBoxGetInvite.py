#!/bin/python
######################################
# Invite Generator for Hackthebox
# by Humberto Júnior
# 28/08/2017
# requirements: python3 requests
#
######################################
import requests
import json
import base64

print("HackTheBoxGetInvite v0.1\n\n")
print("[+] Aguarde, gerando a chave:\n")

r = requests.post("https://www.hackthebox.eu/api/invite/generate")
json_object = json.dumps(r.json())

resp = json.loads(json_object)

key = resp['data']['code']

print("Chave gerada: " + base64.b64decode(key).decode('utf-8'))
