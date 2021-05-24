
import asyncio
import glob
import os
import traceback
import urllib
from pathlib import Path
from random import randint

import telethon.utils
from telethon import TelegramClient
from telethon import __version__ as vers
from telethon.errors.rpcerrorlist import (
    ApiIdInvalidError,
    AuthKeyDuplicatedError,
    PhoneNumberInvalidError,
)
from telethon.tl.custom import Button
from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditAdminRequest,
    EditPhotoRequest,
    JoinChannelRequest,
)
from telethon.tl.types import (
    ChatAdminRights,
    InputChatUploadedPhoto,
    InputMessagesFilterDocument,
)

from . import *
from .dB import DEVLIST
from .functions.all import updater
from .utils import *
from .version import __version__ as ver

x = ["resources/auths", "resources/downloads", "addons"]
for x in x:
    if not os.path.isdir(x):
        os.mkdir(x)

if udB.get("CUSTOM_THUMBNAIL"):
    os.system(f"wget {udB.get('CUSTOM_THUMBNAIL')} -O resources/extras/cf1.jpg")

if udB.get("GDRIVE_TOKEN"):
    with open("resources/auths/auth_token.txt", "w") as t_file:
        t_file.write(udB.get("GDRIVE_TOKEN"))


async def istart(ult):
    await ultroid_bot.start(ult)
    ultroid_bot.me = await ultroid_bot.get_me()
    ultroid_bot.uid = telethon.utils.get_peer_id(ultroid_bot.me)
    ultroid_bot.first_name = ultroid_bot.me.first_name
    if not ultroid_bot.me.bot:
        udB.set("OWNER_ID", ultroid_bot.uid)
    if str(BOT_MODE) == "True":
        if Var.OWNER_ID:
            OWNER = await ultroid_bot.get_entity(Var.OWNER_ID)
            ultroid_bot.me = OWNER
            asst.me = OWNER
            ultroid_bot.uid = OWNER.id
            ultroid_bot.first_name = OWNER.first_name
        elif udB.get("OWNER_ID"):
            OWNER = await ultroid_bot.get_entity(int(udB.get("OWNER_ID")))
            ultroid_bot.me = OWNER
            asst.me = OWNER
            ultroid_bot.uid = OWNER.id
            ultroid_bot.first_name = OWNER.first_name


ultroid_bot.asst = None


async def bot_info(asst):
    await asst.start()
    asst.me = await asst.get_me()
    return asst.me


LOGS.info(
    """
                -----------------------------------
                        Starting Deployment
                -----------------------------------
"""
)


LOGS.info("Initialising...")
LOGS.info(f"InfinatoLoader Version - {ver}")
LOGS.info(f"Telethon Version - {vers}")
LOGS.info("INFINATO Version - 0.0.7.1")

if str(BOT_MODE) == "True":
    mode = "Bot Mode - Started"
else:
    mode = "User Mode - Started"

# log in
if Var.BOT_TOKEN:
    LOGS.info("Starting INFINATO...")
    try:
        ultroid_bot.asst = TelegramClient(
            "infinato", api_id=Var.API_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
        asst = ultroid_bot.asst
        ultroid_bot.loop.run_until_complete(istart(asst))
        ultroid_bot.loop.run_until_complete(bot_info(asst))
        LOGS.info("Done, startup completed")
        LOGS.info(mode)
    except AuthKeyDuplicatedError or PhoneNumberInvalidError:
        LOGS.info(
            "Session String expired. Please create a new one! Infinato is stopping..."
        )
        exit(1)
    except ApiIdInvalidError:
        LOGS.info("Your API ID/API HASH combination is invalid. Kindly recheck.")
        exit(1)
    except BaseException:
        LOGS.info("Error: " + str(traceback.print_exc()))
        exit(1)
else:
    LOGS.info(mode)
    ultroid_bot.start()

BOTINVALID_PLUGINS = [
    "globaltools",
    "autopic",
    "pmpermit",
    "fedutils",
    "_userlogs",
    "webupload",
    "clone",
    "inlinefun",
    "tscan",
    "animedb",
    "limited",
    "quotly",
    "findsong",
    "sticklet",
]

# for userbot
path = "plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        try:
            if str(BOT_MODE) == "True" and plugin_name in BOTINVALID_PLUGINS:
                LOGS.info(
                    f"INFINATO - BOT_MODE_INVALID_PLUGIN - {plugin_name}"
                )
            else:
                load_plugins(plugin_name.replace(".py", ""))
                if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                    LOGS.info(f"INFINATO -  Installed - {plugin_name}")
        except Exception:
            LOGS.info(f"INFINATO - ERROR - {plugin_name}")
            LOGS.info(str(traceback.print_exc()))


# for addons
addons = udB.get("ADDONS")
if addons == "True" or addons is None:
    try:
        os.system("git clone https://github.com/TeamUltroid/UltroidAddons.git addons/")
    except BaseException:
        pass
    LOGS.info("Installing packages for addons")
    os.system("pip install -r addons/addons.txt")
    path = "addons/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            try:
                if str(BOT_MODE) == "True" and plugin_name in BOTINVALID_PLUGINS:
                    LOGS.info(
                        f"Ultroid - Addons - BOT_MODE_INVALID_PLUGIN - {plugin_name}"
                    )
                else:
                    load_addons(plugin_name.replace(".py", ""))
                    if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                        LOGS.info(f"Ultroid - Addons - Installed - {plugin_name}")
            except Exception as e:
                LOGS.info(f"Ultroid - Addons - ERROR - {plugin_name}")
                LOGS.info(str(e))
else:
    os.system("cp plugins/__init__.py addons/")


# for assistant
path = "assistant/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        try:
            load_assistant(plugin_name.replace(".py", ""))
            if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                LOGS.info(f"INFINATO - Assistant - Installed - {plugin_name}")
        except Exception as e:
            LOGS.info(f"INFINATO - Assistant - ERROR - {plugin_name}")
            LOGS.info(str(e))

# for channel plugin
Plug_channel = udB.get("PLUGIN_CHANNEL")
if Plug_channel:

    async def plug():
        if str(BOT_MODE) == "True":
            LOGS.info("PLUGIN_CHANNEL Can't be used in BOT_MODE")
            return
        try:
            if Plug_channel.startswith("@"):
                chat = Plug_channel
            else:
                try:
                    chat = int(Plug_channel)
                except BaseException:
                    return
            async for x in ultroid_bot.iter_messages(
                chat, search=".py", filter=InputMessagesFilterDocument
            ):
                await asyncio.sleep(0.6)
                files = await ultroid_bot.download_media(x.media, "./addons/")
                file = Path(files)
                plugin = file.stem
                if "(" not in files:
                    try:
                        load_addons(plugin.replace(".py", ""))
                        LOGS.info(f"INFINATO - PLUGIN_CHANNEL - Installed - {plugin}")
                    except Exception as e:
                        LOGS.info(f"INFINATO - PLUGIN_CHANNEL - ERROR - {plugin}")
                        LOGS.info(str(e))
                else:
                    LOGS.info(f"Plugin {plugin} is Pre Installed")
                    os.remove(files)
        except Exception as e:
            LOGS.info(str(e))


# chat via assistant
pmbot = udB.get("PMBOT")
if pmbot == "True":
    path = "assistant/pmbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            load_pmbot(plugin_name.replace(".py", ""))
    LOGS.info(f"Infinato - PM Bot Message Forwards - Enabled.")

# customize assistant


async def customize():
    try:
        xx = await ultroid_bot.get_entity(asst.me.username)
        if xx.photo is None:
            LOGS.info("Customising Ur Assistant Bot in @BOTFATHER")
            UL = f"@{asst.me.username}"
            if (ultroid_bot.me.username) is None:
                sir = ultroid_bot.me.first_name
            else:
                sir = f"@{ultroid_bot.me.username}"
            await ultroid_bot.send_message(
                Var.LOG_CHANNEL, "Auto Customisation Started on @botfather"
            )
            await asyncio.sleep(1)
            await ultroid_bot.send_message("botfather", "/cancel")
            await asyncio.sleep(1)
            await ultroid_bot.send_message("botfather", "/start")
            await asyncio.sleep(1)
            await ultroid_bot.send_message("botfather", "/setuserpic")
            await asyncio.sleep(1)
            await ultroid_bot.send_message("botfather", UL)
            await asyncio.sleep(1)
            await ultroid_bot.send_file(
                "botfather", "resources/extras/cf1.jpg"
            )
            await asyncio.sleep(2)
            await ultroid_bot.send_message("botfather", "/setabouttext")
            await asyncio.sleep(1)
            await ultroid_bot.send_message("botfather", UL)
            await asyncio.sleep(1)
            await ultroid_bot.send_message(
                "botfather", f"✨ Hello ✨!! I'm Assistant Bot of {sir}"
            )
            await asyncio.sleep(2)
            await ultroid_bot.send_message("botfather", "/setdescription")
            await asyncio.sleep(1)
            await ultroid_bot.send_message("botfather", UL)
            await asyncio.sleep(1)
            await ultroid_bot.send_message(
                "botfather",
                f"✨PowerFull INFINATO Assistant Bot✨\n✨Master ~ {sir} ✨",
            )
            await asyncio.sleep(2)
            await ultroid_bot.send_message("botfather", "/start")
            await asyncio.sleep(1)
            await ultroid_bot.send_message(
                Var.LOG_CHANNEL, "**Auto Customisation** Done at @BotFather"
            )
            LOGS.info("Customisation Done")
    except Exception as e:
        LOGS.warning(str(e))


# some stuffs
async def ready():
    chat_id = Var.LOG_CHANNEL
    try:
        MSG = f"**INFINATO has been deployed!**\n➖➖➖➖➖➖➖➖➖\n**UserMode**: [{ultroid_bot.me.first_name}](tg://user?id={ultroid_bot.me.id})\n**Assistant**: @{asst.me.username}\n➖➖➖➖➖➖➖➖➖"
        BTTS = None
        updava = await updater()
        if updava:
            BTTS = [[Button.inline(text="Update Available", data="updtavail")]]
        await ultroid_bot.asst.send_message(chat_id, MSG, buttons=BTTS)
    except BaseException:
        try:
            MSG = f"**INFINATO has been deployed!**\n➖➖➖➖➖➖➖➖➖\n**UserMode**: [{ultroid_bot.me.first_name}](tg://user?id={ultroid_bot.me.id})\n**Assistant**: @{asst.me.username}\n➖➖➖➖➖➖➖➖➖"
            await ultroid_bot.send_message(chat_id, MSG)
        except Exception as ef:
            LOGS.info(ef)


if Var.HEROKU_APP_NAME:
    ws = f"WEBSOCKET_URL=https://{Var.HEROKU_APP_NAME}.herokuapp.com"
else:
    ws = f"WEBSOCKET_URL=127.0.0.1"

try:
    with open(".env", "r") as x:
        m = x.read()
    if "WEBSOCKET_URL" not in m:
        with open(".env", "a+") as t:
            t.write("\n" + ws)
except BaseException:
    with open(".env", "w") as t:
        t.write(ws)


if str(BOT_MODE) != "True":
    ultroid_bot.loop.run_until_complete(customize())
    if Plug_channel:
        ultroid_bot.loop.run_until_complete(plug())
ultroid_bot.loop.run_until_complete(ready())

LOGS.info(
    """
                ----------------------------------------------------------------------
                                     INFINATO has been deployed!
                ----------------------------------------------------------------------
"""
)

if __name__ == "__main__":
    ultroid_bot.run_until_disconnected()
