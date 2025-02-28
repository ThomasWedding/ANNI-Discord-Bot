from discord.ext import commands, tasks
import discord
from datetime import datetime
import asyncio

'''

Program automatically sends a message to remind interns to submit their weekly report. This is sent between 12pm-1pm on Saturdays.

Note: this program can be set to send messages at a specific minute in the 12pm-1pm range, but it would need to run 60x as often to check every minute. 
      this can be configured in the wrapper around the weekly_reminder() function

'''

class Report_Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.weekly_reminder.start()

    def cog_unload(self):
        self.weekly_reminder.cancel()

    @tasks.loop(minutes=60)  # NOTE where to configure how often this program runs/checks if it's time for the message. Parameter means it checks every 60 mins obviously. 
    async def weekly_reminder(self):
        now = datetime.now()
        
        if now.weekday() == 0 and now.hour == 12: # NOTE this is where to update the day/time the message is sent
            channel = self.bot.get_channel(895108659552583730)
            if channel:
                await channel.send("Reminder to submit your weekly report by 5pm today!")

    @weekly_reminder.before_loop
    async def before_weekly_task(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(Report_Reminder(bot))
