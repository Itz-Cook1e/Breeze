# Import libraries
import discord
from discord.ext import commands

# Create class to define bot and load it in as a cog
class AutoMod(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

    
# No command yet :(
    

# Load up as a cog
def setup(bot):
    bot.add_cog(AutoMod(bot))
