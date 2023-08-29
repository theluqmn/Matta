from discord import Embed

#   Embeds

def home():
    embed = Embed(
        description= """
        Måtta is an open-sourced Discord bot made by luqmanity and several
        other contributors, using `pycord` (a fork of discord.py).
        This bot also uses cogs, command groups, and discord views and UI.
        It is recommended to at least have some experience with working on
        Discord bots, and pycord, if you would like to contribute to the
        project. 
    
        **You are allowed to repurpose/reuse this bot's source code, refer to the GitHub.**

        Join the Nytra Discord for support/etc:
        > https://discord.gg/7w8b6MMXBy
        
        This project's GitHub repo:
        > https://github.com/luqmanity/matta
        
        **Use the menu below to navigate between different modules/functions!**"""
    )
    embed.set_author(name= "Help - Home")
    embed.set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")

    return embed

def autoresponder():
    embed = Embed(
        description= """
            The autoresponder module allows servers to have custom autoresponders.

            `autoresponder add`
            > Creates a new autoresponder for this server
            > Requires the `responderName`, `triggers` and `responses` arguments.
            
            `autoresponder toggle`
            > Enables/Disables an autoresponder.
            
            `autoresponder edit`
            > Edits an autoresponder
            > Note that this command will overwrite any existing values of the autoresponder.
            
            `autoresponder delete`
            > Deletes an autoresponder
            > **Irreversible action**. """
    )

    embed.set_author(name= "Help - Autoresponder")
    embed.set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
    
    return embed

def tools():
    embed = Embed(
        description= """
            (Usefull?) tools for your server.
            
            `ping`
            > Pings the bot, then returns the latency.
            
            `membercount`
            > Responds with the membercount of this server."""
    )
    embed.set_author(name= "Help - Tools")
    embed.set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")

    return embed

def moderation():
    embed = Embed(
        description= """
            The moderation module does things mods do. real.
            Note that **only administrators** have access to this module for now.
            
            `ban`
            > Bans a member of the server
            
            `kick`
            > Kicks a member of the server
            
            `timeout`
            > Time-outs a member of the server
            > Takes arguments such as days, hours, minutes, seconds - but is optional.
            
            `unmute`
            > Gets rid of a member's timeout.
            > Temporary command name, it will be part of the timeout subground soon."""
    )
    embed.set_author(name= "Help - Moderation")
    embed.set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")

    return embed