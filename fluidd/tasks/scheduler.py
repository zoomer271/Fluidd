from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

class Schedule:
    """
    Schedules Tasks For the bot.
    """
    def __init__(self):
        self.scheduler = AsyncIOScheduler()

    def schedule(self, *args):
        """
        *args is your function
        """
        pass