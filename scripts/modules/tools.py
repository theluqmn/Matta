import discord
from discord import Option, Embed
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

    
def setup(bot):
    bot.add_cog(Tools(bot))