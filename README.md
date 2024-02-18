# Måtta The Discord Bot

**Please note that this project has not been updated for at least 5 months. Some scripts may not work as intended**.
This is the rewritten and latest version of Måtta. The LEGACY version can be found [here](https://github.com/luqmanity/matta-legacy) (legacy version is no longer supported)

Join the Discord Server for support, etc:
https://discord.gg/7w8b6MMXBy

Måtta is an open-sourced Discord bot made by luqmanity and several
other contributors, using `pycord` (a fork of discord.py).
This bot also uses cogs, command groups, and discord views and UI.
It is recommended to at least have some experience working on
Discord bots, and pycord, if you would like to contribute to the project.

This repo includes an overview of how to run the bot and other useful informations. Use `/help` after completing setup!

**Usage of the source code for commercial, private, or fun uses is allowed, as long as this repo is credited. The crediting needs to be easily visible.**

## How to run

Below are the instructions on how to run this bot on your local machine.

### 1 - Discord application, bot

You'll need a Discord bot token in order for this to work. Head over to [discord.com/developers](https://discord.com/developers/applications), and create/select an application.
Open the application, then go to the Bots page and click that reset token button to generate a token.
**Do note that if you have an existing code that uses a token, clicking that reset disables the old token and you'll have to use the newly generated one.**

Copy the token displayed. If you have 2FA enabled, you may need to enter authorization code.
![image](https://github.com/luqmanity/matta/assets/75654558/89826e88-a539-4a5b-a80b-ad40e689dbbd)

### 2 - Setup

Setting up is easy, simply run `main.py` and it will ask if to open **Config Panel** - simply
proceed by inputting **y**.  It should output a panel on the console, that shows available actions and
it's description. Simply input "setup", and once "setup complete" is outputted, all required folders
and files should be created in the project folder.

**The folders and files created are required for the bot to function, but is excluded from 
this repo so that anyone can just keep their old data even when running off a newer version.**

**Alternatively**, you can run the `config.py` script located in the project.

Please note that if you ran `main.py` to open the Config Panel, the bot will run after
the Config Panel closed (using `quit`).

### 3 - Token

Now that we've got all the required files and folders, all that is left is the bot token. Open the `data`
folder in the project folder (by default: matta/data), then open `.env`.

Once opened, edit to include the following variable:

```env
TOKEN = "Your Bot Token"
```

Your Discord bot should work now! Do note that Discord will reset/disable the token if they found it
somewhere in the internet. Discord will DM you to inform if that happens. Please do **NOT** share your
discord bot's token anywhere unsecure, and it's best to keep it to yourself or your team. If you need
to share the token, please encrypt it so only those with the key(s) can view the token.

The token will be invalid if Discord found it on the internet via crawlers, if so happens, Discord will notify you regarding this and will ask you to generate a new one.

## Updating

You can easily update the bot by downloading the source code, then running `config.py`. The process
is similar to when you first setup the bot. The `setup()` function will check
what files, folders, etc is missing, then later creates it. *If it exists but is on an outdated format,
it will be updated and included with new data. (Planned)*

## Config panel

This project includes `config.py`, which is a console-based panel created specifically help with
a variety of tools that can help you manage and customise the bot the way you want it to be!

The Config Panel is updated in every major release.

## The future of this project

I will work on a major rewrite of this project this year (2024). 