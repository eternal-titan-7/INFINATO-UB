
from datetime import datetime
from . import *

@asst_cmd("ping")
@owner
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await asst.send_message(
        event.chat_id,
        f"🏓**Pong!!**\n `{ms}ms`\n\n**My Master** - [{OWNER_NAME}](tg://user?id={OWNER_ID})",
    )
