import discord
from discord.ext import commands
import lib.util as util

def is_owner( ):
    """Checks if someone is an owner."""
    async def predicate(ctx: commands.Context):
        return util.is_owner( ctx.author.id )
    return commands.check( predicate )

def is_guild_owner( ):
    """Checks if someone is a guild owner."""
    async def predicate(ctx: commands.Context):
        if ctx.guild is not None:
            return ctx.guild.owner.id == ctx.author.id
        else:
            return False
    return commands.check( predicate )