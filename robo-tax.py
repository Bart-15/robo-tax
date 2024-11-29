from dotenv import load_dotenv
import os
import discord
from discord.ext import commands


# Load the .env file
load_dotenv()

# Access variables
bot_token = os.getenv("DISCORD_BOT_TOKEN")


# bot instance
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

@bot.command(name='robux')
async def calculateRobux(ctx, amount: str):
  try:
    amount = int(amount)
    after_tax = amount * (1 - 0.3)
    print(ctx)
    await ctx.reply(f"The total after a 30% tax deduction is: {after_tax:,.0f} Robux")
  except ValueError:
    await ctx.reply("Please enter a valid number for the amount of Robux")


bot.run(bot_token)