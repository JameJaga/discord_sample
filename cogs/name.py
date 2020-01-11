import discord
import re
from discord.ext import commands

class ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        guild = message.guild
        member_count = guild.member_count  
        name = guild.name
        name = re.split('-', name)[0]
        payload = f"{name} + {str(member_count)} members."
        await guild.edit(name=payload) 

def setup(bot):
    bot.add_cog(ping(bot))

