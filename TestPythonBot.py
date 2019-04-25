# TestPythonBot
# Copyright (C) 2019 Rax Ixor (raxixor@gmail.com)
# Full license in '<base directory>/LICENSE'

from config import CREDENTIALS
import util
import discord

class TestPythonBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as: {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if util.check_kill_command(message.content) and util.is_owner(message.author.id):
            await message.delete()
            await self.logout()
            if not self.is_closed():
                await self.close()
            print("Exited")
            return

        # TODO: Command Handler
            

client = TestPythonBot()
client.run(CREDENTIALS["Token"])