from telethon.tl.custom import Message

from . import *


@ultroid_cmd(pattern="uspam")
async def unlimitedspam(ult):
    input = ult.text[7:]
    udB.delete("USPAM")
    x = None
    while x == None:
        x = Redis("USPAM")
        await ult.respond(input)


@ultroid_cmd(pattern="resend")
async def _(ult: Message):
    try:
        await ult.delete()
    except Exception as ex:
        LOGS.info(ex)
    if ult.reply_to_msg_id:
        m = ult.get_reply_message()
        if m:
            await ult.respond(m)


@ultroid_cmd(pattern="stopuspam$")
async def _(e):
    udB.set("USPAM", ".")
    await eod(e, "Unlimited spam stopped")
