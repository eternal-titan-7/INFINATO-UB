from telethon import events
import asyncio


@ultroid_cmd(pattern="imsorry (.*)")
async def _(event):
    if event.fwd_from:
        return
    num = int(event.pattern_match.group(1))
    animation_interval = 1
    await event.edit("`INFINATO Starting...`")
    animation_chars = [
        "I'M SORRY ❤️",
        "❤️❤️❤️❤️❤️️"
    ]
    for i in range(num):
        for j in animation_chars:
            await asyncio.sleep(animation_interval)
            await event.edit(j)
