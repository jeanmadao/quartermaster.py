from discord.ext import commands, tasks

import datetime
from cogs.utils.date import isweekday
from zoneinfo import ZoneInfo

brussels_tz = ZoneInfo("Europe/Brussels")
checkin_times = [
        datetime.time(hour=8, minute=46, tzinfo=brussels_tz),
        datetime.time(hour=13, minute=16, tzinfo=brussels_tz),
        ]
checkout_times = [
        datetime.time(hour=12, minute=30, tzinfo=brussels_tz),
        datetime.time(hour=17, minute=0, tzinfo=brussels_tz),
        ]

class Attendance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.checkin_announcement.start()
        self.checkout_announcement.start()

    @tasks.loop(time=checkin_times)
    async def checkin_announcement(self):
        if isweekday(datetime.date.today()):
            if self.bot.maintenance:
                await self.bot.maintenance_channel.send("Don't forget to check in!")
            else:
                await self.bot.announcement_channel.send("Don't forget to check in!")

    @tasks.loop(time=checkout_times)
    async def checkout_announcement(self):
        if isweekday(datetime.date.today()):
            if self.bot.maintenance:
                await self.bot.maintenance_channel.send("Don't forget to check out!")
            else:
                await self.bot.announcement_channel.send("Don't forget to check out!")

async def setup(bot):
    await bot.add_cog(Attendance(bot))
