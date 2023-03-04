import json
import discord
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', 'r', encoding='utf8') as j_file:
    j_data = json.load(j_file)


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(j_data["general_channel"]))
        await channel.send(f'{member} join')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(j_data["general_channel"]))
        await channel.send(f'{member} leave')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.context == 'apple' and msg.author != self.bot.user:
            await msg.channel.send('apple')


def setup(bot):
    bot.add_cog(Event(bot))
