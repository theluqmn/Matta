import discord, os, time, json
from dotenv import load_dotenv, set_key
from discord.ext import commands
from pathlib import Path
from config import setup

print("""
Måtta Discord Bot

GitHub repo: 
- https://github.com/luqmanity/matta

Nytra Discord server:
- https://discord.gg/7w8b6MMXBy\n""")

load_dotenv("data/.env") # Loading the .env

#   Required files exists
print("Required files exists. Deploying bot...")
TOKEN = str(os.getenv("token"))

if __name__ == "__main__":
    bot = discord.Bot(
        intents=discord.Intents.all()
    )

    # Startup configs
    startup_time = time.time()

    @bot.event
    async def on_ready():

        #   Setting the bot RPC
        await bot.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                ame="Hej då! /help"
            )
        )

        #   Checking how long to run
        startup_duration = round(time.time() - startup_time, 4)
        print(f"{bot.user} is online, took {startup_duration}s")

    # Cogs
    bot.load_extension("src.modules.autoresponses")
    bot.load_extension("src.modules.tools")
    bot.load_extension("src.modules.moderation")

    # Cooldown Management
    @bot.event
    async def on_application_command_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)
        else:
            raise error

    bot.run(TOKEN)