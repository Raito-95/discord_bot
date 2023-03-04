import discord
from discord.ext import commands
import json
import os

with open('setting.json', 'r', encoding='utf8') as j_file:
    j_data = json.load(j_file)

bot = commands.Bot(intents=discord.Intents.default(), command_prefix='!')


@bot.event
async def on_ready():
    print('Bot is online')


@commands.command
async def load(ctx, extension):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')


@commands.command
async def reload(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'UnLoaded {extension} done.')


@commands.command
async def unload(ctx, extension):
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'ReLoaded {extension} done.')


async def load_extensions():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(j_data["PUBLIC_TOKEN"])
