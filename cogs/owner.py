import discord
import util
from discord.ext import commands

LOG = util.setup_logger( "Main" )

class OwnerCog( commands.Cog, name="Owner Commands", command_attrs=dict( hidden=True ) ):
    """Owner Commands Cog"""
    def __init__(self, bot):
        self.bot = bot
        pass


    pass

def setup(bot: commands.Bot):
    bot.add_cog( OwnerCog( bot ) )