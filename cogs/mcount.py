import discord
from discord.ext import commands

class mcount(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        guild = message.guild   
        member_count = guild.member_count  
        user_count = sum(1 for member in guild.members if not member.bot)  
        bot_count = sum(1 for member in guild.members if member.bot)  
        category = discord.utils.get(guild.category, name='counter') 
        
      

def setup(bot):
    bot.add_cog(mcount(bot))
