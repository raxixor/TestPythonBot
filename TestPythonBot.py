# TestPythonBot
# Copyright (C) 2019 Rax Ixor (raxixor@gmail.com)
# Full license in '<base directory>/LICENSE'
from config import CREDENTIALS, CONFIGURATION, IDENTITY
from discord.ext import commands
import asyncio
import logging
import discord
import lib.util as util

# Uncomment next line to enable logging of discord.py messages
# logging.basicConfig( level=logging.INFO )
LOG = util.setup_logger( "Main" )

LOG.info( "Starting to load." )

bot = commands.Bot( command_prefix=util.get_prefix, description=IDENTITY["Description"] )

if __name__ == '__main__':
    for extension in CONFIGURATION["InitialExtensions"]:
        try:
            bot.load_extension( extension )
        except Exception:
            LOG.error( f"Failed to load extension '{extension}'.", exc_info=True )
            continue
        else:
            LOG.info( f"Loaded `{extension}`" )
            continue
        pass
    pass

@bot.event
async def on_ready( ):
    LOG.info( f"\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\nOwners: {util.get_owners()}" )
    await bot.change_presence( activity=discord.Game( name="TestPythonBot", type=1, url="https://rax.ee" ) )
    LOG.info( "Successfully logged in and booted." )
    pass

bot.run( CREDENTIALS["Token"], bot=True, reconnect=True )