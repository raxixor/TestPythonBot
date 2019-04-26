import discord
from discord.ext import commands
import lib.util as util

def is_owner():
    """Checks if someone is an owner."""
    def predicate(ctx: commands.Context):
        return util.is_owner(ctx.message.author.id)
    return commands.check(predicate)