import discord
from discord.ext import commands

class TestCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(description='Command for the bot to say hi to you.')
  async def sayhi(self, ctx):
    await ctx.send(f'Hi, {ctx.author.name}!')

def setup(bot):
    bot.add_cog(TestCommands(bot))