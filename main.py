#python3 main.py
import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix = "!", description = "Ce bot est là pour aider les étudiants à lever la mains pendant les cours pour participer")

#a token is needed in token.txt
tokenfile = open("token.txt", "r")
token = tokenfile.readline()
tokenfile.close()

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
      if random.randrange(num): continue
      line = aline
    return line

@bot.event
async def on_ready():
    print("ready")

@bot.command()
async def leverMain(ctx, *args):
    await ctx.message.delete()

    member = ctx.author
    
    if not args:
        time = 5
    else:
        try:
            time = int(args[0])
        except ValueError:
            time = 5


    nick = member.display_name

    if (nick[0:3] == "[✋]"):
        afile = open("crampe.txt", "r")
        status = random_line(afile)
        afile.close()
        await ctx.send(f'{member.mention}{status}')


    else:
        handRaisedName = "[✋] "+ nick

        op = ""
        try:
            await member.edit(nick=handRaisedName)
        except:
            op = "ne peux pas changer de pseudo mais"

        if time < 5:
            time = 5

        await ctx.send(f'{member.mention} {op} lève la main et risque d\'avoir une crampe dans {time} secondes')

        await asyncio.sleep(time)

        try:
            await member.edit(nick=nick)
        except:
            None



bot.run(token)


