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

def check_kill_command(string: str):
    return string == CONFIGURATION["KillCommand"]

def is_owner(id: int):
    return id in CONFIGURATION["Owner"]

def setup_logger(name):
    logger = logging.getLogger( name )

    logger.setLevel( logging.DEBUG )
    c_handler = logging.StreamHandler( )
    c_handler.setLevel( logging.DEBUG )

    c_format = logging.Formatter( "({name} | {levelname}): {message}", style="{" )
    c_handler.setFormatter( c_format )

    logger.addHandler( c_handler )

    return logger