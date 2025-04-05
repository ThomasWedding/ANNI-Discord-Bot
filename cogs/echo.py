# Local imports
import utils.helpers as helpers
import utils.documentation as document

# Discord imports
import discord
from discord.ext import commands


class echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="echo", description="returns the same message that the user sent")
    async def echo(self, ctx) -> None:
        message = ctx.message.content
        message = message[5:] # truncates the '!echo' part
        await ctx.send(message[5:])

async def setup(bot):
    await bot.add_cog(echo(bot))