import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
TOKEN = os.environ.get("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print('起動しました！(\'◇\')ゞ')
@bot.command()
async ping(ctx):

bot.run(TOKEN)
