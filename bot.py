# module imports
import discord
import json
from os import listdir
from os.path import isfile, join

# reading the json file
with open("botsettings.json") as json_data:
    botSettings = json.load(json_data)
    token = botSettings.get("token")
    prefix = botSettings.get("prefix")
    # ownerID = botSettings.get("ownerID")  // better to implement both with Discord permissions instead of hard coding
    # adminID = botSettings.get("adminID")  // them on the json file


client = discord.Client()

# listing all the files on cmds
onlyfiles = [f for f in listdir("cmds") if isfile(join("cmds", f))]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(onlyfiles)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f"{prefix}hello"):
        await message.channel.send('Hello!')

client.run(token)
