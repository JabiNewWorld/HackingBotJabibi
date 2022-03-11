import random 
import discord
import asyncio as req
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument as req 
from discord.ext.commands import CommandNotFound as req 
import requests
from urllib.request import Request, urlopen
import socket
import json
from discord import Webhook
import aiohttp
import discord, ctypes, json, os, webbrowser, requests, datetime, urllib, time, string, random, asyncio, aiohttp
from urllib.request import urlcleanup, urlopen
from json import loads, dumps
from urllib.request import Request, urlopen
from discord import channel as req 
from discord import embeds as req
from discord import user as req 



TOKEN = "AQUI PONES EL TOKEN DE TU BOT" #PARA TOKEN DEL BOT



intents = discord.Intents(messages=True, guilds=True)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!")

intents = discord.Intents().default()
intents.members = True
client = discord.Client(intents=intents)

bot.remove_command('help')

print(f"""
      
       ▄▄▄██▀▀▀▄▄▄       ▄▄▄▄    ██▓ ▄▄▄▄    ██▓    ▄▄▄▄    ▒█████  ▄▄▄█████▓
   ▒██  ▒████▄    ▓█████▄ ▓██▒▓█████▄ ▓██▒   ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
   ░██  ▒██  ▀█▄  ▒██▒ ▄██▒██▒▒██▒ ▄██▒██▒   ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▓██▄██▓ ░██▄▄▄▄██ ▒██░█▀  ░██░▒██░█▀  ░██░   ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
 ▓███▒   ▓█   ▓██▒░▓█  ▀█▓░██░░▓█  ▀█▓░██░   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
 ▒▓▒▒░   ▒▒   ▓▒█░░▒▓███▀▒░▓  ░▒▓███▀▒░▓     ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
 ▒ ░▒░    ▒   ▒▒ ░▒░▒   ░  ▒ ░▒░▒   ░  ▒ ░   ▒░▒   ░   ░ ▒ ▒░     ░    
 ░ ░ ░    ░   ▒    ░    ░  ▒ ░ ░    ░  ▒ ░    ░    ░ ░ ░ ░ ▒    ░      
 ░   ░        ░  ░ ░       ░   ░       ░      ░          ░ ░           
                        ░           ░              ░                   
      """)


@bot.event
async def on_ready():
      print("====================")
      print("INFO PYTHON BOT DE JABIBI ESTA ACTIVO")
      print("====================")
  
@bot.event
async def on_member_join(member , ctx): 
   guild = ctx.guild
   guild = bot.get_guild(937392395056734280)
   channel = guild.get_channel(949415755043192842)
   await ctx.send(f"{member.mention} a entrado al server")
   await ctx.guild.send(f" bienvenido al {guild.name} {member.name}")

@bot.command()
async def ayuda(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
    title = ('💎AYUDA DE COMANDOS Y PARA ENTENDER MEJOR ESTE BOT💎'),
    description = ("😎ESTE BOT CREADO POR JABIBI ES PARA QUE APRENDAS A ENTENDER LOS COMMANDOS Y EL BOT EN SI😁"),
    colour = discord.Colour.random(),
    )
    embed.set_image(url="https://media.discordapp.net/attachments/848250303731990528/864181493659074570/a_fdaeab4ddedcacc5000d8ea257c52ee1.gif")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/848250303731990528/864181493659074570/a_fdaeab4ddedcacc5000d8ea257c52ee1.gif")
    embed.add_field(name="!ayuda PARA help", value="PARA APRENDER A USAR LOS COMANDOS", inline=True)
    embed.add_field(name="!partner", value="ESA PARA HACER PROMOCION DE TU SERVER", inline=True)
    embed.add_field(name="!infouser", value="ESTE COMANDO SE USA ")
    await ctx.send(embed=embed)   

@bot.command()
async def userinfo(ctx, *, user: discord.User = None): # b'\xfc'
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    embed.set_footer(text="CREATED BYJABIBI HACKING: ID:"  + str(user.id))
    return await ctx.send(embed=embed)
    
@bot.command(name='avatar', help='fetch avatar of a user')
async def avatar(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)


format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

@client.command()
@commands.guild_only()
async def serverinfo(ctx):
    embed = discord.Embed(
        color = ctx.guild.owner.top_role.color
    )
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    embed.add_field(name = f"Information About **{ctx.guild.name}**: ", value = f":white_small_square: ID: **{ctx.guild.id}** \n:white_small_square: Owner: **{ctx.guild.owner}** \n:white_small_square: Location: **{ctx.guild.region}** \n:white_small_square: Creation: **{ctx.guild.created_at.strftime(format)}** \n:white_small_square: Members: **{ctx.guild.member_count}** \n:white_small_square: Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories \n:white_small_square: Verification: **{str(ctx.guild.verification_level).upper()}** \n:white_small_square: Features: {', '.join(f'**{x}**' for x in ctx.guild.features)} \n:white_small_square: Splash: {ctx.guild.splash}")
    await ctx.send(embed=embed)
    
@bot.command(pass_context=True)
async def getip(ctx, *, ip = None,user: discord.User = None): 
    await ctx.message.delete()
    if ip is None:   
     if user is None:
        user = ctx.author
        ip = ip
        localhost = ip
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)  
    ip = requests.get('https://api.ipify.org/').text
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
    geo = r.json()
    embed = discord.Embed(title="GEOIP INFORMACION DE LA IP DEL USUARIO",  colour = discord.Colour.blue())
    embed.set_author(name=f"IP GRABBER BY JABIBI CODING")
    embed.add_field(name=f'`\nIP PRIVADA DEL USUARIO`: {user}', value=IPAddr, inline=False)
    embed.add_field(name=f'`\nIP PUBLICA DEL USUARIO`: {user}', value=ip, inline=False)
    embed.add_field(name=f'`\nId Del Usuario`', value=user, inline=True)
    embed.add_field(name='`\nIPTYPE`', value=geo['ipType'], inline=True)
    embed.add_field(name='`\nCountry`', value=geo['country'], inline=True)
    embed.add_field(name='`\nCity`', value=geo['city'], inline=True)
    embed.add_field(name='`\nRegion`', value=geo['region'], inline=True)
    embed.add_field(name='`\nContinent`', value=geo['continent'], inline=True) 
    embed.add_field(name='`\nStatus`', value=geo['status'], inline=True)
    embed.add_field(name='`\nIpname`', value=geo['ipName'], inline=True)
    embed.add_field(name='`\nCOMPUTER NAME?`', value=hostname, inline=True)
    embed.add_field(name='`\nHOST?' , value=localhost, inline=True)
    embed.set_image(url="https://cdn.discordapp.com/avatars/852727930802274304/a_45a739efc7794250f233c429b39c2ccb.gif?size=2048")
    embed.set_footer(text=f"Creado Por CodeJH: runed by {user}")
    await ctx.send(embed=embed)

@bot.command()
async def usuario(ctx, *, user: discord.User = None):  
    await ctx.message.delete()
    if user is None: 
        user = ctx.author
        guild = ctx.guild   
    embed = discord.Embed(title="USUARIO INFO", colour = discord.Colour.default())
    embed.set_author(name=f"GENERAL INFOMATION")
    embed.add_field(name=f"USER>>>", value=user, inline=False)
    embed.add_field(name=f"ID DEL USER>>>", value=user.id, inline=False)
    embed.add_field(name=f"CUENTA CREADA>>>", value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
    embed.add_field(name=f"ENTRO AL SERVER?>>>", value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
    embed.set_footer(text="🔥creado por jabibicoding🔥")
    embed.set_image(url=user.avatar_url)    
    await ctx.send(embed=embed)  
   

@bot.command(pass_context=True)
async def ipuser(ctx, *, ip = None, user: discord.User = None):
  await ctx.message.delete()
  if user is None:
    user = ctx.author
    if ip is None:
      ip = ip
  ip = requests.get("https://api.ipify.org/").text
  r = requests.get(f"http://extreme-ip-lookup.com/json/{ip}")
  geo = r.json()
  embed = discord.Embed(title="IP LOGGER USER BY MOHAMED", colour = 
  discord.Colour.random())
  embed.set_author(name=f"{user.name}", icon_url=f"{user.avatar_url}")
  embed.set_thumbnail(url=user.avatar_url)
  embed.add_field(name=f"`IP DEL USUARIO {user.name}`", value=ip, 
  inline=False)
  embed.add_field(name=f"USUARIO {user.name}", value=user, inline=False)
  await ctx.send(embed=embed)
  
  
    
bot.run("TOKEN", bot=True)
