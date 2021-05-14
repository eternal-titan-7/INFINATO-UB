
import functools

from telethon import *
from telethon import events
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name

from .. import *
from ..dB.core import *
from ..utils import *
from ._decorators import sed

OWNER_NAME = infinato_bot.me.first_name
OWNER_ID = infinato_bot.me.id
INFINATO_PIC = "https://telegra.ph/file/9c22477daacf4ca4a2914.png"
MSG = f"""
**INFINATO BOT**
➖➖➖➖➖➖➖➖➖➖
**Owner**: [{get_display_name(infinato_bot.me)}](tg://user?id={infinato_bot.me.id})
➖➖➖➖➖➖➖➖➖➖
"""

# decorator for assistant


def inline_owner():
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(event):
            try:
                await function(event)
            except BaseException:
                pass

        return wrapper

    return decorator


def asst_cmd(dec):
    def ult(func):
        pattern = "^/" + dec  # todo - handlers for assistant?
        infinato_bot.asst.add_event_handler(
            func, events.NewMessage(incoming=True, pattern=pattern)
        )

    return ult


def callback(sed):
    def ultr(func):
        data = sed
        infinato_bot.asst.add_event_handler(
            func, events.callbackquery.CallbackQuery(data=data)
        )

    return ultr


def inline():
    def ultr(func):
        infinato_bot.asst.add_event_handler(func, events.InlineQuery)

    return ultr


def in_pattern(pat):
    def don(func):
        pattern = pat
        infinato_bot.asst.add_event_handler(func, events.InlineQuery(pattern=pattern))

    return don


# check for owner
def owner():
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(event):
            if event.sender_id in sed:
                await function(event)
            else:
                try:
                    await event.answer(f"This is {OWNER_NAME}'s bot!!")
                except BaseException:
                    pass

        return wrapper

    return decorator
