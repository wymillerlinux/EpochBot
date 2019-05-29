# bot.py
# Bot startup and loop for Epoch
# Written by Wyatt J. Miller

import config as c
import util
import socket
import re
import logging
import sys

from time import sleep

def main():
    s = socket.socket()
    s.connect((c.HOST, c.PORT))
    s.send(f"PASS {c.PASS}\r\n".encode("utf-8"))
    s.send(f"NICK {c.NICK}\r\n".encode("utf-8"))
    s.send(f"JOIN #{c.CHAN}\r\n".encode("utf-8"))

    logging.basicConfig(filename="./app.log", filemode="w+", format="%(asctime)s - %(levelname)s - %(message)s")

    chat_msg = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    logging.debug(f"EpochBot: version {c.VERSION}")
    logging.debug("Logging has started!")

    util.chat(s, "Hello and welcome! Messages sent to this bot will be logged.")

    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0)
            message = chat_msg.sub("", response)
            logging.info(response)

            if message.strip() == "!links":
                logging.info(f"{c.PERSONAL} {c.GITHUB}")
                util.chat(s, f"{c.PERSONAL} {c.GITHUB}")
                # code goes here
            if message.strip() == "!projects":
                logging.info(f"Chatversity API: {c.CHATVERSITY}\n")
                util.chat(s, f"Chatversity API: {c.CHATVERSITY}\n")
            if message.strip() == "!help":
                logging.info(f"!links - To see what I'm up to - !projects - Current projects I'm working on - !help - Displays this help page - !schudule - To see when I'm streaming")
                util.chat(s, f"!links - To see what I'm up to - !projects - Current projects I'm working on - !help - Displays this help page - !schudule - To see when I'm streaming")
            if message.strip() == "!schedule":
                logging.info(f"I'm going to try to get get on once a week during the weekend, typically around 9PM EST.")
                util.chat(s, f"I'm going to try to get get on once a week during the weekend, typically around 9PM EST.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Gracefully shutting down...")
    except Exception:
        print("Exception occurred!")
        sys.exit(0)


