# Måtta The Discord Bot

This is a rewritten version. The LEGACY version can be found [here](https://github.com/luqmanity/matta-legacy).

### Join the Discord Server for support, etc:
https://discord.gg/7w8b6MMXBy

This is a general-purpose, all-in-one Discord bot designed to be helpful and customisable according to the exact
needs and wants, requirements and situations of servers and communities.

Made using Python, pycord fork of the discord library. Some JSON is used for data saving.
Ping me on Discord via the server if you would like to be a contributor.

This repo includes an overview of how to run the bot, and the default commands.

**Usage of the source code for commercial, private or fun uses are allowed, as long as this repo is credited. The crediting needs to be easily visible.**

# How to run
## 1 - Discord application, bot
You'll need a Discord bot token in order for this to work. Head over to [discord.com/developers](https://discord.com/developers/applications), create/select an application.
Open the application, then go to the Bots page and click that reset token button to generate a token.
**Do note that if you have a existing code that uses a token, clicking that reset disables the old token and you'll have to use the newly generated one.**

Copy the token displayed. If you have 2FA enabled, you may need to enter your authorisation code.
![image](https://github.com/luqmanity/matta/assets/75654558/89826e88-a539-4a5b-a80b-ad40e689dbbd)

## 2 - Adding the token to the project
Assuming you have the source code downloaded (raw), next you'll need to create a `.env` file in the main directory.
Include the following variable:
```env
TOKEN = "Your Bot Token"
```

# Commands
An overview of the currently available commands.

## Moderation
`/timeout` <br>
Time out a user<br>
`/unmute` <br>
Removes timeout<br>
`/kick` <br>
Kicks a user<br>
`/ban` <br>
Bans a user<br>

## Autoresponder
Autoresponders works by having a dictionary storing all the triggers and responses for a unique autoresponder in each server.
It can also be edited and toggled, or even deleted. It's just here for fun so you can at least do some conversations
with bots in a lonely server lol. 

`/autoresponder add` <br>
Create a new autoresponder, include triggers and responses. <br>
`/autoresponder toggle` <br>
Toggle an autoresponder<br>
`/autoresponder edit` <br>
Edit the triggers and responses of an existing autoresponder<br>
`/autoresponder delete` <br>
Deletes an autoresponder<br>
