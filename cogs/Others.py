import discord
from discord.ext import commands

class Others(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='cats')
    async def cats(self, ctx):
        """Dreaming city cats collectables
        """
        response='https://www.shacknews.com/article/107348/all-cat-locations-in-the-dreaming-city-in-destiny-2'
        await ctx.send(response)

    @commands.command(name='bun')
    async def bun(self, ctx):
        """ Moon Bunnies collectables
        """
        response='https://www.shacknews.com/article/114314/all-jade-rabbit-locations-on-the-moon-in-destiny-2'
        await ctx.send(response) 

    @commands.command(name='peng')
    async def peng(self, ctx):
        """ Europa penguins collectables
        """
        response='https://www.shacknews.com/article/121495/all-penguin-souvenir-locations-on-europa-destiny-2'
        await ctx.send(response)  

    @commands.command(name='moth')
    async def moth(self, ctx):
        """ Throne World moths collectables
        """
        response='https://www.shacknews.com/article/129115/all-lucent-moth-locations-destiny-2'
        await ctx.send(response)  

    @commands.command(name='egg')
    async def egg(self, ctx):
        """ Corrupted eggs for taken sparrow
        """
        response='https://www.shacknews.com/article/107725/all-corrupted-egg-locations-in-destiny-2'
        await ctx.send(response)  

def setup(bot):
    bot.add_cog(Others(bot))