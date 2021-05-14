
"""
✘ Commands Available

• `{i}autocorrect`
    To on/off Autocorrect Feature.

"""

from gingerit.gingerit import GingerIt
from googletrans import Translator
from telethon import events

from . import *

tr = Translator()


@infinato_cmd(pattern="autocorrect")
async def acc(e):
    if not is_fullsudo(ult.sender_id):
        return await eod(ult, "`This Command Is Sudo Restricted.`")
    if Redis("AUTOCORRECT") != "True":
        udB.set("AUTOCORRECT", "True")
        await eod(e, "AUTOCORRECT Feature On")
    else:
        udB.delete("AUTOCORRECT")
        await eof(e, "AUTOCORRECT Feature Off")


@infinato_bot.on(events.NewMessage(outgoing=True))
async def gramme(event):
    if Redis("AUTOCORRECT") != "True":
        return
    t = event.text
    tt = tr.translate(t)
    if t.startswith((HNDLR, ".", "?", "#", "_", "*", "'", "@", "[", "(", "+")):
        return
    if t.endswith(".."):
        return
    if tt.src != "en":
        return
    xx = GingerIt()
    x = xx.parse(t)
    res = x["result"]
    try:
        await event.edit(res)
    except BaseException:
        pass


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})