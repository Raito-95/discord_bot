import discord
import json
import random
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', 'r', encoding='utf8') as j_file:
    j_data = json.load(j_file)


class React(Cog_Extension):

    @commands.command()
    async def image(self, ctx):
        random_image = random.choice(j_data["local_image"])
        picture = discord.File(random_image)
        await ctx.send(file=picture)

    @commands.command()
    async def web_image(self, ctx):
        random_image = random.choice(j_data["web_image"])
        await ctx.send(random_image)


def setup(bot):
    bot.add_cog(React(bot))
