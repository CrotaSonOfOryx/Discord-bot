import discord
from discord.ext import commands

class Crucible(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='pacifica')
    async def paci(self, ctx):
        """Pacifica map 
        """
        response='https://warmind.io/img/maps/Pacifica.jpg'
        await ctx.send(response)

    @commands.command(name='aof')
    async def flame(self, ctx):
        """Altar of Flame map 
        """
        response='https://warmind.io/img/maps/Altar_of_Flame.jpg'
        await ctx.send(response)

    @commands.command(name='shore')
    async def shore(self, ctx):
        """Distant Shore map 
        """
        response='https://warmind.io/img/maps/Distant_Shore.jpg'
        await ctx.send(response)

    @commands.command(name='respite')
    async def emperor(self, ctx):
        """Emperor's Respite (legacy) map 
        """
        response='https://warmind.io/img/maps/Emperors_Respite.jpg'
        await ctx.send(response)

    @commands.command(name='vale')
    async def vale(self, ctx):
        """Endless Vale map 
        """
        response='https://warmind.io/img/maps/Endless_Vale.jpg'
        await ctx.send(response)

    @commands.command(name='eternity')
    async def eternity(self, ctx):
        """Eternity map 
        """
        response='https://warmind.io/img/maps/Eternity.jpg'
        await ctx.send(response)

    @commands.command(name='javelin')
    async def jav(self, ctx):
        """Javelin-4 map 
        """
        response='https://warmind.io/img/maps/Javelin-4.jpg'
        await ctx.send(response)

    @commands.command(name='gulch')
    async def gulch(self, ctx):
        """Legion's Gulch (legacy) map 
        """
        response='https://warmind.io/img/maps/Legions_Gulch.jpg'
        await ctx.send(response)
        
    @commands.command(name='midtown')
    async def midtown(self, ctx):
        """Midtown map 
        """
        response='https://warmind.io/img/maps/Midtown.jpg'
        await ctx.send(response)

    @commands.command(name='retrib')
    async def retrib(self, ctx):
        """Retribution (legacy) map 
        """
        response='https://warmind.io/img/maps/Retribution.jpg'
        await ctx.send(response)

    @commands.command(name='cliffs')
    async def cliffs(self, ctx):
        """The Dead Cliffs map 
        """
        response='https://warmind.io/img/maps/The_Dead_Cliffs.jpg'
        await ctx.send(response)

    @commands.command(name='fort')
    async def fort(self, ctx):
        """The Fortress map 
        """
        response='https://warmind.io/img/maps/The_Fortress.jpg'
        await ctx.send(response)

    @commands.command(name='vostok')
    async def vostok(self, ctx):
        """Vostok map 
        """
        response='https://warmind.io/img/maps/Vostok.jpg'
        await ctx.send(response)

    @commands.command(name='haven')
    async def haven(self, ctx):
        """Wormhaven map 
        """
        response='https://warmind.io/img/maps/Wormhaven.jpg'
        await ctx.send(response)

    @commands.command(name='cliffs')
    async def cliffs(self, ctx):
        """Radiant Cliffs map 
        """
        response='https://warmind.io/img/maps/Radiant_Cliffs.jpg'
        await ctx.send(response)

    @commands.command(name='burn')
    async def burn(self, ctx):
        """The Burnout map 
        """
        response='https://warmind.io/img/maps/The_Burnout.jpg'
        await ctx.send(response)

    @commands.command(name='solitude')
    async def solitude(self, ctx):
        """Solitude (legacy) map 
        """
        response='https://warmind.io/img/maps/Solitude.jpg'
        await ctx.send(response)

    @commands.command(name='melt')
    async def melt(self, ctx):
        """Meltdown (legacy) map 
        """
        response='https://warmind.io/img/maps/Meltdown.jpg'
        await ctx.send(response)

    @commands.command(name='banner')
    async def banner(self, ctx):
        """Bannerfall map 
        """
        response='https://warmind.io/img/maps/Bannerfall.jpg'
        await ctx.send(response)

    @commands.command(name='conver')
    async def conver(self, ctx):
        """Convergance map 
        """
        response='https://warmind.io/img/maps/Convergence.jpg'
        await ctx.send(response)

    @commands.command(name='equinox')
    async def equinox(self, ctx):
        """Equinox map 
        """
        response='No map yet :('
        await ctx.send(response)

    @commands.command(name='echo')
    async def echo(self, ctx):
        """Firebase Echo (legacy) map 
        """
        response='No map yet :('
        await ctx.send(response)

    @commands.command(name='citadel')
    async def citadel(self, ctx):
        """Citedel (legacy) map 
        """
        response='No map yet :('
        await ctx.send(response)

    @commands.command(name='ruin')
    async def echo(self, ctx):
        """Gambler's Ruin (legacy) map 
        """
        response='No map yet :('
        await ctx.send(response)

    @commands.command(name='fragment')
    async def fragment(self, ctx):
        """Fragment map 
        """
        response='No map yet :('
        await ctx.send(response)

    @commands.command(name='gap')
    async def gap(self, ctx):
        """Twilight Gap map 
        """
        response='https://warmind.io/img/maps/Twilight_Gap.jpg'
        await ctx.send(response)

    @commands.command(name='court')
    async def court(self, ctx):
        """Widow's Court map 
        """
        response='https://warmind.io/img/maps/Widows_Court.jpg'
        await ctx.send(response)

    @commands.command(name='rust')
    async def rust(self, ctx):
        """Rusted Lands map 
        """
        response='https://warmind.io/img/maps/Rusted_Lands.jpg'
        await ctx.send(response)

    @commands.command(name='anomaly')
    async def anomaly(self, ctx):
        """The Anomaly map 
        """
        response='No map yet :('
        await ctx.send(response)

    @commands.command(name='blue')
    async def blue(self, ctx):
        """Exodus Blue map 
        """
        response='No map yet :('
        await ctx.send(response)

    @commands.command(name='cauldron')
    async def cauldron(self, ctx):
        """The Cauldron map 
        """
        response='https://warmind.io/img/maps/Cauldron.jpg'
        await ctx.send(response)

def setup(bot):
    bot.add_cog(Crucible(bot))