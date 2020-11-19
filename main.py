#python3 main.py
import discord
from discord.ext import commands
from leverMain import get_duration, has_nick_prefixe, hand_already_raised, raise_hand 

bot = commands.Bot(command_prefix = "!", description = "Je sers à faciliter les interactions en distanciel")

#a token is needed in token.txt
tokenfile = open("token.txt", "r")
token = tokenfile.readline()
tokenfile.close()

@bot.event
async def on_ready():
    print("ready")

@bot.command()
async def leverMain(ctx, *args):
    try:
        await ctx.message.delete()
    except:
        None

    prefix = "[✋]"
    member = ctx.author
    nick = member.display_name

    duration, msg = get_duration(args)

    if (has_nick_prefixe(nick, prefix)):
        await hand_already_raised(ctx, member)
    else:
        await raise_hand(ctx, member, prefix, duration, nick, msg)

#@bot.command()
#async def hello(ctx):
#    member = ctx.author
#    embedVar = discord.Embed(title=f'{member.display_name} dit hello', color=0xEC941C)
#    await ctx.send(embed=embedVar)

bot.run(token)