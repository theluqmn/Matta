import discord
from discord import Option
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ui import Select

#   Main class
class Help(Cog):
    def __init__(self, bot):
        self.bot = bot

    #   The command
    @discord.slash_command(
        name= "help",
        description= "Overview of commands and modules."
    )
    async def help(
        self, ctx
    ):
        #   Loading up the embeds
        from scripts.embeds import help as Embeds
        embed = Embeds.home()

        #   Selection setup
        select = Select(
            placeholder= "Select a category",
            options= [
                discord.SelectOption(label= "Home", emoji= "🏠"),
                discord.SelectOption(label= "Autoresponder", emoji="💬"),
                discord.SelectOption(label= "Moderation", emoji= "⚒️")
            ]
        )

        #   View
        class View(discord.ui.View):
            async def on_timeout(self):
                self.disable_all_items()
        
        view = View(timeout=0)

        #   Interactions
        async def response(interaction):
            if select.values[0] == "Home":
                #   Home
                embed = Embeds.home()
                await interaction.response.edit_message(embed= embed)
            
            if select.values[0] == "Autoresponder":
                #   Autoresponder
                embed = Embeds.autoresponder()
                await interaction.response.edit_message(embed= embed)
            
            if select.values[0] == "Moderation":
                #   Moderation
                embed = Embeds.moderation()
                await interaction.response.edit_message(embed= embed)

            else:
                pass
            
        #   Default message
        select.callback = response
        view.add_item(select)

        await ctx.respond(embed= embed, view= view)

#   Cog setup
def setup(bot):
    bot.add_cog(Help(bot))