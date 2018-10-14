from sys import argv
import json

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

f = open(argv[1], 'r')
json_str = f.read()
message_list = json.loads(json_str)

s = "["

for j in message_list:
    s += "\"{}\",".format(j['message'])


s = s[:-1]
s += "]"

print(s)
