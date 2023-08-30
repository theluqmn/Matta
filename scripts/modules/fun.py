import discord
from discord.ext.commands import Cog
from discord import Option
from scripts.embeds import fun as Embeds

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(
        name= "calculator",
        description= "A simple calculator"
    )
    async def calculator(
        self, ctx,
        operation: Option(str, description= "+, -, * or /"),
        num1: Option(str, description= "First number?"),
        num2: Option(str, description= "Second number?")
    ):
        #   Operation
        if operation == "+":
            #   Addition
            await ctx.respond(embed= Embeds.addition(num1, num2))
        
        elif operation == "-":
            #   Subtraction
            await ctx.respond(embed= Embeds.subtraction(num1, num2))
        
        elif operation == "*":
            #   Multiplication
            await ctx.respond(embed= Embeds.multiplication(num1, num2))
        
        elif operation == "/":
            #   Division
            await ctx.respond(embed= Embeds.division(num1, num2))

        else:
            #   No match
            await ctx.respond(embed= Embeds.not_found(num1, num2))
    
#   Cog setup
def setup(bot):
    bot.add_cog(Fun(bot))