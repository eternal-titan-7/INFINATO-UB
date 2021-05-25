#
import inspect
import re
import sys
from pathlib import Path
from sys import *
from time import gmtime, sleep, strftime
from traceback import format_exc

from plugins import infinato_version as ult_ver
from telethon import *
from telethon import __version__ as telever
from telethon.errors.rpcerrorlist import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    FloodWaitError,
    MessageIdInvalidError,
    MessageNotModifiedError,
)
from telethon.utils import get_display_name

from .. import *
from ..dB.core import *
from ..functions.all import bash
from ..functions.all import time_formatter as tf
from ..utils import *
from ..version import __version__ as pyver
from ._wrappers import *

# sudo
ok = udB["SUDOS"]
if ok:
    SUDO_USERS = set(int(x) for x in ok.split())
else:
    SUDO_USERS = ""

if SUDO_USERS:
    sudos = list(SUDO_USERS)
else:
    sudos = ""

on = udB["SUDO"] if udB["SUDO"] is not None else "False"

if on == "True":
    sed = [ultroid_bot.uid, *sudos]
else:
    sed = [ultroid_bot.uid]

hndlr = "\\" + HNDLR

kek = udB.get("SUDO_PLUGINS")

if kek:
    SUDO_ALLOWED_PLUGINS = set(str(x) for x in kek.split(" "))
else:
    SUDO_ALLOWED_PLUGINS = ""

if SUDO_ALLOWED_PLUGINS:
    sudoplugs = list(SUDO_ALLOWED_PLUGINS)
else:
    sudoplugs = ""

black_list_chats = eval(udB.get("BLACKLIST_CHATS"))


# decorator


def ultroid_cmd(allow_sudo=on, **args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args["pattern"]
    groups_only = args.get("groups_only", False)
    admins_only = args.get("admins_only", False)

    if pattern is not None:
        if pattern.startswith(r"\#"):
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(hndlr + pattern)
        reg = re.compile("(.*)")
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = (
                    cmd.group(1)
                        .replace("$", "")
                        .replace("?(.*)", "")
                        .replace("(.*)", "")
                        .replace("(?: |)", "")
                        .replace("| ", "")
                        .replace("( |)", "")
                        .replace("?((.|//)*)", "")
                        .replace("?P<shortname>\\w+", "")
                )
            except BaseException:
                pass
            try:
                LIST[file_test].append(cmd)
            except BaseException:
                LIST.update({file_test: [cmd]})
        except BaseException:
            pass
    args["blacklist_chats"] = True
    black_list_chats = eval(udB.get("BLACKLIST_CHATS"))
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    # check if the plugin should allow edited updates
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        args["allow_edited_updates"]
        del args["allow_edited_updates"]
    if "admins_only" in args:
        del args["admins_only"]
    if "groups_only" in args:
        del args["groups_only"]

    # check if the plugin should listen for outgoing 'messages'

    def decorator(func):
        async def wrapper(ult):
            if allow_sudo == "False":
                if not ult.out:
                    return
            if not ult.out and (ult.sender_id not in sudos):
                return
            chat = await ult.get_chat()
            naam = get_display_name(chat)
            if ult.fwd_from:
                return
            if groups_only and ult.is_private:
                return await eod(ult, "`Use this in group/channel.`")
            if admins_only and not chat.admin_rights:
                return await eod(ult, "`I am not an admin.`")
            try:
                await func(ult)
            except MessageIdInvalidError:
                pass
            except MessageNotModifiedError:
                pass
            except FloodWaitError as fwerr:
                await ultroid_bot.asst.send_message(
                    Var.LOG_CHANNEL,
                    f"`FloodWaitError:\n{str(fwerr)}\n\nSleeping for {tf((fwerr.seconds + 10) * 1000)}`",
                )
                sleep(fwerr.seconds + 10)
                await ultroid_bot.asst.send_message(
                    Var.LOG_CHANNEL,
                    "`Bot is working again`",
                )
            except BotMethodInvalidError:
                return await eor(
                    ult,
                    "`Seems Like You are using BOT_MODE\nYou cant Use This Command !`",
                )
            except ChatSendInlineForbiddenError:
                return await eod(ult, "`Inline Locked In This Chat.`")
            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException as e:
                LOGS.exception(e)
                date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                ftext = (
                    "**Infinato Client Error:** `Report this to Developers.`\n\n"
                )
                ftext += "\nInfinato Version: " + str(ult_ver)
                ftext += "\nTelethon Version: " + str(telever) + "\n\n"
                ftext += "--------START INFINATO CRASH LOG--------"
                ftext += "\nDate: " + date
                ftext += "\nGroup: " + str(ult.chat_id) + " " + str(naam)
                ftext += "\nSender ID: " + str(ult.sender_id)
                ftext += "\nReplied: " + str(ult.is_reply)
                ftext += "\n\nEvent Trigger:\n"
                ftext += str(ult.text)
                ftext += "\n\nTraceback info:\n"
                ftext += str(format_exc())
                ftext += "\n\nError text:\n"
                ftext += str(sys.exc_info()[1])
                ftext += "\n\n--------END INFINATO CRASH LOG--------"
                ftext += "\n\n\nLast 5 commits:\n"

                stdout, stderr = await bash('git log --pretty=format:"%an: %s" -5')
                result = str(stdout.strip()) + str(stderr.strip())

                ftext += result + "`"

                if Var.LOG_CHANNEL:
                    Placetosend = Var.LOG_CHANNEL
                else:
                    Placetosend = ultroid_bot.uid
                await ultroid_bot.asst.send_message(
                    Placetosend,
                    ftext,
                )

        ultroid_bot.add_event_handler(wrapper, events.NewMessage(**args))
        try:
            LOADED[file_test].append(wrapper)
        except Exception:
            LOADED.update({file_test: [wrapper]})
        return wrapper

    return decorator
