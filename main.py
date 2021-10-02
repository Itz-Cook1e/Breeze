# Import libraries
import discord
from discord.ext import commands

# Define bot as client
client = commands.Bot(command_prefix="Breeze ")

# Remove ehhhh help command so I can make custom one later
client.remove_command("help")

# on_ready event (what do do when bot starts)
@client.event
async def on_ready():
    print('Breeze now online!')
    await client.change_presence(activity=discord.Game(name='on Discord'))

# Define cog files
cogs = ['automod']

# Load cog file(s) above
try:
    for cog in cogs:
        client.load_extension(f'cogs.{cog}')
        print(f'Loaded: {cog}.')
except Exception as e:
    print(f'Error loading {cog}: {e}')

# Run the bot
client.run("token")
