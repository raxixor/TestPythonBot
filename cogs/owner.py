import discord
from lib import checks, util
from discord.ext import commands

LOG = util.setup_logger( "Main" )

class OwnerCog( commands.Cog, name="Owner Commands", command_attrs=dict( hidden=True ) ):
    """Owner Commands Cog"""
    def __init__(self, bot):
        self.bot = bot
        pass

    @commands.group( name="cog", pass_context=True, hidden=True )
    @checks.is_owner( )
    async def group_cog(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send( "Invalid sub command passed.\nFor more info, do `cog help`" )
            pass
        pass

    @group_cog.command(name="help")
    @checks.is_owner( )
    async def help_cog(self, ctx, *, command: str):
        embed = discord.Embed(title="Cog Management Commands",
                              description="Commands for managing Cogs.",
                              colour=0x00FF00)

        embed.set_author(name = )
        pass

    @group_cog.command( name="load" )
    @checks.is_owner( )
    async def load_cog(self, ctx, *, cog: str):
        """Loads a module.
        Remember to use dot path, example: 'cogs.owner'"""
        try:
            self.bot.load_extension( cog )
        except Exception as e:
            await ctx.send( f"An error occurred. ```{type(e).__name__}\n{e}```" )
        else:
            await ctx.send( f'Successfully loaded `{cog}`' )
        pass

    @group_cog.command( name="unload" )
    @checks.is_owner( )
    async def unload_cog(self, ctx, *, cog: str):
        """Unloads a module.
        Remember to use dot path, example: 'cogs.owner'"""

        if not util.cog_unloadable( cog ):
            await ctx.send( f"You cannot unload `{cog}`." )
            return
        try:
            self.bot.unload_extension( cog )
        except Exception as e:
            await ctx.send( f"An error occurred. ```{type(e).__name__}\n{e}```" )
        else:
            await ctx.send( f"Successfully unloaded `{cog}`." )
        pass

    @group_cog.command( name="reload" )
    @checks.is_owner( )
    async def reload_cog(self, ctx, *, cog: str):
        """Reloads a module.
        Remember to use dot path, example: 'cogs.owner'"""

        try:
            self.bot.unload_extension( cog )
            self.bot.load_extension( cog )
        except Exception as e:
            await ctx.send( f"An error occurred. ```{type(e).__name__}\n{e}```" )
        else:
            await ctx.send( f"Successfully reloaded `{cog}`." )
        pass

    pass

def setup(bot: commands.Bot):
    bot.add_cog( OwnerCog( bot ) )