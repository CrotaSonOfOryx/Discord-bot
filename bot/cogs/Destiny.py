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

    @commands.command(name='vogColl')
    async def Vog_shader(self, ctx):
        """Vault of Glass Bitterpearl collectibles guide.
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
    
    @commands.command(name='vogMaps')
    async def Vog_Maps(self, ctx):
        """ Vault of Glass maps
        """
        response='https://external-preview.redd.it/cDYr6Pw9U2_wQv6jDYCQG4G561Cla_bfREHgYZOB2jg.jpg?auto=webp&s=a1c822efc50ea974088dffe5b223896085e9a7e5 https://destinyraider.files.wordpress.com/2015/03/vog-maps_templars-well-conflux-1.png  https://external-preview.redd.it/onlPaktR_xhwsLjN-wSwPMG-3CaEkzx427owlzFRobE.jpg?auto=webp&s=22024d2d383ea4b1d40730a094ffe997111f0748  https://destinyraider.files.wordpress.com/2015/03/vog_maps_waking-ruins_2.png'
        await ctx.send(response) 

    @commands.command(name='vogTriumph')
    async def Vog_triumph(self, ctx):
        """ Vault of Glass triumphs
        """
        response='https://youtu.be/pgTLfbDVzmQ https://youtu.be/b_tC_RBs6MI https://youtu.be/8sM3x9NcBUc https://youtu.be/0GDu0daAbuc https://youtu.be/zECAFZ-v3Xw https://youtu.be/ad5qilgYiOY'
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

    @commands.command(name='gosMaps')
    async def Gos_maps(self, ctx):
        """Garden of Salvation maps.
        """
        response='https://www.powerpyx.com/wp-content/uploads/Desiny-2-Shadowkeep-Garden-of-Salvation-Map-3-300x169.jpg https://external-preview.redd.it/DHZ20ueQuQCZzLyxJ_ZoIJf1E4b-Rh3JM2dd4pNu2lE.jpg?auto=webp&s=72a703defa0e9da9e75d6a8e308a6989d36e0c6d'
        await ctx.send(response)
    
    @commands.command(name='gosHelp')
    async def Gos_help(self, ctx):
        """Garden of Salvation guide.
        """
        response='https://youtu.be/IvOVrXudWNw'
        await ctx.send(response)

    @commands.command(name='gosChal')
    async def Gos_chal(self, ctx):
        """Garden of Salvation challenges.
        """
        response='https://www.eurogamer.net/destiny-2-garden-of-salvation-challenges-6007'
        await ctx.send(response)

    @commands.command(name='gosDiv')
    async def Gos_div(self, ctx):
        """Garden of Salvation Divinity run guide.
        """
        response='https://youtu.be/BL7cJxcPtSs'
        await ctx.send(response)

    @commands.command(name='gosTriumph')
    async def gos_triumph(self, ctx):
        """Garden of Salvation triumphs
        """
        response='https://youtu.be/Y9mwt_ojXN0 https://youtu.be/FwKHVqf6HaY https://youtu.be/hzJeEcrNlDs https://youtu.be/O5AXzTPo63A'
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

    @commands.command(name='dscHelp')
    async def dsc_help(self, ctx):
        """Deep Stone Crypt guide.
        """
        response='https://youtu.be/snBkeb7hvVU'
        await ctx.send(response)

    @commands.command(name='dscMaps')
    async def dsc_maps(self, ctx):
        """Deep Stone Crypt maps.
        """
        response='https://geilt.com/wp-content/uploads/2020/12/dsc-atraks-1-space.png https://geilt.com/wp-content/uploads/2020/12/dsc-crypt-security-top-floor.png https://external-preview.redd.it/CZuyhtA6AEI36SJi6kKpngxA0HIf_LoNJhnNou4y6Xk.jpg?auto=webp&s=2dc78a442cf49e992aacf5aaf19462eef08ce9d5 https://pbs.twimg.com/media/En74iHHWMAAs9UE.jpg https://pbs.twimg.com/media/En74iGrVEAA0RhP.jpg'
        response2='https://external-preview.redd.it/Ynbw3E0Vm2kXCksY-REHYq2PK_VYNhdYRxZW-3eDPiI.jpg?auto=webp&s=9024ae3b389832ecb8bf7f55d110026226016a16'
        await ctx.send(response)
        await ctx.send(response2)

    @commands.command(name='dscChal')
    async def dsc_chal(self, ctx):
        """Deep Stone Crypt challenges.
        """
        response='https://external-preview.redd.it/o_XIQFH8XgFV542p5ELfxIk8XueajzdIFxxfIYmZxQ4.jpg?auto=webp&s=512b15f7a028c6b42597b4a1cf0af5c2e84f8baf, https://youtu.be/-jqEEyd6kdU'
        await ctx.send(response)

    @commands.command(name='dscColl')
    async def dsc_ghost(self, ctx):
        """Deep Stone Crypt Exo data pads guide (ghost shell collectibles).
        """
        response='https://youtu.be/N_qWFV2o-X8'
        await ctx.send(response)
    
    @commands.command(name='dscTriumph')
    async def dsc_triumph(self, ctx):
        """Deep Stone Crypt triumphs
        """
        response='https://youtu.be/DibQLmb72qE https://youtu.be/PTcVYI15DnY https://youtu.be/Rtmg8Tn4jo8 https://youtu.be/GrULV_8TM4g'
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
       
    @commands.command(name='lwHelp')
    async def lw_help(self, ctx):
        """Last Wish guide.
        """
        response='https://youtu.be/54I9DUz5JaQr'
        await ctx.send(response)

    @commands.command(name='lwChal')
    async def lw_chal(self, ctx):
        """Last Wish challenges.
        """
        response='https://youtu.be/TRMBIV0yKEM https://youtu.be/67BuMtPMqXs https://youtu.be/hr2KArqxMcM https://youtu.be/FUzeykFixjk https://youtu.be/hyg4u-L0TIs'
        await ctx.send(response)

    @commands.command(name='lwMaps')
    async def lw_maps(self, ctx):
        """Last Wish maps.
        """
        response='https://external-preview.redd.it/_REkK_9Zajlf0v6u7UOY1wcuVE4Mj_NKGa-45Km6w5Q.jpg?auto=webp&s=de3d7bd287e4600a3a0800f9ef37db2531085f84'
        await ctx.send(response)

    @commands.command(name='lwColl')
    async def lw_coll(self, ctx):
        """Last Wish collectibles (taken eggs for sparrow).
        """
        response='https://youtu.be/81XxH2E-RsE'
        await ctx.send(response)

    @commands.command(name='lwWish')
    async def lw_wish(self, ctx):
        """Last Wish wishes.
        """
        response='https://external-preview.redd.it/aavingD6IbbNh7woYBJ9a8_h1WGICaXYtwVRt-j610o.jpg?auto=webp&s=d6a94062a594b8642957ca3420ee4399114dd2d1'
        await ctx.send(response)  

    @commands.command(name='lwCalls')
    async def lw_wish(self, ctx):
        """Last Wish symbol callouts.
        """
        response='https://external-preview.redd.it/crRNxN0JBvWGFHs52LEEoLvSfrUVeK03WwcRTcAUHys.jpg?auto=webp&s=b48ce85faee8c20c6a4efedd391e335dddb72631'
        await ctx.send(response) 

class VotD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='votdLoot')
    async def vod_loot(self, ctx):
        """Vow of the Disciple loot table.
        """
        response='https://cdn.vox-cdn.com/thumbor/hSc7NF6x-aRkMt28dkKT9yejGH4=/0x0:2048x1152/1200x0/filters:focal(0x0:2048x1152):no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/23304244/VotDLootTable.Table.jpg'
        await ctx.send(response)   

    @commands.command(name='votdMaps')
    async def vod_maps(self, ctx):
        """Vow of the Disciple maps.
        """
        response='https://cdn.vox-cdn.com/thumbor/kbxUP4gTftKgs9QldAehPL89f-s=/0x0:1920x1080/1200x0/filters:focal(0x0:1920x1080):no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/23300581/IMOHPw8.jpg https://cdn.vox-cdn.com/thumbor/kbxUP4gTftKgs9QldAehPL89f-s=/0x0:1920x1080/1200x0/filters:focal(0x0:1920x1080):no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/23300581/IMOHPw8.jpg https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2022/03/destiny-2-artifacts-exhibition-map.jpg'
        await ctx.send(response)
    
    @commands.command(name='votdMaster')
    async def vod_master(self, ctx):
        """Vow of the Disciple (Master) guide.
        """
        response='https://youtu.be/r8-t2RDNQiQ'
        await ctx.send(response) 

    @commands.command(name='votdTriumph')
    async def vod_triumph(self, ctx):
        """Vow of the Disciple triumphs guide. 
        """
        response='https://youtu.be/r8Op7AHibEE https://youtu.be/Vc0WdhwOSkY https://youtu.be/ThJU0x54ies https://youtu.be/nbg6iRsKD4s'
        await ctx.send(response) 

    @commands.command(name='votdChal')
    async def vod_chal(self, ctx):
        """Vow of the Disciple challenges guide. 
        """
        response='https://youtu.be/hSAbRouUnE0 https://youtu.be/vND0iOZEn-s https://youtu.be/Zyp3fgIrVe0 https://youtu.be/QGuxfef6oRU'
        await ctx.send(response) 

    @commands.command(name='votdHelp')
    async def vod_help(self, ctx):
        """Vow of the Disciple guide. 
        """
        response='https://youtu.be/3zcfl1mtgVU'
        await ctx.send(response) 

    @commands.command(name='votdCalls')
    async def vod_calls(self, ctx):
        """Vow of the Disciple callouts. 
        """
        response='https://oyster.ignimgs.com/mediawiki/apis.ign.com/destiny-2/8/88/RaidGlyphsVotD.jpg?width=1280'
        await ctx.send(response) 

    @commands.command(name='votdChest')
    async def vod_chest(self, ctx):
        """Vow of the Disciple insight chest puzzle. 
        """
        response='https://www.reddit.com/r/DestinyTheGame/comments/taf57b/vow_of_the_disciple_symbol_room_locations/'
        await ctx.send(response) 

        
def setup(bot):
    bot.add_cog(VoG(bot))
    bot.add_cog(GoS(bot))
    bot.add_cog(LW(bot))
    bot.add_cog(DSC(bot))
    bot.add_cog(VotD(bot))