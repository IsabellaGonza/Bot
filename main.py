#Clse client para crear un bot
"""import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'Hola, soy un bot {client.user}!')
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
        
client.run("Token")"""

#Clse bot para crear bots de discord
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def help_(ctx):
    await ctx.send("Las Funciones del Bot:")
    await ctx.send("$hello: El bot saluda")
    await ctx.send("$heh: Repite heh la cantidad de veces que se espesifíque")
    await ctx.send("$add: Suma dos números")
    await ctx.send("$joined: Dice la fecha en la que un miembro se unió")
    await ctx.send("$repeat: Repite una palabra la cantidad de que se indique")
    await ctx.send("$choose: Elige al azar entre varias opciones")

bot.run("Token")
