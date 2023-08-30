from discord import Embed

def not_found():
    embed = Embed(
        description= "Command not found"
    )
    embed.set_author(name= "Math Fun! - 404")
    embed.set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")

    return embed

def addition(num1, num2):
    embed = Embed(
        description= f"{num1} + {num2} = {float(num1) + float(num2)}"
    )
    embed.set_author(name= "Math Fun! - Addition")
    embed.set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")

    return embed

def subtraction(num1, num2):
    embed = Embed(
        description= f"{num1} - {num2} = {float(num1) - float(num2)}"
    )
    embed.set_author(name= "Math Fun! - Subtraction")
    embed.set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")

    return embed

def multiplication(num1, num2):
    embed = Embed(
        description= f"{num1} * {num2} = {float(num1) * float(num2)}"
    )
    embed.set_author(name= "Math Fun! - Multiplication")
    embed.set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")

    return embed

def division(num1, num2):
    embed = Embed(
        description= f"{num1} / {num2} = {float(num1) / float(num2)}"
    )
    embed.set_author(name= "Math Fun! - Division")
    embed.set_footer(text= "Måtta Discord Bot - https://github.com/luqmanity/matta")

    return embed