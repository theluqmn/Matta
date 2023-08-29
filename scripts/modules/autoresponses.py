import discord, random, json
from discord import Option, Embed
from discord.ext import commands
from discord.ext.commands import Cog

#   Getting the saved autoresponses
with open("data/responses.json", "r") as file:
    autoresponses = json.load(file)
    print(autoresponses)

#   Main class
class AutoResponder(Cog):
    def __init__(self, bot):
        self.bot = bot

        autoresponder = bot.create_group(
            "autoresponder",
            "View and manage autoresponders in this server."
        )


        #   Add new autoresponder
        @autoresponder.command(description= "Add a new autoresponder")
        async def add(
            ctx,
            responder_name: Option(str, "A unique name for the autoresponder", required= True),
            triggers: Option(str, "Words that trigger the autoresponder, separated with commas.", required= True),
            responses: Option(str, "A list of responses, seperated by commas.", required= True)
        ):
            
            #   Converting inputs into a list
            triggersList = triggers.split(",")
            responseList = responses.split(",")
            triggersList = [word.strip() for word in triggersList]
            responseList = [word.strip() for word in responseList]
            autoresponses[str(ctx.guild.id)] = {responder_name: {"enabled": True, "triggers": triggersList, "responses": responseList}}


            #   Saving the dictionary to JSON
            with open("data/responses.json", "w") as file:
                json.dump(autoresponses, file)

            #   Respond
            await ctx.respond(
                embed = Embed(
                description= f"""
                    **Name:**
                    > {responder_name}

                    **Triggers:**
                    > {triggersList}

                    **Responses:**
                    > {responseList}
                    """)
                .set_author(name= "Successfully created new autoresponder")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
                )
        

        #   Toggle autoresponder
        @autoresponder.command(description= "Toggle an autoresponder")
        async def toggle(
            ctx,
            responder_name: Option(str, "The name of autoresponder", required=True)
        ):
            #   Check if enable
            if autoresponses[str(ctx.guild.id)][responder_name]["enabled"] == False:
                autoresponses[str(ctx.guild.id)][responder_name]["enabled"] = True
            else:
                autoresponses[str(ctx.guild.id)][responder_name]["enabled"] = False
            
            #   Respond
            await ctx.respond(
                    embed = Embed(
                    description= f"""
                        **Name:**
                        {responder_name}

                        **State:**
                        {autoresponses[str(ctx.guild.id)][responder_name]["enabled"]}
                        """)
                    .set_author(name= "Successfully toggled autoresponder")
                )

        #   Edit an autoresponder
        @autoresponder.command(description= "Edit an existing autoresponder")
        async def edit(
            ctx,
            responder_name: Option(str, "Autoresponder name", required= True),
            triggers: Option(str, "Words that trigger the autoresponder, separated with commas.", required= True),
            responses: Option(str, "A list of responses, seperated by commas.", required= True)
        ):
            
            #   Converting inputs into a list
            triggersList = triggers.split(",")
            responseList = responses.split(",")
            triggersList = [word.strip() for word in triggersList]
            responseList = [word.strip() for word in responseList]

            #   Saving the dictionary to JSON
            with open("data/responses.json", "w") as file:
                json.dump(autoresponses, file)

            #   Respond
            await ctx.respond(
                embed = Embed(
                description= f"""
                    **Name:**
                    > {responder_name}

                    **Triggers:**
                    > {triggersList}

                    **Responses:**
                    > {responseList}
                    """)
                .set_author(name= "Successfully edited autoresponder")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
                )
            
        #   Delete an autoresponder
        @autoresponder.command(description = "Delete an autoresponder in this server")
        async def delete(
            ctx,
            responder_name: Option(str, "Autoresponder name", required= True)
        ):
            
            del autoresponses[str(ctx.guild.id)][responder_name]

            await ctx.respond(
                embed = Embed(
                description=  f"""
                    **Name:**
                    > {responder_name}
                    """)
                .set_author(name= "Successfully deleted autoresponder")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
                )

    #   Message responder
    @discord.Cog.listener()
    async def on_message(self,message):
        message_unfilt = message.content

        #A couple of changes so it's readable
        unwanted_chars = ["'", "!", ",", "?", " "]
        message.content = "".join([char for char in message.content if char not in unwanted_chars])
        message.content = message.content.lower()

        if not message.author == self.bot.user:
            #   Automated responder using 
            for guild in autoresponses:
                #   Looking for responders in guild
                for responder in autoresponses[guild]:
                    #   Only proceeding if enabled
                    if autoresponses[guild][responder]["enabled"] == True:
                        if message.content in autoresponses[guild][responder]["triggers"]:

                            if len(autoresponses[guild][responder]["responses"]) > 1:
                                #   If multiple, then randomly select for response
                                await message.channel.send(random.choice(autoresponses[guild][responder]["responses"]))
                            else:
                                #   If only single response item
                                await message.channel.send(autoresponses[guild][responder]["responses"][0])

#   Cog setup
def setup(bot):
    bot.add_cog(AutoResponder(bot))