import discord
from discord import ApplicationContext, Option, Embed
from discord.ext import commands
from discord.ext.commands import Cog

#   Main Class
class Tools(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #   Ping
    @discord.slash_command(
        name= "ping",
        description= "Ping the server and returns latency."
    )
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)

        await ctx.respond(
            embed= Embed(
            description= f"""
                Latency:
                > {latency}ms"""
            )
            .set_author(name= "Pong!")
            .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
        )

        print(f"Bot pinged. Latency: {latency}ms")
    
    #   Membercount
    @discord.slash_command(
        name= "membercount",
        description= "Membercount of the server"
    )
    async def membercount(self, ctx):
        await ctx.respond(
            embed= Embed(
            description= f"""
                Membercount:
                > {ctx.guild.member_count}"""
            )
            .set_author(name= f"Membercount of {ctx.guild.name}")
        )
        
    @discord.slash_command(
        name= "calc",
        description= "Do math"
    )
    async def calculate(
        self,
        ctx: ApplicationContext,
        num1: Option(str),
        operation: Option(str, choices=["+", "-", "*", "/"]),
        num2: Option(str),
    ):
        if operation not in ["+", "-", "*", "/"]:
            await ctx.respond("Please type a valid operation type.")
        else:
            var = f"{num1} {operation} {num2}"
            await ctx.respond(f"{var} = {eval(var)}")


    
def setup(bot):
    bot.add_cog(Tools(bot))
