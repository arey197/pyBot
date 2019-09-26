import discord
from discord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)

    @clear.error
    @commands.has_permissions(manage_messages=True)
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify an amount of messages to delete.")


def setup(client):
    client.add_cog(Moderation(client))