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
cmd = []
onlyfiles = [f for f in listdir("cmds") if isfile(join("cmds", f))]

for i in range(len(onlyfiles)):
    cmd.append(onlyfiles[i].split(".")[0])   # removes the extension from the file and stores it on cmd


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    if not onlyfiles:
        print("No commands to load!")
    else:
        print(onlyfiles)

'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f"{prefix}hello"):
        await message.channel.send('Hello!')
'''


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for x in range(len(cmd)):
        if message.content.startswith(f"{prefix}{cmd[x]}"):
            await message.channel.send(f"Yup, the **{cmd[x]}** command exists!")
            break

client.run(token)
