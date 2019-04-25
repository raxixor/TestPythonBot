# TestPythonBot
# Copyright (C) 2019 Rax Ixor (raxixor@gmail.com)
# Full license in '<base directory>/LICENSE'

from config import CONFIGURATION

def check_prefix(string: str):
    return string.startswith(CONFIGURATION["Prefix"])

def strip_prefix(string: str):
    if string.startswith(CONFIGURATION["Prefix"]):
        return string[len(CONFIGURATION["Prefix"]):]
    return string

def check_kill_command(string: str):
    return string == CONFIGURATION["KillCommand"]

def is_owner(id: int):
    return id in CONFIGURATION["Owner"]