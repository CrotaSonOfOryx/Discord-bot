import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='%',intents=intents)                      #prefix

@bot.event                                                  #message o połączeniu do serwera
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@bot.event                                               #witajka
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Witaj Strażniku {member.name}!'
    )

@bot.event                                                                                  #role check
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('Nie posiadasz odpowiedniej rangi dla tej komendy <:losos:949354894488383488>')

@bot.command(name='test', help='Test')                                               #testowa komenda
@commands.has_role('Uprawnienia')
async def nine_nine(ctx):
    response = 'Tu nie ma światuła!'
    await ctx.send(response)

for cog_new in os.listdir("C:/Users/socze/Desktop/bot/cogs"): #cogs
    if cog_new.endswith(".py"):
        try:
            cog = f"cogs.{cog_new.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog_new} can not be loaded: {e}")

bot.run(TOKEN)
