# Import libraries
import discord
from discord.ext import commands
from config import bot_token

# Get intents to do kool things with data
intents = discord.Intents.default()
intents.members = True

# Define bot as client
client = commands.Bot(command_prefix="Breeze ", intents = intents)

# on_ready event (what do do when bot starts)
@client.event
async def on_ready():
    print('Breeze now online!')
    await client.change_presence(activity=discord.Game(name='on Discord'))

# Remove help command
client.help_command = None

# Make Help Command Look Smexy
@client.command()
async def help(ctx):
    await ctx.send(file=discord.File(r'help.mp4'))

# Define cog files
cogs = ['automod', 'admin', 'chat-link', 'tests']

# Load cogs above
try:
    for cog in cogs:
        client.load_extension(f'cogs.{cog}')
        print(f'Loaded: {cog}.')
except Exception as e:
    print(f'Error loading {cog}: {e}')

# Run the bot
client.run(bot_token)
