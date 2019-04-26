# TestPythonBot
# Copyright (C) 2019 Rax Ixor (raxixor@gmail.com)
# Full license in '<base directory>/LICENSE'
from config import CREDENTIALS, CONFIGURATION
from discord.ext import commands
import asyncio
import os
import re
import logging
import discord
import sys
import traceback
import lib.util as util

# Uncomment next line to enable logging of discord.py messages
# logging.basicConfig( level=logging.INFO )
LOG = util.setup_logger( "Main" )

LOG.info( "Starting to load." )

bot = commands.Bot( command_prefix=util.get_prefix, description="A Python Test Bot." )

if __name__ == '__main__':
    for extension in CONFIGURATION["InitialExtensions"]:
        bot.load_extension( extension )
        pass
    pass

@bot.event
async def on_ready( ):
    LOG.info( f"\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n" )
    await bot.change_presence( activity=discord.Game( name="TestPythonBot", type=1, url="https://rax.ee" ) )
    LOG.info( "Successfully logged in and booted." )
    pass

bot.run( CREDENTIALS["Token"], bot=True, reconnect=True )