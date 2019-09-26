# module imports
import discord
from discord.ext import commands
import os
import json
from os import listdir
from os.path import isfile, join

# Reading the json file
with open("botsettings.json") as json_data:
    botSettings = json.load(json_data)
    token = botSettings.get("token")
    prefix = botSettings.get("prefix")
    # ownerID = botSettings.get("ownerID")  // better to implement both with Discord permissions instead of hard coding
    # adminID = botSettings.get("adminID")  // them on the json file


client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Miami's daily traffic!"))
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That command doesn't exist!")


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")  # removes the last 3 characters of the string (.py)
        print(f"Loaded cogs.{filename[:-3]} correctly")


client.run(token)
