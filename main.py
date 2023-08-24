import discord, os, time
from dotenv import load_dotenv
from discord.ext import commands

if not os.path.exists(".env"):
    print("Missing required .env token file.")

else:

    load_dotenv() # Loading the .env

    if __name__ == "__main__":
        TOKEN = str(os.getenv("token"))

        bot = discord.Bot(
            intents= discord.Intents.all()
        )

        #   Startup configs 
        startup_time = time.time()

        @bot.event
        async def on_ready():
            await bot.change_presence(
                status= discord.Status.do_not_disturb,
                activity= discord.Activity(
                    type= discord.ActivityType.playing,
                    name= "Hej då! /help"
                )
            )

            startup_duration = round(time.time() - startup_time, 4)
            print(f"{bot.user} is online, took {startup_duration}s")
        
        #   Cogs
        bot.load_extension("src.modules.autoresponses")
        bot.load_extension("src.modules.tools")
        bot.load_extension("src.modules.moderation")

        #   Cooldown Management
        @bot.event
        async def on_application_command_error(ctx, error):
            if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(error)
            else:
                raise error

        bot.run(TOKEN)