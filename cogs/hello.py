import discord
from discord.ext import commands


class Hello(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events @commands.Cog.listener()

    # Commands @commands.command()
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")


def setup(client):
    client.add_cog(Hello(client))
