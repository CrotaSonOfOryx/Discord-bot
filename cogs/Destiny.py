import aiobungie
import discord
from discord.ext import commands

class VoG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='vogLoot')
    async def Vog_loot(self, ctx):
        """Vault of Glass loot table.
        """
        response='https://cdn.vox-cdn.com/thumbor/cCHZpJJnj3hq7L7eUiW-9teJstE=/1400x0/filters:no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/22531462/NvCnIbB.png'
        await ctx.send(response)
        
    @commands.command(name='vogAdept')
    async def Vog_adept(self, ctx):
        """Vault of Glass (Master) loot table.
        """
        response='http://overgear.com/guides/wp-content/uploads/2021/08/chalenge-loot.png'
        await ctx.send(response)

    @commands.command(name='vogHelp')
    async def Vog_help(self, ctx):
        """Vault of Glass guide.
        """
        response='https://youtu.be/BM688RORcOQ'
        response2='https://youtu.be/vBYPSZotwkU'
        await ctx.send(response)
        await ctx.send(response2)

    @commands.command(name='vogShader')
    async def Vog_shader(self, ctx):
        """Vault of Glass Bitterpearl collectables guide.
        """
        response='https://youtu.be/5qZLfVgWNh8'
        await ctx.send(response)

    @commands.command(name='vogMaster')
    async def Vog_master(self, ctx):
        """Vault of Glass (Master) guide.
        """
        response='https://youtu.be/U_TzK1tAZrM'
        await ctx.send(response)
    
    @commands.command(name='vogChal')
    async def Vog_chal(self, ctx):
        """ Vault of Glass challenges (normal & master)
        """
        response='https://www.reddit.com/r/DestinyTheGame/comments/s7v2lr/master_vog_guide_to_challenges_for_fatebreaker/'
        await ctx.send(response)
    
    @commands.command(name='vogCata')
    async def Vog_cata(self, ctx):
        """ Vex Mythoclast catalyst guide
        """
        response='https://youtu.be/Ip7oROyDxVY'
        await ctx.send(response) 
    
class GoS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='gosLoot')
    async def Gos_loot(self, ctx):
        """Garden of Salvation loot table.
        """
        response='https://external-preview.redd.it/gBdzBanQ51IKYeYoAXLncXlOJykmSkpEqCPUd5n3VdA.jpg?auto=webp&s=6553f120d89515c2b7cce5a0baccc46d180083a6'
        await ctx.send(response)

class DSC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dscLoot')
    async def dsc_loot(self, ctx):
        """Deep Stone Crypt loot table.
        """
        response='https://external-preview.redd.it/ECe3YRpipKfxiMfYWu9iUI-DTpkMoLEa-UeitPM_SWQ.png?auto=webp&s=e24d772719bf4cd8b58f3ced05ebacc7ab722981'
        await ctx.send(response)

class LW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='lwLoot')
    async def lw_loot(self, ctx):
        """Last Wish loot table.
        """
        response='All weapons and armor drop from any encounter'
        await ctx.send(response)   

class VotD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='votdLoot')
    async def vod_loot(self, ctx):
        """Vow of the Disciple loot table.
        """
        response='https://preview.redd.it/1iviuwmyolm81.png?auto=webp&s=a1eb897145679ed523051b29a92cd92326f618d9'
        await ctx.send(response)   


def setup(bot):
    bot.add_cog(VoG(bot))
    bot.add_cog(GoS(bot))
    bot.add_cog(LW(bot))
    bot.add_cog(DSC(bot))
    bot.add_cog(VotD(bot))