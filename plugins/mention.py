from telethon import events
import asyncio
from . import *


@ultroid_cmd(pattern="mention (.*)")
async def _(event):
    if event.fwd_from:
        return
    txt = event.pattern_match.group(1).split(" ")
    un = txt[0].strip("@")
    nm = txt[1]
    await event.edit(f"[{nm}](https://t.me/{un}) {' '.join(txt[2::])}")


@ultroid_cmd(pattern="mention_id (.*)")
async def _(event):
    if event.fwd_from:
        return
    txt = event.pattern_match.group(1).split(" ")
    un = txt[0]
    nm = txt[1]
    await event.edit(f"[{nm}](tg://user?id={un}) {' '.join(txt[2::])}")
