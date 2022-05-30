import discord
from discord.ext import commands
from discord.utils import get
from PIL import Image, ImageChops, ImageDraw, ImageFont
from io import BytesIO


"""
8888888888                         888    d8b                            
888                                888    Y8P                            
888                                888                                   
8888888  .d88b.  88888b.   .d8888b 888888 888  .d88b.  88888b.  .d8888b  
888     d88""88b 888 "88b d88P"    888    888 d88""88b 888 "88b 88K      
888     888  888 888  888 888      888    888 888  888 888  888 "Y8888b. 
888     Y88..88P 888  888 Y88b.    Y88b.  888 Y88..88P 888  888      X88 
888      "Y88P"  888  888  "Y8888P  "Y888 888  "Y88P"  888  888  88888P'

"""

def circle(pfp,size = (215,215)):

    pfp = pfp.resize(size, Image.LANCZOS).convert("RGBA")  # pfp = pfp.resize(size, Image.LANCZOS).convert("RGBA")

    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.LANCZOS)  # mask = mask.resize(pfp.size, Image.LANCZOS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp





"""
8888888                   888                                                
  888                     888                                                
  888                     888                                                
  888   88888b.  .d8888b  888888  8888b.  88888b.   .d8888b .d88b.  .d8888b  
  888   888 "88b 88K      888        "88b 888 "88b d88P"   d8P  Y8b 88K      
  888   888  888 "Y8888b. 888    .d888888 888  888 888     88888888 "Y8888b. 
  888   888  888      X88 Y88b.  888  888 888  888 Y88b.   Y8b.          X88 
8888888 888  888  88888P'  "Y888 "Y888888 888  888  "Y8888P "Y8888   88888P' 

"""

f = open('token.txt','r')
TOKEN = str(f.read())
f.close()

CONST_TROPHEES = {
    "0️⃣":979351436146118698,
    "1️⃣":979351590878199878,
    "2️⃣":979351700332761138,
    "3️⃣":979351774181879839,
}

STATUS_MOOVE = {
    None:False
}


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = '*', description = '',intents=intents)





"""


 .d8888b.  888                     888                    
d88P  Y88b 888                     888                    
Y88b.      888                     888                    
 "Y888b.   888888  8888b.  888d888 888888 .d88b.  888d888 
    "Y88b. 888        "88b 888P"   888   d8P  Y8b 888P"   
      "888 888    .d888888 888     888   88888888 888     
Y88b  d88P Y88b.  888  888 888     Y88b. Y8b.     888     
 "Y8888P"   "Y888 "Y888888 888      "Y888 "Y8888  888  


"""

@bot.event
async def on_ready():
    print("-----------")
    print('\nBot Operationnel\n')
    await bot.change_presence(activity=discord.Game(name="Clash Royale"))
    print("-----------")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    pass





"""
  888888          d8b                      d88P      888                                         
    "88b          Y8P                     d88P       888                                         
     888                                 d88P        888                                         
     888  .d88b.  888 88888b.           d88P         888      .d88b.   8888b.  888  888  .d88b.  
     888 d88""88b 888 888 "88b         d88P          888     d8P  Y8b     "88b 888  888 d8P  Y8b 
     888 888  888 888 888  888        d88P           888     88888888 .d888888 Y88  88P 88888888 
     88P Y88..88P 888 888  888       d88P            888     Y8b.     888  888  Y8bd8P  Y8b.     
     888  "Y88P"  888 888  888      d88P             88888888 "Y8888  "Y888888   Y88P    "Y8888  
   .d88P                                                                                         
 .d88P"                                                                                          
888P"                                                                                            
          
"""

@bot.event
async def on_member_join(member):

    #Canvas de Join
    channelJoin = bot.get_guild(965709687406354503).get_channel(979533133890326528)

    name = str(member)

    base = Image.open("base.png").convert("RGBA")

    pfp = member.avatar_url_as(size=256)
    data = BytesIO(await pfp.read())
    pfp = Image.open(data).convert("RGBA")

    name = f"{name[:12]}.." if len(name) > 12 else name

    draw = ImageDraw.Draw(base)
    pfp = circle(pfp,(398,398))
    font = ImageFont.truetype("Nunito-Regular.ttf",140)
    #571-484
    draw.text((490,330), name, font=font)
    base.paste(pfp,(55,141),pfp)

    with BytesIO() as a:
        base.save(a,"PNG")
        a.seek(0)
        await channelJoin.send(f"Bienvenue à toi {member.mention} !",file= discord.File(a,"file.png"))

    #Edit de nom Vocal Member Count +
    channelCount = bot.get_guild(965709687406354503).get_channel(980927535837765672)
    memberCount = bot.get_guild(965709687406354503).member_count
    newName = f"Member Count : {memberCount} 📈"
    await channelCount.edit(name=newName)


@bot.event
async def on_member_remove(member):

    ##Edit de nom Vocal Member Count -
    channelCount = bot.get_guild(965709687406354503).get_channel(980927535837765672)
    memberCount = bot.get_guild(965709687406354503).member_count
    newName = f"Member Count : {memberCount} 📉"
    await channelCount.edit(name=newName)





"""
 .d8888b.                    888    d8b                        888     888                                              
d88P  Y88b                   888    Y8P                        888     888                                              
888    888                   888                               888     888                                              
888         .d88b.  .d8888b  888888 888  .d88b.  88888b.       Y88b   d88P  .d88b.   .d8888b  8888b.  888  888 888  888 
888  88888 d8P  Y8b 88K      888    888 d88""88b 888 "88b       Y88b d88P  d88""88b d88P"        "88b 888  888 `Y8bd8P' 
888    888 88888888 "Y8888b. 888    888 888  888 888  888        Y88o88P   888  888 888      .d888888 888  888   X88K   
Y88b  d88P Y8b.          X88 Y88b.  888 Y88..88P 888  888         Y888P    Y88..88P Y88b.    888  888 Y88b 888 .d8""8b. 
 "Y8888P88  "Y8888   88888P'  "Y888 888  "Y88P"  888  888          Y8P      "Y88P"   "Y8888P "Y888888  "Y88888 888  888

"""

@bot.event
async def on_voice_state_update(member, before, after):

    #Quand il se connecte pure pour creer
    if not before.channel and after.channel and after.channel.id == 980073096906149938:  #  and member.id == 389438982133645312
        nomVoc = f"Vocal de {member.name}"
        category = discord.utils.get(member.guild.categories, id=978995213295038536)
        await member.guild.create_voice_channel(nomVoc, category=category, position=6)
        channels = category.channels
        for c in channels:
            if c.name == f"Vocal de {member.name}":
                id = c.id
        channelCreated = bot.get_channel(id)
        await member.move_to(channelCreated)

    #Quand il se deconnecte pure pour quitter
    elif not after.channel and before.channel and before.channel.name[:8] == "Vocal de":
        members = before.channel.members
        if members == []:
            await before.channel.delete()





"""
8888888b.                            888    d8b                            
888   Y88b                           888    Y8P                            
888    888                           888                                   
888   d88P .d88b.   8888b.   .d8888b 888888 888  .d88b.  88888b.  .d8888b  
8888888P" d8P  Y8b     "88b d88P"    888    888 d88""88b 888 "88b 88K      
888 T88b  88888888 .d888888 888      888    888 888  888 888  888 "Y8888b. 
888  T88b Y8b.     888  888 Y88b.    Y88b.  888 Y88..88P 888  888      X88 
888   T88b "Y8888  "Y888888  "Y8888P  "Y888 888  "Y88P"  888  888  88888P'

"""

@bot.event
async def on_raw_reaction_add(payload):

    #Infos
    guild = bot.get_guild(payload.guild_id)
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    user = guild.get_member(payload.user_id)

    # Auto Role Trophées +
    if message.id == 979350948671537173:  
        if str(payload.emoji) in CONST_TROPHEES.keys():
            role = get(guild.roles, id=CONST_TROPHEES[str(payload.emoji)])
            await user.add_roles(role)
            print(f"\n{user.name} hérite désormais du rôle : {role.name}")

    # Changement Pseudo WP +
    if message.id == 979430376881659914:  
        if str(payload.emoji) == "✨":
            newUser = f"WP | {user.name}"
            try:
                await user.edit(nick=newUser)
                print(f"\nLe joueur {user.name} à changé son pseudo avec WP Edit")
            except discord.errors.Forbidden:
                await user.send("Le Bot ne peut pas modifier votre pseudo car il n'en a pas les droits")


@bot.event
async def on_raw_reaction_remove(payload):

    #Infos
    guild = bot.get_guild(payload.guild_id)
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    user = guild.get_member(payload.user_id)

    # Auto Role Trophées -
    if message.id == 979350948671537173:
        if str(payload.emoji) in CONST_TROPHEES.keys():
            role = get(guild.roles, id=CONST_TROPHEES[str(payload.emoji)])
            await user.remove_roles(role)
            print(f"\n{user.name} n'hérite désormais plus du rôle : {role.name}")

    # Changement Pseudo WP -
    if message.id == 979430376881659914:
        if str(payload.emoji) == "✨":
            newUser = f"{user.name}"
            try:
                await user.edit(nick=newUser)
                print(f"\nLe joueur {user.name} à remis son pseudo avec WP Edit")
            except discord.errors.Forbidden:
                pass





"""
 .d8888b.                                                              888                   
d88P  Y88b                                                             888                   
888    888                                                             888                   
888         .d88b.  88888b.d88b.  88888b.d88b.   8888b.  88888b.   .d88888  .d88b.  .d8888b  
888        d88""88b 888 "888 "88b 888 "888 "88b     "88b 888 "88b d88" 888 d8P  Y8b 88K      
888    888 888  888 888  888  888 888  888  888 .d888888 888  888 888  888 88888888 "Y8888b. 
Y88b  d88P Y88..88P 888  888  888 888  888  888 888  888 888  888 Y88b 888 Y8b.          X88 
 "Y8888P"   "Y88P"  888  888  888 888  888  888 "Y888888 888  888  "Y88888  "Y8888   88888P' 

"""

@bot.command()
async def carte(ctx, *args):

    #Jolie carte de présentation CR
    if ctx.channel.id == 965711530136076378:
        try:
            pseudo, tr, pb, deck, ccsc, about = args
            bug = False
        except:
            await ctx.reply(f"Salut {ctx.author.mention} voilà comment on utilise la commande :\n*carte <pseudo> <trophees> <pb> <deck> <CS/SC> <A-Propos>")
            bug = True

        if not bug:
            tr = int(tr)
            
            base = Image.open("basecarte.png").convert("RGBA")
            if tr >= 0 and tr < 5300:
                loc = "logo/c1.png"
            elif tr >= 5300 and tr < 5600:
                loc = "logo/c2.png"
            elif tr >= 5600 and tr < 6000:
                loc = "logo/c3.png"
            elif tr >= 6000 and tr < 6300:
                loc = "logo/m1.png"
            elif tr >= 6300 and tr < 6600:
                loc = "logo/m2.png"
            elif tr >= 6600 and tr < 7000:
                loc = "logo/m3.png"
            elif tr >= 7000 and tr < 7300:
                loc = "logo/z1.png"
            elif tr >= 7300 and tr < 7600:
                loc = "logo/z2.png"
            elif tr >= 7600 and tr < 8000:
                loc = "logo/z3.png"
            elif tr >= 8000:
                loc = "logo/z4.png"
            background = Image.open(loc).convert("RGBA")

            pfp = ctx.author.avatar_url_as(size=256)
            data = BytesIO(await pfp.read())
            pfp = Image.open(data).convert("RGBA")

            name = f"{ctx.author.name[:16]}.." if len(ctx.author.name) > 16 else ctx.author.name
            pseudo = f"{pseudo[:16]}.." if len(pseudo) > 16 else pseudo

            draw = ImageDraw.Draw(base)
            pfp = circle(pfp,(256,256))
            font = ImageFont.truetype("Nunito-Regular.ttf",38)
            subfont = ImageFont.truetype("Nunito-Regular.ttf",25)

            draw.text((300,240),name,font=font)
            draw.text((65,490),pseudo,font=subfont)
            draw.text((405,490),str(tr),font=subfont)
            draw.text((65,635),pb,font=subfont)
            draw.text((405,635),deck,font=subfont)
            draw.text((65,770),ccsc,font=subfont)
            draw.text((405,770),about,font=subfont)

            base.paste(pfp,(37,159),pfp)

            background.paste(base,(0,0),base)

            with BytesIO() as a:
                background.save(a,"PNG")
                a.seek(0)
                await ctx.reply(file = discord.File(a,"carte.png"))
    else:
        await ctx.reply(f"Salut {ctx.author.mention}, essaye ici ! <#965711530136076378>")

@bot.command()
async def snipe(ctx, *args):
    #Snipe a travailler
    pseudo = ""
    for e in args:
        pseudo = pseudo + e
        pseudo+="+"
    toSend = f"https://royaleapi.com/player/search/results?q={pseudo}"
    await ctx.reply(toSend)


"""
@bot.command()
async def Test(ctx,member:discord.Member=None):
    if not member:
        member = ctx.author

    name = str(member)

    base = Image.open("base.png").convert("RGBA")

    pfp = member.avatar_url_as(size=256)
    data = BytesIO(await pfp.read())
    pfp = Image.open(data).convert("RGBA")

    name = f"{name[:12]}.." if len(name) > 12 else name

    draw = ImageDraw.Draw(base)
    pfp = circle(pfp,(398,398))
    font = ImageFont.truetype("Nunito-Regular.ttf",140)
    #571-484
    draw.text((490,330), name, font=font)
    base.paste(pfp,(55,141),pfp)

    with BytesIO() as a:
        base.save(a,"PNG")
        a.seek(0)
        await ctx.send(file= discord.File(a,"file.png"))

@bot.command()
async def setup(ctx):
    embed=discord.Embed(title="AUTO-ROLE TROPHEES", description="Choisissez vos rôles trophées pour le serveur discord grâce aux réactions !", color=0xffde05)
    embed.set_author(name="WAR PHANTOMS BOT", icon_url="https://imgur.com/XdogjqR.png")
    embed.add_field(name="7000TR + :  3️⃣", value="\u200b", inline=False)
    embed.add_field(name="6600TR + :  2️⃣", value="\u200b", inline=False)
    embed.add_field(name="6000TR + :  1️⃣", value="\u200b", inline=False)
    embed.add_field(name="-6000TR  :  0️⃣", value="\u200b", inline=False)
    embed.set_footer(text="En cas de problème merci de contacter un superieur.")
    await ctx.send(embed=embed)

@bot.command()
async def setup2(ctx):
    embed=discord.Embed(title="AUTO-PSEUDO WP |", description="Pour placer 'WP |' devant son pseudo ! (Réservé aux membres du clan)", color=0xffde05)
    embed.set_author(name="WAR PHANTOMS BOT", icon_url="https://imgur.com/XdogjqR.png")
    embed.add_field(name="Cliquez simplement sur la réaction : ✨", value="\u200b", inline=False)
    embed.set_footer(text="En cas de problème merci de contacter un superieur.")
    await ctx.send(embed=embed)
"""



"""
8888888b.                    
888   Y88b                   
888    888                   
888   d88P 888  888 88888b.  
8888888P"  888  888 888 "88b 
888 T88b   888  888 888  888 
888  T88b  Y88b 888 888  888 
888   T88b  "Y88888 888  888 

"""
bot.run(TOKEN)