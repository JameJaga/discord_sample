# coding: UTF-8
import re
import discord
from discord.ext import commands
import os
import cogs.ping as ping
import cogs.counter as counter
imporrt cogs.name as name

@bot.event
async def on_ready():
    pint.setup(bot)
    counter.setup(bot)
    name.setup(bot)
    print('起動しました！(\'◇\')ゞ')
@bot.command()
async ping(ctx):
    await ctx.send('pong!')

bot.run(TOKEN)
