# Standard includes
import discord
from discord.ext import commands

# Define and initialize "mimic" command
class mimic( commands.Cog ):
    def __init__( self, bot ):
        self.bot = bot

    # Command that simply repeats the provided input back to the user
    @commands.command( name = "mimic", description = "Repeats provided input back to the user" )
    async def mimic( self, ctx, *, message ):
        await ctx.send( message )

# Set up command when the bot is started
async def setup( bot ):
    await bot.add_cog( mimic( bot ) )