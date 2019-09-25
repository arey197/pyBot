import discord
from discord.ext import commands


class Hello(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    '''
    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))
    '''

    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")


def setup(client):
    client.add_cog(Hello(client))
