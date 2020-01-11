import discord
from discord.ext import commands

class counter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def count(self,ctx,arg): 
        guild = ctx.guild   
        if arg == 'all':
            member_count = guild.member_count  
            await ctx.send(f'メンバー数：{member_count}')   
        elif arg == 'user':
            user_count = sum(1 for member in guild.members if not member.bot)  
            await ctx.send(f'ユーザ数：{user_count}')  
        elif arg == 'bot':
            bot_count = sum(1 for member in guild.members if member.bot)  
            await ctx.send(f'BOT数：{bot_count}')  

def setup(bot):
    bot.add_cog(counter(bot))
