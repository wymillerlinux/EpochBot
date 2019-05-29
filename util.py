# util.py
# Utility functions for Epoch
# Written by Wyatt J. Miller

import config as c

# Base chat message
def chat(s, msg):
    s.send(f"PRIVMSG #{c.CHAN} :{msg}\r\n".encode("utf-8"))

# Timeout for a user
def timeout(s, user, seconds=300):
    chat(s, f".timeout {user, seconds}")

