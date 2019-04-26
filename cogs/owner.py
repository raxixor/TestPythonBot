import discord
from lib import checks, util
from discord.ext import commands

LOG = util.setup_logger( "Main" )

class OwnerCog( commands.Cog, name="Owner Commands", command_attrs=dict( hidden=True ) ):
    """Owner Commands Cog"""
    def __init__(self, bot):
        self.bot = bot
        pass

    @commands.command( name="load" )
    @checks.is_owner( )
    async def cog_load(self, ctx, *, cog: str):
        """Loads a module.
        Remember to use dot path, example: 'cogs.owner'"""
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f"An error occurred. ```{type(e).__name__} - {e}```")
        else:
            await ctx.send(f'Successfully loaded "{cog}"')
        pass

    @commands.command(name="unload")
    @checks.is_owner()
    async def cog_unload(self, ctx, *, cog: str):
        """Unloads a module.
        Remember to use dot path, example: 'cogs.owner'"""

        if util.cog_unloadable(cog):


    pass

def setup(bot: commands.Bot):
    bot.add_cog( OwnerCog( bot ) )