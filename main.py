import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utf8') as j_file:
    j_data = json.load(j_file)

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Bot is online')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(j_data["general_channel"]))
    await channel.send(f'{member} join')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(j_data["general_channel"]))
    await channel.send(f'{member} leave')


@bot.event
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)} ms')


@bot.event
async def image(ctx):
    picture = discord.File(j_data["test_image"])
    await ctx.send(file=picture)


bot.run(j_data["TOKEN"])
