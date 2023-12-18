import discord
import requests
from discord.ext import commands as cmd

intents = discord.intents.default()
intents.message_content = True

bot = cmd.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


def getToken():
    authToken = requests.get('http://127.0.0.1:5000/')


@bot.event
@bot.command(name='hello')
async def onMessage(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message) or message.content.startswith('!hello'):
        await message.channel.send(f"Hello World")

    await bot.process_commands(message)
