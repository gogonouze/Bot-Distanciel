import asyncio
import random
import discord

def random_line(afile):
    """chose a random line in a textfile"""
    line = next(afile)
    for num, aline in enumerate(afile, 2):
      if random.randrange(num): continue
      line = aline
    return line


def get_duration(args):
    """ gives a valid duration and a message if the duration is too long"""
    msg = ""

    if not args:
        duration = 10
    else:
        try:
            duration = int(args[0])
            if duration < 5:
                duration = 5
            if duration > 60:
                duration = 60 
                msg = " se croit malin mais regrette un peu. Il"
        except ValueError:
            duration = 10
    return duration, msg


def has_nick_prefixe (nick, prefix):
    """gives true if nick has a prefix, else false """
    return nick[0:len(prefix)] == prefix


async def hand_already_raised(ctx, member):
    """
    send a random Discord message to tell user is already raising his hand"
    """
    afile = open("crampe.txt", "r")
    status = random_line(afile)
    afile.close()
    embedVar = discord.Embed(title=f'{member.display_name}{status}', color=0xEC941C)
    await ctx.send(embed=embedVar)


async def raise_hand(ctx, member, prefix, duration, nick, msg):
    """send a Discord message to tell user is raising his hand for X seconds"""
    handRaisedName = prefix+" "+ nick

    op = ""
    try:
       await member.edit(nick=handRaisedName)
    except:
        op = " ne peux pas changer de pseudo mais"
        handRaisedName = nick #see below

    #instead of handRaisedName, it must be member.display_name. But the nickname doesn't change fast enough /shrug
    embedVar = discord.Embed(title=f'{handRaisedName}{op}{msg} lève la main et risque d\'avoir une crampe dans {duration} secondes',description="commande = !leverMain", color=0xEC941C)
    await ctx.send(embed=embedVar)

    await asyncio.sleep(duration)

    try:
        await member.edit(nick=nick)
    except:
        None
        