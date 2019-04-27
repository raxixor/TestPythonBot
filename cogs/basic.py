import discord
import lib.util as util
from discord.ext import commands
from config import IDENTITY

LOG = util.setup_logger( "Main" )

class BasicsCog( commands.Cog, name="Basic Commands" ):
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
        user = self.bot.user

        embed = discord.Embed( title=f"About {IDENTITY['Name']}", description=IDENTITY["Description"], color=0x00ff00 )

        embed.set_author(name="Lys#5926", url="https://rax.ee", icon_url="https://i.imgur.com/8gRCPpf.png")

        embed.add_field(name="Repository Link", value=IDENTITY["Repo"], inline=False)
        embed.add_field(name="Created On", value=f"{user.created_at}", inline=False)

        await ctx.send(embed=embed)
        pass
    pass

def setup(bot):
    bot.add_cog( BasicsCog( bot ) )