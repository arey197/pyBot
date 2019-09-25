import discord
from discord.ext import commands


class Hello(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("That command doesn't exist!")

    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)

    @clear.error
    @commands.has_permissions(manage_messages=True)
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify an amount of messages to delete.")


def setup(client):
    client.add_cog(Hello(client))
