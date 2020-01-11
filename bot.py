# coding: UTF-8
import re
import discord
import random
from discord.ext import commands
import os
import asyncio
import asyncpg
from yarl import URL
import pandas as pd

#データベース
dburl = URL(os.environ.get("DATABASE_URL"))
host = dburl.host
user = dburl.user
database = dburl.path[1:]
port = dburl.port
password = dburl.password
print('host = ' + str(host))
print('user = ' + str(user))
print('database = ' + str(database))
print('port = ' + str(port))
print('password = ' + str(password))

bot = commands.Bot(command_prefix='!')
TOKEN = os.environ.get("DISCORD_TOKEN")

conn = await asyncpg.connect(host = host ,user = user, database = database, port = port, password = password)
values = await conn.fetch(f'SELECT * ')
@bot.event
async def on_ready():
    print('起動しました！(\'◇\')ゞ')
    print(values)
@bot.command()
async ping(ctx):
    await ctx.send('pong!')

bot.run(TOKEN)
