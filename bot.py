import os
import discord
from discord.ext import commands

import cogs.mcount as mcount

bot = commands.Bot(command_prefix='!')
TOKEN = os.environ.get("DISCORD_TOKEN")

@bot.event
async def on_ready():
    mcount.setup(bot)
    print('起動しました！(\'◇\')ゞ')
    
@bot.command()
async ping(ctx):
    await ctx.send('pong!')

bot.run(TOKEN)
