import discord, os, time, json
from dotenv import load_dotenv, set_key
from discord.ext import commands
from pathlib import Path
from config import setup
os.system("cls")

print("""
Måtta Discord Bot

If you're facing any problems, please post an issue
on the GitHub repo, and/or alert us in the
Discord server.

GitHub repo: 
- https://github.com/luqmanity/matta

Nytra Discord server:
- https://discord.gg/7w8b6MMXBy\n""")

load_dotenv("data/.env") # Loading the .env

#   Required files exists
print("Required files exists. Deploying bot...\n")
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
                name="Hej då! /help"
            )
        )

        #   Checking how long to run
        startup_duration = round(time.time() - startup_time, 4)
        print(f"{bot.user} is online, took {startup_duration}s\n")

    # Cogs
    bot.load_extension("scripts.modules.autoresponses")
    bot.load_extension("scripts.modules.tools")
    bot.load_extension("scripts.modules.moderation")
    bot.load_extension("scripts.modules.help")

    # Cooldown Management
    @bot.event
    async def on_application_command_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)
        else:
            raise error

    bot.run(TOKEN)