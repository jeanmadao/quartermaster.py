import discord
import asyncio
import logging
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("TOKEN")
MAINTENANCE_CHANNEL = os.getenv("MAINTENANCE_CHANNEL")
ANNOUNCEMENT_CHANNEL = os.getenv("ANNOUNCEMENT_CHANNEL")
FEED_CHANNEL = os.getenv("FEED_CHANNEL")
MAINTENANCE = os.getenv("MAINTENANCE")

extensions = (
        "cogs.time",
        "cogs.feed",
        )

log = logging.getLogger(__name__)

class QuarterMaster(commands.Bot):
    def __init__(self):
        intents = discord.Intents(
                messages=True,
                message_content=True
                )
        super().__init__(
                command_prefix='!',
                intents=intents
                )

    async def setup_hook(self):
        try:
            if MAINTENANCE_CHANNEL and ANNOUNCEMENT_CHANNEL and FEED_CHANNEL and MAINTENANCE:
                self.maintenance_channel = await self.fetch_channel(int(MAINTENANCE_CHANNEL))
                self.announcement_channel = await self.fetch_channel(int(ANNOUNCEMENT_CHANNEL))
                self.feed_channel = await self.fetch_channel(int(FEED_CHANNEL))
                self.maintenance = eval(MAINTENANCE)
        except Exception:
            log.exception(f'Failed to load channels.')

        for extension in extensions:
            try:
                await self.load_extension(extension)
            except Exception:
                log.exception(f'Failed to load extension {extension}.')

def main():
    bot = QuarterMaster()
    if TOKEN:
        asyncio.run(bot.start(TOKEN))

if __name__ == '__main__':
    main()
