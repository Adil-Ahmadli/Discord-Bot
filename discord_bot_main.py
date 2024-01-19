from discord.ext import commands
from apikeys import BOTTOKEN

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("The Bot is ready!")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am a bot!")

client.run(BOTTOKEN)