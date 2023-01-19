import os
import json
import discord
from discord.ext import commands


with open('setting.json', 'r', encoding='utf8') as j_file:
    j_data = json.load(j_file)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


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

@bot.commands()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done')

@bot.commands()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done')

@bot.commands()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

bot.run(j_data["TOKEN"])
