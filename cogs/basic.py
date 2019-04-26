import discord
import lib.util as util
from discord.ext import commands

LOG = util.setup_logger( "Main" )

class BasicsCog( commands.Cog ):
    """Basics Cog"""
    def __init__(self, bot):
        self.bot = bot
        pass

    @commands.command( name="repeat", aliases=[ "copy", "mimic", "echo" ] )
    async def do_repeat(self, ctx, *, input: str):
        """Simply echoes what's said."""

        await ctx.send( input )
        pass

    @commands.command( name="about" )
    async def do_about(self, ctx):
        """An about embed."""

        pass
    pass

def setup(bot):
    bot.add_cog( BasicsCog( bot ) )