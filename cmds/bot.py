from discord.ext import commands
from core.classes import Cog_Extensoin


class Bot(Cog_Extensoin):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000) }ms')


def setup(bot):
    bot.add_cog(Bot())
