import util

LOG = util.setup_logger("Main")

def setup(bot):

    @bot.listen()
    async def on_ready():
        LOG.info("Logged in as: {}".format(bot.user))
        return