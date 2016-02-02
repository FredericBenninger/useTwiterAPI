#!/usr/bin/python3

# Send a tweet 

from twython import Twython
import pprint

exec(open("initkeys.py").read())

api = Twython(C_K, C_S, A_T, A_S)

pp = pprint.PrettyPrinter(depth=5)

pp.pprint(api.verify_credentials())

api.update_status(status="Hello world")
