import discord
import lib.util as util
from discord.ext import commands

LOG = util.setup_logger("Main")

class ListenersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        pass

def setup(bot):
    bot.add_cog(ListenersCog(bot))