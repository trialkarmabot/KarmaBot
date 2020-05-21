"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`Baithe baithe hue boreâ€¦..Karna hai Kuch kaam Shuru kro yeh userbot leke prabhu ka naam Ïˆ(ï½€âˆ‡Â´)Ïˆ`**\n\n"
                      "**Telethon version:- 6.9.0**\nâ—† â–¬â–¬â–¬â–¬â–¬â–¬ â´âœªâµ â–¬â–¬â–¬â–¬â–¬â–¬ â—†\n**Python: 3.7.3**\nâ—† â–¬â–¬â–¬â–¬â–¬â–¬ â´âœªâµ â–¬â–¬â–¬â–¬â–¬â–¬ â—†\n"
                    f"`My Peru Owner`: {DEFAULTUSER}\nâ—† â–¬â–¬â–¬â–¬â–¬â–¬ â´âœªâµ â–¬â–¬â–¬â–¬â–¬â–¬ â—†\n"
                     "**Database Status: Databases functioning normally!**\nâ—† â–¬â–¬â–¬â–¬â–¬â–¬ â´âœªâµ â–¬â–¬â–¬â–¬â–¬â–¬ â—†\nAlways with you, my peru master!\n`"
                    "**Bot Created By:- @KarmaHacx\n**"
                    
                     "[Deploy this userbot Now](https://github.com/Karma-goku/KarmaBot)")
