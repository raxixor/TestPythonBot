import util

LOG = util.setup_logger("Main")

def setup(bot):
    
    @bot.listen()
    async def on_message(message):
        return