import discord
from discord.ext import commands

class Legacy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    class Levi(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command(name='leviHelp')
        async def levi_help(self, ctx):
            """Leviathan (legacy) guide
            """
            response='https://youtu.be/OzkxpLkEkfE'
            await ctx.send(response)

        @commands.command(name='leviMaps')
        async def levi_maps(self, ctx):
            """Leviathan (legacy) maps
            """
            response='https://cdn.vox-cdn.com/thumbor/E1xSyTZvU-IcJK2BxG5ywt1pV88=/1400x0/filters:no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/9416909/pleasuregardens2.png https://gamerant.com/wp-content/uploads/destiny-2-pleasure-gardens-prestige-map.jpg https://i.imgur.com/UVt3gMR.jpg'
            await ctx.send(response)

        @commands.command(name='leviChal')
        async def levi_chal(self, ctx):
            """Leviathan (legacy) challenges
            """
            response='https://www.eurogamer.net/destiny-2-leviathan-raid-guide-walkthrough-4747?page=9'
            await ctx.send(response)

        @commands.command(name='leviLoot')
        async def levi_loot(self, ctx):
            """Leviathan (legacy) loot table
            """
            response='https://pbs.twimg.com/media/DK0hgBeVwAAWHFt.jpg'
            await ctx.send(response)

        @commands.command(name='leviPres')
        async def levi_pres(self, ctx):
            """Leviathan Prestige (legacy) guide 
            """
            response='https://www.youtube.com/watch?v=Zr5f4_9tjJ4'
            await ctx.send(response)

    class EoW(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command(name='eowHelp')
        async def eow_help(self, ctx):
            """Eater of Worlds (legacy) guide 
            """
            response='https://youtu.be/5WljA6Krwbk'
            await ctx.send(response)
 
        @commands.command(name='eowMaps')
        async def eow_maps(self, ctx):
            """Eater of Worlds (legacy) maps 
            """
            response='https://i.imgur.com/yL4IlHe.jpg'
            await ctx.send(response)

        @commands.command(name='eowChest')
        async def eow_chest(self, ctx):
            """Eater of Worlds (legacy) chest location 
            """
            response='https://youtu.be/9X1XY_2c1EA'
            await ctx.send(response)   

    class SoS(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command(name='sosHelp')
        async def sos_help(self, ctx):
            """Spire of Stars (legacy) guide 
            """
            response='https://www.shacknews.com/article/105096/destiny-2---spire-of-stars-raid-lair-guide'
            await ctx.send(response)
 
        @commands.command(name='sosMaps')
        async def sos_maps(self, ctx):
            """Spire of Stars (legacy) maps 
            """
            response='https://external-preview.redd.it/POIQ5_zD3QnUbrNJ9cEB_QG_j5Uy9eI4P9JAL8xYKrc.jpg?auto=webp&s=526c773580be41c3b0c224eb92c07f1f2371a5a4'
            await ctx.send(response)

    class SotP(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command(name='sotpHelp')
        async def sotp_help(self, ctx):
            """Scourge of the Past (legacy) guide 
            """
            response='https://youtu.be/nq0p_JSnQH4'
            await ctx.send(response)

        @commands.command(name='sotpMaps')
        async def sotp_maps(self, ctx):
            """Scourge of the Past (legacy) maps 
            """
            response='https://preview.redd.it/4fqi78jbxy221.png?auto=webp&s=76d62cf9c1eba6f11aa3be8308d4dc8f6f6494dc https://preview.redd.it/dqnu9g4hun521.jpg?auto=webp&s=229747f73d22bff2e9b33094a564ad5c35b04e3e https://external-preview.redd.it/mWcOz2IEvoWtwowYU3HVMqF8GsUdjQ5q4IvsHsdaX10.jpg?auto=webp&s=5863cc17709cb139345db09090fe0fe02b8ac316 https://ipsjwse.s3.eu-north-1.amazonaws.com/monthly_2020_04/large.84993336_BonusAblazedGloryMapfirstdraft.jpg.c27fc1a40671fb6834f7559ebcec09ba.jpg'
            await ctx.send(response)

        @commands.command(name='sotpChal')
        async def sotp_chal(self, ctx):
            """Scourge of the Past (legacy) challenges
            """
            response='https://www.polygon.com/destiny-2-guide-walkthrough/2018/12/21/18148011/scourge-of-the-past-raid-challenge-hold-the-line https://www.reddit.com/r/DestinyTheGame/comments/a9pron/guide_for_all_for_one_one_for_all_raid_challenge/ https://www.polygon.com/destiny-2-guide-walkthrough/2019/1/4/18165903/to-each-their-own-challenge-black-armory-scourge-of-the-past-raid'
            await ctx.send(response)

    class CoS(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command(name='cosHelp')
        async def cos_help(self, ctx):
            """Crown of Sorrow (legacy) guide 
            """
            response='https://youtu.be/1gqDOBWMzx8'
            await ctx.send(response)

        @commands.command(name='cosMaps')
        async def cos_maps(self, ctx):
            """Crown of Sorrow (legacy) maps
            """
            response='https://cdn.vox-cdn.com/thumbor/9WB6vVhJjZqGpODpLcxio2iz3ZM=/1400x0/filters:no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/16333897/Gahlran_s_Deception_fight.jpg'
            await ctx.send(response)

        @commands.command(name='cosChal')
        async def cos_chal(self, ctx):
            """Crown of Sorrow (legacy) challenges
            """
            response='https://youtu.be/3o-9FZPScHc'
            await ctx.send(response)

def setup(bot):
    bot.add_cog(Legacy.Levi(bot))
    bot.add_cog(Legacy.EoW(bot))
    bot.add_cog(Legacy.SoS(bot))
    bot.add_cog(Legacy.SotP(bot))
    bot.add_cog(Legacy.CoS(bot))
