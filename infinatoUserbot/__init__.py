
import os
import time
from datetime import datetime
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, FileHandler, StreamHandler, basicConfig, getLogger

from decouple import config
from redis import ConnectionError, ResponseError, StrictRedis
from telethon import TelegramClient
from telethon.errors.rpcerrorlist import AuthKeyDuplicatedError
from telethon.sessions import StringSession

from .dB.core import *
from .dB.database import Var
from .misc import *
from .utils import *
from .version import __version__

LOGS = getLogger(__name__)

# remove the old logs file.
if os.path.exists("infinato.log"):
    os.remove("infinato.log")

# start logging into a new file.
basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=INFO,
    handlers=[FileHandler("infinato.log"), StreamHandler()],
)

LOGS.info(
    """
                -----------------------------------
                        Starting Deployment
                -----------------------------------
"""
)


def connect_redis():
    redis_info = Var.REDIS_URI.split(":")
    DB = StrictRedis(
        host=redis_info[0],
        port=redis_info[1],
        password=Var.REDIS_PASSWORD,
        charset="utf-8",
        decode_responses=True,
    )
    return DB


try:
    udB = connect_redis()
    LOGS.info("Getting Connection With Redis Database")
    time.sleep(6)
except ConnectionError as ce:
    LOGS.info(f"ERROR - {ce}")
    exit(1)
except ResponseError as res:
    LOGS.info(f"ERROR - {res}")
    exit(1)
except Exception as er:
    LOGS.info(f"ERROR - {er}")
    exit(1)

START_TIME = datetime.now()

try:
    udB.ping()
except BaseException:
    ok = []
    LOGS.info("Can't connect to Redis Database.... Restarting....")
    for x in range(1, 6):
        udB = connect_redis()
        time.sleep(5)
        try:
            if udB.ping():
                ok.append("ok")
                break
        except BaseException:
            LOGS.info(f"Connection Failed ...  Trying To Reconnect {x}/5 ..")
    if not ok:
        LOGS.info("Redis Connection Failed.....")
        exit()
    else:
        LOGS.info("Reconnected To Redis Server Succesfully")

LOGS.info("Succesfully Established Connection With Redis DataBase.")

BOT_MODE = Var.BOT_MODE or udB.get("BOT_MODE")

if Var.SESSION:
    try:
        ultroid_bot = TelegramClient(
            StringSession(Var.SESSION), Var.API_ID, Var.API_HASH
        )
    except Exception as ap:
        LOGS.info(f"ERROR - {ap}")
        exit(1)
elif str(BOT_MODE) == "True":
    try:
        ultroid_bot = TelegramClient(
            None, api_id=Var.API_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
    except Exception as ap:
        LOGS.info(f"ERROR - {ap}")
        exit(1)
else:
    LOGS.info("No string Session found, Bot Quiting Now !!")
    exit(1)

if str(BOT_MODE) == "True" and not (udB.get("OWNER_ID") or Var.OWNER_ID):
    LOGS.info("ERROR - OWNER_ID Not Found ! Please Add it !")
    exit(1)

if udB.get("HNDLR"):
    HNDLR = udB.get("HNDLR")
else:
    udB.set("HNDLR", ".")
    HNDLR = udB.get("HNDLR")

if not udB.get("SUDO"):
    udB.set("SUDO", "False")

if not udB.get("SUDOS"):
    udB.set("SUDOS", "1")

if udB.get("VC_SESSION"):
    try:
        vcbot = TelegramClient(
            StringSession(udB.get("VC_SESSION")),
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
        )
    except AuthKeyDuplicatedError:
        LOGS.info("ERROR - Please create a new VC string Session !")
        vcbot = None
    except Exception:
        vcbot = None
else:
    vcbot = None
