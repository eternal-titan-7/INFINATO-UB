
"""
✘ Commands Available -

• `{i}tagall`
    Tag Top 100 Members of chat.

• `{i}tagadmins`
    Tag Admins of that chat.

• `{i}tagowner`
    Tag Owner of that chat

• `{i}tagbots`
    Tag Bots of that chat.

• `{i}tagrec`
    Tag recently Active Members.

• `{i}tagon`
    Tag online Members(work only if privacy off).

• `{i}tagoff`
    Tag Offline Members(work only if privacy off).
"""

from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec
from telethon.utils import get_display_name

from . import *


@ultroid_cmd(
    pattern="tag(on|off|all|bots|rec|admins|owner)?(.*)",
    groups_only=True,
)
async def _(e):
    okk = e.text
    lll = e.pattern_match.group(2)
    users = 0
    o = 0
    nn = 0
    rece = 0
    xx1 = []
    async for bb in e.client.iter_participants(e.chat_id):
        users = users + 1
        x = bb.status
        y = bb.participant
        if isinstance(x, onn):
            o = o + 1
            if "on" in okk:
                xx1.append(f"[{get_display_name(bb)}](tg://user?id={bb.id})")
        if isinstance(x, off):
            nn = nn + 1
            if "off" in okk:
                if not (bb.bot or bb.deleted):
                    xx1.append(f"[{get_display_name(bb)}](tg://user?id={bb.id})")
        if isinstance(x, rec):
            rece = rece + 1
            if "rec" in okk:
                if not (bb.bot or bb.deleted):
                    xx1.append(f"[{get_display_name(bb)}](tg://user?id={bb.id})")
        if isinstance(y, owner):
            if ("admin" in okk) or ("owner" in okk):
                xx1.append(f"꧁[{get_display_name(bb)}](tg://user?id={bb.id})꧂")
        if isinstance(y, admin):
            if "admin" in okk:
                if not bb.deleted:
                    xx1.append(f"[{get_display_name(bb)}](tg://user?id={bb.id})")
        if "all" in okk:
            if not (bb.bot or bb.deleted):
                xx1.append(f"[{get_display_name(bb)}](tg://user?id={bb.id})")
        if "bot" in okk:
            if bb.bot:
                xx1.append(f"[{get_display_name(bb)}](tg://user?id={bb.id})")
    for z in range(0, len(xx1), 100):
        if lll:
            xx = f"{lll}"
        else:
            xx = ""
        mentions = ' '.join(xx1[z:z+100])
        xx += f"\n{mentions}"
        await e.client.send_message(e.chat_id, xx)
        await asyncio.sleep(5)
    await e.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
