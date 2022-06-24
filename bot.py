import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix= '[',intents = intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(989811936080298035)
    await channel.send(f'{member} join!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(989811995593285663)
    await channel.send(f'{member} leave!')

bot.run("OTg2MTA3Mjc2NDA0MzMwNDk2.G4KN1p.cKyyMHndH8Vg3ehdxwsKYPipE67wDyODSqTLnI")