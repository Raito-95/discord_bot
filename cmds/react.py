import discord
import random
import json
from discord.ext import commands
from core.classes import Cog_Extensoin

with open('setting.json', 'r', encoding='utf8') as j_file:
    j_data = json.load(j_file)

class React(Cog_Extensoin):
    @commands.command()
    async def image(self, ctx):
        random_pic = random.choice(j_data["local_image"])
        pic = discord.File(random_pic)
        await ctx.send(File=pic)

    @commands.command()
    async def web(self, ctx):
        random_pic = random.choice(j_data["url_image"])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React())