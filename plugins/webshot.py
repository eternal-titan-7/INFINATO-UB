
"""
✘ Commands Available -

• `{i}webshot <url>`
    Get a screenshot of the webpage.

"""

import requests

from . import *


@infinato_cmd(pattern="webshot")
async def webss(event):
    xx = await eor(event, get_string("com_1"))
    mssg = event.text.split(" ", maxsplit=2)
    try:
        xurl = mssg[1]
    except IndexError:
        return await eod(xx, "`Give a URL please!`", time=5)
    try:
        requests.get(xurl)
    except requests.ConnectionError:
        return await eod(xx, "Invalid URL!", time=5)
    except requests.exceptions.MissingSchema:
        try:
            r = requests.get("https://" + xurl)
        except requests.ConnectionError:
            try:
                r2 = requests.get("http://" + xurl)
            except requests.ConnectionError:
                return await eod(xx, "Invalid URL!", time=5)

    lnk = f"https://shot.screenshotapi.net/screenshot?url={xurl}"
    ok = requests.get(lnk).json()
    try:
        sshot = ok["screenshot"]
    except BaseException:
        return await eod(xx, "Something Went Wrong :(", time=10)
    await xx.reply(
        f"**WebShot Generated**\n**URL**: {xurl}",
        file=sshot,
        link_preview=False,
        force_document=True,
    )
    await xx.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
