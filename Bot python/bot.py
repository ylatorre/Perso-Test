import discord
from datetime import datetime
from discord.ext import commands
import sqlite3,mysql

bot = commands.Bot(command_prefix="?", description="Bot de Yvan")
# bot.remove_command('help')


TOKEN = "NjkwNjkxNTE4ODM4ODY2MDcw.XnVGmg.qlNJwGyz1nluNJExqqTXhIB5_h4"




@bot.event
async def on_ready():
    print(datetime.now())
    print("ready")
    # activity = discord.Game(name="Minecraft")
    # await bot.change_presence(status=discord.Status.idle, activity=activity)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="attentivement les personnes"))

# @bot.command(pass_context=True)
# async def help()


@bot.command(brief="Affiche Hello !!!", description="description")
async def hello(ctx):
    print("Hello !!")  # affiche dans la console
    await ctx.send("Hello !!!")  # affiche sur discord


@bot.command(brief="Afficher les informations du serveur")
async def serverinfo(ctx):
    server = ctx.guild
    serverName = server.name
    numberOfTextChannels = len(server.text_channels)
    serverdescrip = server.description
    numpersonne = server.member_count
    message = f"Vous etes sur le serveur de **{serverName}** et contient {numpersonne} personnes."
    await ctx.send(message)




@bot.command(brief='Supprime un nombre de message precedents definit',description="?sup 4\n supprimeras les 4 precedents message en plus du ?sup 4")
async def sup(ctx, nbredeligne: int):
    messages = await ctx.channel.history(limit=nbredeligne + 1).flatten()
    for message in messages:
        await message.delete()




@bot.command(brief='Repete X fois le message envoyez' ,description='ajouter une couleur parmis les suivants : \n Rouge')
async def sayXfois(ctx, number, couleur,*texte):
    if couleur.lower() == 'vert':
        for i in range(int(number)):
            mes = str(" ".join(texte))
            print(mes)
            retStr = str(f"""```css\n {mes}```""")
            await ctx.send(retStr)
            # embed = discord.Embed(title="Vert TEST")
            # embed.add_field(name="Nom sous titre couleur vert",value=retStr)
            # await ctx.send(embed=embed)
    else:
        await ctx.send('Autre')
        await ctx.send("```diff\n - du texte  et un tiret à chaque ligne```")
        for i in range(int(number)):
            texte2 = couleur + ' ' + " ".join(texte)
            await ctx.send(texte2)




@bot.command(brief="En cours de developpement")         
async def test(ctx, *args):
    retStr = str("""```css\nThis is some colored Text```""")
    embed = discord.Embed(title="Random test")
    embed.add_field(name="Name field can't be colored as it seems",value=retStr)
    await ctx.send(embed=embed)







@bot.command(brief="En cours de developpement")
async def vote(ctx, *choix: str):
    basevote = ['a', 'b', 'c']  # a remplacer par des émojis correspondant
    choixInter = " ".join(choix)
    choixfin = choixInter.split("|")
    raison = choixfin[0]
    # print(raison)
    # print(choixfin)
    message = await ctx.send(f"```{raison}```\n```{choixfin[1:]}```")
    # await message.add_reaction('👍')
    for i in range(len(choixfin)):
        
        await message.add_reaction(':regional_indicator_a:')



@bot.command(brief="Arrete le bot")
async def stop(ctx):
    # if message.content == '!stop': 
    activity = discord.Game(name="Hors ligne")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    await bot.logout()



@bot.command(brief="Affiche le lien github")
async def git(ctx):
    await ctx.send("""```https://github.com/ylatorre```\nhttps://github.com/ylatorre""")



@bot.command(brief="En cours de developpement")
async def anime(ctx,*nom):
    anime = str(" ".join(nom))
    
    print(anime)

# @bot.command()
# async def test(ctx):
#     await bot.wait_for("message", check = check)
# bot.user.setStatus('available')
bot.run(TOKEN)
