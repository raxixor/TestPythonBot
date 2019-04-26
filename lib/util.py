# TestPythonBot
# Copyright (C) 2019 Rax Ixor (raxixor@gmail.com)
# Full license in '<base directory>/LICENSE'
from config import CONFIGURATION
from discord.ext import commands
import os
import logging
import discord

def get_prefix(bot: commands.Bot, message: discord.Message):
    """A callable Prefix for our bot."""
    prefixes = CONFIGURATION["Prefixes"]

    if not message.guild:
        return [x for x in prefixes if x["DirectOnly"]]

    return commands.when_mentioned_or(*[x for x in prefixes if not x["DirectOnly"]])(bot, message)

def is_owner(id: int) -> bool:
    """Checks if an ID is in the list of owners.
    
    @param id: ID of the user to check
    @return: True if the user is in the list of owners."""
    return id in CONFIGURATION["Owner"]

def setup_logger(name: str) -> logging.Logger:
    """Sets up a logger.
    
    @param name: Name for the logger
    @return: a Logger set up properly.
    """
    logger = logging.getLogger( name )

    logger.setLevel( logging.DEBUG )
    c_handler = logging.StreamHandler( )
    c_handler.setLevel( logging.DEBUG )

    c_format = logging.Formatter( "({name} | {levelname}): {message}", style="{" )
    c_handler.setFormatter( c_format )

    logger.addHandler( c_handler )

    return logger

def cog_unloadable(cog: str) -> bool:
    """Checks if a cog is able to be unloaded.
    
    @param name: Name of the cog.
    @return: True if the cog can be unloaded."""
    return cog not in CONFIGURATION["NoUnload"]