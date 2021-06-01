from pytz import timezone
from telethon.errors import FloodWaitError
from telethon.tl.functions.account import UpdateProfileRequest

from . import *


@ultroid_cmd(pattern="autoname")
async def _(ult):
    first_name = (await ultroid_bot.get_me()).first_name
    last_name = (await ultroid_bot.get_me()).last_name
    if first_name and last_name:
        DEFAULTUSER = f"{first_name} {last_name}"
    elif ultroid_bot.me.first_name:
        DEFAULTUSER = first_name
    elif ultroid_bot.me.last_name:
        DEFAULTUSER = last_name
    else:
        DEFAULTUSER = ''
    udB.set("OLDNAME", DEFAULTUSER)
    udB.set("AUTONAME", "True")
    await eor(ult, "Auto Name has been started Master")
    while True:
        if udB.get("TIMEZONE") is not None:
            tym = datetime.now(timezone(udB.get("TIMEZONE")))
        else:
            tym = datetime.now(timezone('Asia/Kolkata'))
        ge = udB.get("AUTONAME")
        if not ge == "True":
            return
        DMY = tym.strftime("%d.%m.%Y")
        HM = tym.strftime("%H:%M")
        Naam = udB.get("OLDNAME")
        name = f"⌚{HM} 🔥{Naam}🔥 📅{DMY}"
        try:
            await ultroid_bot(UpdateProfileRequest(
                first_name=name
            ))
        except FloodWaitError as ex:
            await asst.send_message(
                Var.LOG_CHANNEL,
                f"Floodwait of {ex.seconds}.",
            )
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(60)


@ultroid_cmd(pattern="stopname")
async def stoppo(ult):
    name = udB.get("OLDNAME")
    gt = udB.get("AUTONAME")
    await ultroid_bot(UpdateProfileRequest(
        first_name=name))
    if not gt == "True":
        return await eor(ult, "AUTONAME was not in use !!")
    udB.set("AUTONAME", "False")
    await eor(ult, "AUTONAME Stopped !!")
