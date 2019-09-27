import discord
from discord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    # CLEAR
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify an amount of messages to delete.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("Action cannot be performed, admin privileges required.")

    # KICK
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("Please specify a member.")
            return
        else:
            await member.kick()
            await ctx.send(f"{member.mention} has been kicked from the server.")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Action cannot be performed, admin privileges required.")

    # BAN
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("Please specify a member.")
            return
        else:
            await member.ban()
            await ctx.send(f"{member.mention} has been banned from the server.")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Action cannot be performed, admin privileges required.")


def setup(client):
    client.add_cog(Moderation(client))
