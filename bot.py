# coding: UTF-8
import re
import discord
from discord.ext import commands
import os

@bot.event
async def on_ready():
    print('起動しました！(\'◇\')ゞ')
    print(values)
@bot.command()
async ping(ctx):
    await ctx.send('pong!')

bot.run(TOKEN)
