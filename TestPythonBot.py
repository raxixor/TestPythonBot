# TestPythonBot
# Copyright (C) 2019 Rax Ixor (raxixor@gmail.com)
# Full license in '<base directory>/LICENSE'
from config import CREDENTIALS, CONFIGURATION
import util
import discord
from discord.ext import commands
import asyncio
import os
import re
import logging

logging.basicConfig(level=logging.INFO)

LOG = util.setup_logger( "Main" )
print( LOG )

EXTENSIONS = [ ]

def load_listeners(bot: commands.Bot):
    LOG.info( "Loading Listeners..." )
    FILES = []

    for root, dirs, files in os.walk("listeners/"):
        for file in files:
            if file.endswith(".py"):
                FILES.append(file.rstrip(".py"))
            pass
        pass

    for x in FILES:
        LOG.info("Loading {}".format(x))
        bot.load_extension("listeners.{}".format(x))
    
    return

LOG.info( "Starting to load." )

bot = commands.Bot( command_prefix=CONFIGURATION["Prefix"] )

load_listeners( bot )

bot.run( CREDENTIALS["Token"] )