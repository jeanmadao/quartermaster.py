from discord.ext import commands, tasks
import feedparser
import time
from datetime import datetime
from cogs.utils.time import calculate_delta_hours

SOURCES = (
        "https://news.ycombinator.com/rss",
        )

RSS_REFRESH_TIME = 12
SEND_ARTICLE_COOLDOWN = 30

class Feed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rss_queue = []
        self.update_queue.start()
        self.send_article.start()

    @tasks.loop(hours=RSS_REFRESH_TIME)
    async def update_queue(self):
        for source in SOURCES:
            d = feedparser.parse(source)
            for entry in d.entries:
                delta_hours = calculate_delta_hours(time.time() - 3600, time.mktime(entry.published_parsed))
                if delta_hours <= RSS_REFRESH_TIME :
                    self.rss_queue.append(entry.link)

    @tasks.loop(minutes=SEND_ARTICLE_COOLDOWN)
    async def send_article(self):
        if 8 <= datetime.today().hour <= 20:
            article = self.rss_queue.pop(0)
            if self.bot.maintenance:
                await self.bot.maintenance_channel.send(article)
            else:
                await self.bot.feed_channel.send(article)


async def setup(bot):
    await bot.add_cog(Feed(bot))
