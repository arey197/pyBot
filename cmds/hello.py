@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f"{prefix}hello"):
        await message.channel.send('Hello!')