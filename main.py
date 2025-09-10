import discord
from discord.ext import commands
import os

# Set up the bot with a prefix (example: !ping)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Run the bot using the TOKEN from Railway Variables
bot.run(os.getenv("TOKEN"))
