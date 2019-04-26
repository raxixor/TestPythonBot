import discord
import util
from discord.ext import commands

LOG = util.setup_logger( "Main" )

class BasicsCog( commands.Cog ):
    """Basics Cog"""
    def __init__(self, bot):
        self.bot = bot
        pass

    @commands.command(name="ping", aliases=["pong"])
    async def ping(self, ctx: commands.Context):
        """A simple test command to check if the bot is actually running."""

        await ctx.send("Pong!")
        pass

    pass

def setup(bot):
    bot.add_cog( BasicsCog( bot ) )