import random
import os
from discord.ext import commands
from core.classes import Cog_Extensoin

url_image = os.environ['url_image']


class React(Cog_Extensoin):
    # @commands.command()
    # async def image(self, ctx):
    #     random_pic = random.choice(url_image)
    #     pic = discord.File(random_pic)
    #     await ctx.send(File=pic)

    @commands.command()
    async def web(self, ctx):
        random_pic = random.choice(url_image)
        await ctx.send(random_pic)


def setup(bot):
    bot.add_cog(React())
