import os
import discord
from discord.ext import commands

TOKEN = os.environ['TOKEN']
DryTalk_ch = os.environ['DryTalk_ch']

intents = discord.Intents.default()
intents.messages = True
intents.members = True
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('Hello!'):
        await message.channel.send('Hello!')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(DryTalk_ch))
    await channel.send(f'{member} join')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(DryTalk_ch))
    await channel.send(f'{member} leave')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done')


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done')


# for filename in os.listdir('./cmds'):
#     if filename.endswith('.py'):
#         bot.load_extension(f'cmds.{filename[:-3]}')

try:
    bot.run(TOKEN)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests.\r\n"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
        os.system("kill 1")
    else:
        raise e
