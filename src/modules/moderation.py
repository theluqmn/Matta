import discord
from discord import Option, Embed
from datetime import timedelta
from discord.ext import commands
from discord.ext.commands import MissingPermissions, Cog

class Moderation(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #   Ban
    @discord.slash_command(
        name= "ban",
        description= "Bans a user in the server"
    )
    @commands.has_permissions(
        ban_members = True,
        administrator = True
    )
    async def ban(
        self, ctx,
        member: Option(discord.Member, description= "Specify user to ban"),
        reason: Option(str, description= "Reason for ban", required= False)
    ):
        #   Banning the author itself
        if member.id == ctx.author.id:
            await ctx.respond(
                embed= Embed(
                description= f"""
                    You can't ban **yourself** lol"""
                )
                .set_author(name= "Ban Command Failed")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )
        
        #   Banning another admin
        elif member.guild_permissions.administrator:
            await ctx.respond(
                embed= Embed(
                description= f"""
                    Don't even try to ban an admin lmao"""
                )
                .set_author(name= "Ban Command Failed")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )

        #   Ban authorised
        else:
            if reason == None:
                reason = "None provided"
            
            await member.ban(reason= reason)
            await ctx.respond(
                embed= Embed(
                description= f"""
                    **Member banned:**
                    > <@{member.id}>

                    **Banned by:**
                    > <@{ctx.author.id}>

                    **Reason:**
                    > {reason}"""
                )
                .set_author(name= "Ban Successful")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )
    
    @ban.error
    async def banerror(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond(
                embed= Embed(
                description= "Missing permissions to execute command"
                )
                .set_author(name= "Ban Unauthorised")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )
        else:
            await ctx.respond(
                embed= Embed(
                description= "Something went wrong"
                )
                .set_author(name= "Ban Command Failed")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )
            

    
    #   Kick
    @discord.slash_command(
        name= "kick",
        description= "Kicks a user in the server"
    )
    @commands.has_permissions(
        kick_members = True,
        administrator= True
    )
    async def kick(
        self, ctx,
        member: Option(discord.Member, "Specify a user to kick", required= True),
        reason: Option(str, "Reason for kick", required= False)
    ):
        #   Kicking the author itself
        if member.id == ctx.author.id:
            await ctx.respond(
                embed= Embed(
                description= f"""
                You can't kick **yourself** lol"""
                )
                .set_author(name= "Kick Command Failed")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )
        
        #   Kicking an admin
        elif member.guild_permissions.administrator:
            await ctx.respond(
                embed= Embed(
                description= f"""
                    Don't even try to kick an admin lmao"""
                )
                .set_author(name= "Kick Command Failed")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )
        
        #   Kick authorised
        else:
            if reason == None:
                reason = "None provided"
            
            await member.kick(reason= reason)
            await ctx.respond(
                embed= Embed(
                description= f"""
                    **Member banned:**
                    > <@{member.id}>

                    **Kicked by:**
                    > <@{ctx.author.id}>

                    **Reason:**
                    > {reason}"""
                )
                .set_author(name= "Ban Successful")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )

    @kick.error
    async def kickerror(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond(
                embed= Embed(
                description= "Missing permissions to execute command"
                )
                .set_author(name= "Kick Unauthorised")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )
        else:
            await ctx.respond(
                embed= Embed(
                description= "Something went wrong"
                )
                .set_author(name= "Kick Command Failed")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )



    #   Timeout
    @discord.slash_command(
        name= "timeout",
        description= "Time out a user in this server"
    )
    @commands.has_permissions(
        administrator = True
    )
    async def timeout(
        self, ctx,
        member: Option(discord.Member, "Specify a member to timeout", required= True),
        reason: Option(str, "Reason for timeout", required= False),
        days: Option(int, max_value= 30, required = False),
        hours: Option(int, required= False),
        minutes: Option(int, required= False),
        seconds: Option(int, required= False)
    ):
        #   Timeout author
        if member.id == ctx.author.id:
            await ctx.respond(
                embed= Embed(
                description= f"""
                You can't timeout **yourself** lol"""
                )
                .set_author(name= "Timeout Command Failed")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )

        #   Timeout admin
        elif member.guild_permissions.administrator:
            await ctx.respond(
                embed= Embed(
                description= f"""
                    Don't even try to timeout an admin lmao"""
                )
                .set_author(name= "Timeout Command Failed")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )

        #   Timeout authorised
        else:
            if reason == None:
                reason = "None specified"
            
            #   Some formatting
            if days == None:
                days = 0
            
            if hours == None:
                hours = 0

            if minutes == None:
                minutes = 0
            
            if seconds == None:
                seconds = 0
            
            #   Duration of timeout
            duration = timedelta(
                days= days,
                hours= hours,
                minutes= minutes,
                seconds= seconds
            )

            await member.timeout_for(duration, reason= reason)

            await ctx.respond(
                embed= Embed(
                description= f"""
                    **Member timed-out:**
                    > <@{member.id}>

                    **Timeout duration:**
                    > {days}d, {hours}h, {minutes}m, {seconds}s

                    **Timeout by:**
                    > <@{ctx.author.id}>

                    **Reason:**
                    > {reason}"""
                )
                .set_author(name= "Timeout Successful")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )
    
    @timeout.error
    async def timeouterror(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond(
                embed= Embed(
                description= "Missing permissions to execute command"
                )
                .set_author(name= "Timeout Unauthorised")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )
        else:
            await ctx.respond(
                embed= Embed(
                description= "Something went wrong"
                )
                .set_author(name= "Timeout Command Failed")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )
            
    
    @discord.slash_command(
        name= "unmute",
        description= "Unmute a user in this server"
    )
    @commands.has_permissions(
        administrator= True
    )
    async def unmute(
        self, ctx,
        member: Option(discord.Member, "Specify who to unmute", required= True)
    ):
        await member.remove_timeout()
        
        await ctx.respond(
                embed= Embed(
                description= f"""
                    **Member timeout removed::**
                    > <@{member.id}>

                    **Approved by:**
                    > <@{ctx.author.id}>"""
                )
                .set_author(name= "Unmute Successful")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )
    
    @unmute.error
    async def unmuteerror(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond(
                embed= Embed(
                description= "Missing permissions to execute command"
                )
                .set_author(name= "Unmute Unauthorised")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )
        else:
            await ctx.respond(
                embed= Embed(
                description= "Something went wrong"
                )
                .set_author(name= "Unmute Command Failed")
                .set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")
            )



def setup(bot):
    bot.add_cog(Moderation(bot))