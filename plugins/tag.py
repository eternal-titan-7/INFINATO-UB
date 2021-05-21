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

• `{i}tagadd <Reply to the Person>`
    Add someone to Tag List For Specific Chat.

• `{i}tagclear <Reply to the Person>`
    Clear Tag List For Specific Chat.

• `{i}taglist`
    Tag Members on Tag List For Specific Chat.

• `{i}tageveryone`
    Tag Everyone in chat With Less Spam.
"""
from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec
from telethon.utils import get_display_name

from . import *


def update_list(chat, name, id):
    if not udB.get("TAGLIST"):
        taglist = {chat: []}
        udB.set("TAGLIST", str(taglist))
    taglist = eval(udB.get("TAGLIST"))
    if chat not in taglist.keys():
        taglist[chat] = []
    taglist[chat].append([name, id])
    udB.set("TAGLIST", str(taglist))


def clear_list(chat):
    if not udB.get("TAGLIST"):
        taglist = {}
        udB.set("TAGLIST", str(taglist))
        return
    taglist = eval(udB.get("TAGLIST"))
    if chat not in taglist.keys():
        return
    del taglist[chat]
    udB.set("TAGLIST", str(taglist))


def get_list(chat):
    if not udB.get("TAGLIST"):
        taglist = {chat: []}
        udB.set("TAGLIST", str(taglist))
    taglist = eval(udB.get("TAGLIST"))
    if chat not in taglist.keys():
        taglist[chat] = []
    return taglist[chat]


@ultroid_cmd(
    pattern="tag(on|off|all|bots|rec|admins|owner|list|add|clear|everyone)?(.*)",
    groups_only=True,
)
async def _(e):
    okk = e.text
    try:
        lll = okk.split(" ", maxsplit=1)[1]
    except:
        lll = ""
    users = 0
    o = 0
    nn = 0
    rece = 0
    xx1 = []
    if okk[4:8] == "list":
        taglist = get_list(e.chat_id)
        if len(taglist) == 0:
            await e.edit("TAGLIST is Empty.")
            await asyncio.sleep(2)
        else:
            for xb in taglist:
                xx1.append(f"[{xb[0]}](tg://user?id={xb[1]})")
    elif okk[4:7] == "add":
        replied_user, error_i_a = await get_full_user(e)
        if replied_user is not None:
            rpl = replied_user.user.id
            nm = get_display_name(replied_user.user)
            update_list(e.chat_id, nm, rpl)
            await e.edit(f"[{nm}](tg://user?id={rpl}) was added to TAGLIST.")
            await asyncio.sleep(2)
        else:
            await e.edit("Please Reply to the person.")
            await asyncio.sleep(2)
    elif okk[4:9] == "clear":
        clear_list(e.chat_id)
        await e.edit(f"TAGLIST of this group was cleared.")
        await asyncio.sleep(2)
    else:
        async for bb in e.client.iter_participants(e.chat_id):
            users = users + 1
            x = bb.status
            y = bb.participant
            if isinstance(x, onn):
                o = o + 1
                if okk[4:6].lower() == "on":
                    xx1.append(f"[{get_display_name(bb)}](tg://user?id={bb.id})")
            if isinstance(x, off):
                nn = nn + 1
                if okk[4:7].lower() == "off":
                    if not (bb.bot or bb.deleted):
                        xx1.append(f"[{get_display_name(bb)}](tg://user?id={bb.id})")
            if isinstance(x, rec):
                rece = rece + 1
                if okk[4:7].lower() == "rec":
                    if not (bb.bot or bb.deleted):
                        xx1.append(f"[{get_display_name(bb)}](tg://user?id={bb.id})")
            if isinstance(y, owner):
                if (okk[4:9] == "admin") or (okk[4:9] == "owner"):
                    xx1.append(f"꧁[{get_display_name(bb)}](tg://user?id={bb.id})꧂")
            if isinstance(y, admin):
                if okk[4:9] == "admin":
                    if not bb.deleted:
                        xx1.append(f"[{get_display_name(bb)}](tg://user?id={bb.id})")
            if okk[4:7] == "all":
                if not (bb.bot or bb.deleted):
                    xx1.append(f"[{get_display_name(bb)}](tg://user?id={bb.id})")
            if okk[4:12] == "everyone":
                if not (bb.bot or bb.deleted):
                    xx1.append(f"[\u200b](tg://user?id={bb.id})")
            if okk[4:8] == "bots":
                if bb.bot:
                    xx1.append(f"[{get_display_name(bb)}](tg://user?id={bb.id})")
    if okk[4:12] == "everyone":
        for z in range(0, len(xx1), 1000):
            xx = lll + "\n\n`<\\Everyone\\>`\n"
            mentions = ' '.join(xx1[z:z + 1000])
            xx += f"\n{mentions}"
            await e.client.send_message(e.chat_id, xx)
            await asyncio.sleep(2)
    else:
        for z in range(0, len(xx1), 100):
            xx = lll
            mentions = ' '.join(xx1[z:z + 100])
            xx += f"\n{mentions}"
            await e.client.send_message(e.chat_id, xx)
            await asyncio.sleep(2)
    await e.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
