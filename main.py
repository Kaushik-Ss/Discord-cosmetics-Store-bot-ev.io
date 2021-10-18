import discord
import os
import requests
import json
import datetime
import asyncio
import random
import pprint
from discord.ext import tasks
from keep_alive import keep_alive
from better_profanity import profanity


k = "*"

URL = "https://ev.io/storefront"
page = requests.get(URL)
j = page
print(page)
if page != "<Response [200]>":
    k = ""
file = []
for i in page.json():
    file.append(i)

client = discord.Client()

# @client.command()
# async def embed():

Temp="A new skin is available in the store at ev.io? It will be in the store for the next 24 hours."
print(file)

@client.event
async def on_ready():
    # channel = client.get_channel(851999924056227840)
    # await channel.send("?b")
    print("We have logged in as{0.user}".format(client))
    

@tasks.loop(hours=24.0) 
async def send_message():
  # channel = client.get_channel(851909479351975972)
  # channel.send("?b")
  
  channel = client.get_channel(851999924056227840)
  channel.send("?b")

n = 0
json_data = json.loads(page.text)

  
@client.event
async def on_message(message):
    curseWord = ['fuck','fool','fishook','ribbons','weed',"rabbit","moderator","panda","ari",'rickrolls','cah','rickroll','mod','hax','hacks','bitch','crap','shit']
    curse_reply=['https://imgur.com/y8Ea8jB','https://i.kym-cdn.com/photos/images/original/002/090/742/7c7.jpg','https://tenor.com/bl0IR.gif','https://tenor.com/bfytM.gif']
    curse_random=random.choice(curse_reply)
    global k, page, j
    if message.content.startswith("?store change"):
        global Temp
        k=str(message.content)[13:]
        Temp=k
            
    if message.content.startswith("?store help"):
        embed = discord.Embed(title="ev.io", value=" :wave:", color=0x109319)
        embed.add_field(name="Help",
                        value="└Use ?help\n*to get bot info*",
                        inline=False)
        embed.add_field(name="Rotation information",
                        value="└Use ?store\n*to get skin info*",
                        inline=False)
        embed.add_field(name="Change time name/title card of the message",
                        value="""└Use ?store change (insert new string)\n*to change the name of the message""",
                        inline=False)
        embed.add_field(name="Small image of skins",
                        value="""└Use ?store small (insert skin name)\n*to get the thumbnail of the skin
                        NOTE- not availabe for weapon skins*""",
                        inline=False)
        await message.channel.send(embed=embed)

    if j != page:
        await message.channel.send("?store")
    if (message.content.startswith("?store small") or message.content.startswith("?store small") ) and len(message.content) >=7 :
      needed=message.content
      needed=needed[13:]
      print(needed)
      try:
        needed=needed.replace("wave","shack")
      except:
        print("True")
      embed = discord.Embed(colour=discord.Color.from_rgb(225, 198, 153),title="ev.io",value=needed)
      k=needed
      head=k[0].lower()+k[1:]+"_head.png"
      if "<Response [404]>"==str(requests.get
      ("https://ev.io/sites/default/files/skin_profile_thumbs/"+head)):
              head=k[0].lower()+k[1:]+"_head%20%281%29.png"
      embed.set_image(url="https://ev.io/sites/default/files/skin_profile_thumbs/"+head)
      await message.channel.send(embed=embed)

    if (message.content.startswith("?store") or message.content.startswith("?store") ) and len(message.content) <= 7:
        URL = "https://ev.io/storefront"
        page = requests.get(URL)
        j = page
        print(page)
        if page != "<Response [200]>":
         k = ""
        file = []
        for i in page.json():
         file.append(i)
        json_data = json.loads(page.text)  
        for i in range(len(file)):
            embed = discord.Embed(colour=discord.Color.from_rgb(225, 198, 153),title="ev.io",
                                  value=json_data[i]['title'])
            if json_data[i]['type'] == 'Player Skin':
                url_i = "https://ev.io" + json_data[i]['field_large_thumb']
                k=str(json_data[i]['title'])
                head=k[0].lower()+k[1:]+"_head.png"
                if "<Response [404]>"==str(requests.get("https://ev.io/sites/default/files/skin_profile_thumbs/"+head)):
                 head=k[0].lower()+k[1:]+"_head%20%281%29.png"
                if "<Response [404]>"==str(requests.get("https://ev.io/sites/default/files/skin_profile_thumbs/"+head)):
                 head=k[0]+k[1:]+"_head%20%281%29.png"
                if "<Response [404]>"==str(requests.get("https://ev.io//sites/default/files/skin_profile_thumbs/"+head)):
                 head=k[0].upper()+k[1:]+"_head%20%281%29.png" 
                if "<Response [404]>"==str(requests.get("https://ev.io/sites/default/files/skin_profile_thumbs/"+head)):
                 head=k[0]+k[1:]+"_head.png"
                try:
                   head=head.replace("wave","shack")
                except:
                     print("True")
                if "<Response [404]>"!=str(requests.get("https://ev.io/sites/default/files/skin_profile_thumbs/"+head)):
                    embed.set_thumbnail(url="https://ev.io/sites/default/files/skin_profile_thumbs/"+head)
                else:
                    embed.set_thumbnail(url="https://ev.io//sites/default/files/skin_profile_thumbs/"+head)
            else:
                url_i = "https://ev.io" + json_data[i][
                    'field_weapon_skin_thumb']

            # embed.set_author(name=Temp,
            #                  url="https://ev.io/node/"+json_data[i]['nid'],
            #                  icon_url="https://ev.io/themes/ev/logo.png")
            embed.set_author(name=Temp,
                             url="https://ev.io/node/"+json_data[i]['nid'],
                             icon_url="https://cdn.discordapp.com/icons/840042875805892649/edc19c9bde59d03a4b90f89c43e83e6f.png?size=128")
            
            embed.set_image(url=url_i)
            embed.add_field(name="```Skin type```",
                            value=json_data[i]['type'],
                            inline=True)
                            
            embed.add_field(name="```Name```",
                            value=json_data[i]['title'],
                            inline=False)
                            
            embed.add_field(name="```Tier```",
                            value=json_data[i]['field_tier'],
                            inline=False)
            embed.add_field(name="```Cost```",
                            value=json_data[i]['field_cost'],
                            inline=False)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text='ev.io')
            await message.channel.send(embed=embed)
    msg_content = message.content.lower()

    
    
    # # delete curse word if match with the list
    for i in msg_content.split():
      if i in curseWord:
        print(msg_content.split())
        await message.channel.send(curse_random)
    # text = msg_content
    # censored = profanity.censor(text,'$')
    # print(censored)
    # await message.channel.send("Please use '"+censored+"'")
        #await message.channel.send("?b")  #delete this    
keep_alive()
while True:
  keep_alive()
  client.run('ODkyMzg2Njk0OTg3Mzk1MDcz.YVMJ3w.cyPHmaZTPik_x0e1pTaNcUStoDc')
    


