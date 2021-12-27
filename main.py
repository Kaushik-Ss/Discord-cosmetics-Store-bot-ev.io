import discord
import os
import requests
import json
import datetime
import asyncio
import random
import pprint
from discord import Embed
from discord.ext import tasks
from keep_alive import keep_alive
from better_profanity import profanity
from replit import db
from imdb import IMDb
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from datetime import datetime, timedelta
from pytz import timezone
import pytz
import time
import pandas as pd
import datetime


def getlink(link):
    k = ""
    soup = BeautifulSoup(requests.get(link, 'lxml'))
    for entry in soup.find_all("style-scope ytd-item-section-renderer"):
        for link in entry.find_all("link"):
            k += link["href"]
            break
        break
    return k


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

Temp = "A new skin is available in the store at ev.io? It will be in the store for the next 24 hours."
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
    curseWord = [
        'fuck', 'fool', 'fishook', 'ribbons', 'weed', "r@bbit", "moderator",
        "panda", "ari", 'rickr@lls', 'c@h', 'rickroll', 'm@d', 'hax', 'h@cks',
        'bitch', 'crap', 'shi@t'
    ]
    curse_reply = [
        'https://imgur.com/y8Ea8jB',
        'https://i.kym-cdn.com/photos/images/original/002/090/742/7c7.jpg',
        'https://tenor.com/bl0IR.gif', 'https://tenor.com/bfytM.gif'
    ]
    curse_random = random.choice(curse_reply)
    global k, page, j
    if message.content.startswith("?store change"):
        global Temp
        k = str(message.content)[13:]
        Temp = k
    if (message.content.startswith("!mov")
            or message.content.startswith("!mov")):
        x = str(message.content)[5:]
        ia = IMDb()
        str_qu = x.split()
        str_qu = "+".join(str_qu)
        movie = ia.search_movie(x)
        id = []
        for i in range(2):
            id.append(movie[i].movieID)
        sel = id[0]
        sel_mov = ia.get_movie(sel)
        name = sel_mov['title']
        embed = discord.Embed(title=name, value=x, color=0x109319)
        embed.add_field(name='Name', value=name, inline=True)
        try:
            yer = sel_mov['year']
        except:
            yer = "Year of release missing"

        embed.add_field(name='Year of release', value=yer, inline=True)

        try:
            kind = sel_mov['kind']
        except:
            kind = "mixed"
        embed.add_field(name='Type', value=kind, inline=True)

        try:
            rat = sel_mov['rating']
        except:
            rat = "Rating missing"
        embed.add_field(name='Ratings :popcorn:', value=rat, inline=False)

        try:
            url_i = sel_mov['cover url'][:-15]
        except:
            url_i = 'https://via.placeholder.com/300/000000/FFFFFF/?text=No+Image'

        try:
            times = sel_mov['runtimes'][0]
        except:
            times = "Variable"
        embed.add_field(name='Runtime', value=times, inline=False)
        pl = ''
        try:
            if yer == 2021 or yer == 2022:
                pl += "||"
            pl += sel_mov['plot outline']
            if yer == 2021 or yer == 2022:
                pl += "||"
        except:
            pl = "Too old or Too new"
        embed.add_field(name='Plot outline', value=pl, inline=False)
        try:
            if kind == "tv series":
                no = sel_mov['number of episodes']
                embed.add_field(name='Total No of episodes',
                                value=no,
                                inline=False)
                no_season = sel_mov['number of seasons']
                embed.add_field(name='No of seasons',
                                value=no_season,
                                inline=False)
        except:
            print('somethin')
        try:
            gen = " ".join(sel_mov['genres'])
        except:
            gen = "Not decided"
        embed.add_field(name='Genre', value=gen, inline=False)

        # rating_c=sel_mov['certificates']
        # __=" ".join(rating_c)
        # embed.add_field(name='Certificates ', value=__, inline=False)

        embed.set_image(url=url_i)
        url_yt = "https://www.youtube.com/results?search_query=" + str_qu + "+official+" + "trailer"

        embed.add_field(name='Trailer link', value=url_yt, inline=False)

        await message.channel.send(embed=embed)
    if (message.content.startswith("?time")
            or message.content.startswith("?Time")):
        if str(message.author) == "JetFlash#8237":
            first_embed = Embed(title='Gimme a min')
            message = await message.channel.send(embed=first_embed)
            while True:
                new_embed = Embed(title='Time around the world')
                naive = datetime.now()
                timelis = [
                    "Australia/Sydney", "Asia/Kolkata", "Asia/Singapore",
                    "Asia/Jakarta", "Asia/Jerusalem", "Asia/Tokyo",
                    'Asia/Shanghai', "Europe/Stockholm", "America/Chicago",
                    "America/Los_Angeles", "America/Los_Angeles",
                    'America/New_York'
                ]
                for i in timelis:
                    timezone = pytz.timezone(i)
                    aware1 = naive.astimezone(timezone)
                    __ = str(aware1)[:-21]
                    __ += "--"
                    __ += str(aware1)[-21:-16]
                    new_embed.add_field(name=i, value=__, inline=True)
                time.sleep(1)
                await message.edit(embed=new_embed)
        else:
            await message.channel.send("Not owner")
    if (message.content.startswith("?cxp")
            or message.content.startswith("?Cxp")):
        if str(message.author) == "JetFlash#8237":
            first_embed = Embed(title='Gimme a min')
            message = await message.channel.send(embed=first_embed)
            while True:
                new_embed = discord.Embed(title=".",
                                          value="?Cp",
                                          color=0x109319)
                base_url = 'https://ev.io/clans'
                r = requests.get(base_url)
                html = r.content
                soup = BeautifulSoup(html, 'lxml')
                table = soup.find('table')
                row = table.find_all('tr')
                clans = [x.contents[-4].text.strip() for x in row[1:]]
                clans_name = [
                    x.contents[3].text.strip('\n')[2:] for x in row[1:]
                ]
                points = pd.DataFrame()
                points['Clan name'] = clans
                points['Cp this week'] = clans_name
                new_embed.add_field(name="Clan bot",
                                    value=points.to_string(index=False)[:500],
                                    inline=False)
                new_embed.set_footer(text="List updated every minute")
                time.sleep(60)
                await message.edit(embed=new_embed)
        else:
            await message.channel.send("Not owner")

    if message.content.startswith("?store help"):
        embed = discord.Embed(title="ev.io", value=" :wave:", color=0x109319)
        embed.add_field(name="Help",
                        value="└Use ?help\n*to get bot info*",
                        inline=False)
        embed.add_field(name="Rotation information",
                        value="└Use ?store\n*to get skin info*",
                        inline=False)
        embed.add_field(
            name="Change time name/title card of the message",
            value=
            """└Use ?store change (insert new string)\n*to change the name of the message""",
            inline=False)
        embed.add_field(
            name="Small image of skins",
            value=
            """└Use ?store small (insert skin name)\n*to get the thumbnail of the skin
                        NOTE- not availabe for weapon skins*""",
            inline=False)
        await message.channel.send(embed=embed)

    if j != page:
        await message.channel.send("?store")
    if (message.content.startswith("?store small")
            or message.content.startswith("?store small")) and len(
                message.content) >= 7:
        needed = message.content
        needed = needed[13:]
        print(needed)
        try:
            needed = needed.replace("wave", "shack")
        except:
            print("True")
        embed = discord.Embed(colour=discord.Color.from_rgb(225, 198, 153),
                              title="ev.io",
                              value=needed)
        k = needed
        head = k[0].lower() + k[1:] + "_head.png"
        if "<Response [404]>" == str(
                requests.get(
                    "https://ev.io/sites/default/files/skin_profile_thumbs/" +
                    head)):
            head = k[0].lower() + k[1:] + "_head%20%281%29.png"
        embed.set_image(
            url="https://ev.io/sites/default/files/skin_profile_thumbs/" +
            head)
        await message.channel.send(embed=embed)

    if (message.content.startswith("?store")
            or message.content.startswith("?store")) and len(
                message.content) <= 7:
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
            embed = discord.Embed(colour=discord.Color.from_rgb(225, 198, 153),
                                  title="ev.io",
                                  value=json_data[i]['title'])
            if json_data[i]['type'] == 'Player Skin':
                try:
                    url_i = "https://ev.io" + json_data[i]['field_large_thumb']
                    k = str(json_data[i]['title'])
                    head = k[0].lower() + k[1:] + "_head.png"
                    if "<Response [404]>" == str(
                            requests.get(
                                "https://ev.io/sites/default/files/skin_profile_thumbs/"
                                + head)):
                        head = k[0].lower() + k[1:] + "_head%20%281%29.png"
                    if "<Response [404]>" == str(
                            requests.get(
                                "https://ev.io/sites/default/files/skin_profile_thumbs/"
                                + head)):
                        head = k[0] + k[1:] + "_head%20%281%29.png"
                    if "<Response [404]>" == str(
                            requests.get(
                                "https://ev.io//sites/default/files/skin_profile_thumbs/"
                                + head)):
                        head = k[0].upper() + k[1:] + "_head%20%281%29.png"
                    if "<Response [404]>" == str(
                            requests.get(
                                "https://ev.io/sites/default/files/skin_profile_thumbs/"
                                + head)):
                        head = k[0] + k[1:] + "_head.png"
                    try:
                        head = head.replace("wave", "shack")
                    except:
                        print("True")

                    if "<Response [404]>" != str(
                            requests.get(
                                "https://ev.io/sites/default/files/skin_profile_thumbs/"
                                + head)):
                        embed.set_thumbnail(
                            url=
                            "https://ev.io/sites/default/files/skin_profile_thumbs/"
                            + head)
                    else:
                        embed.set_thumbnail(
                            url=
                            "https://ev.io//sites/default/files/skin_profile_thumbs/"
                            + head)
                except:
                    embed.set_thumbnail(url="")
            else:
                url_i = "https://ev.io" + json_data[i][
                    'field_weapon_skin_thumb']

            # embed.set_author(name=Temp,
            #                  url="https://ev.io/node/"+json_data[i]['nid'],
            #                  icon_url="https://ev.io/themes/ev/logo.png")
            embed.set_author(
                name=Temp,
                url="https://ev.io/node/" + json_data[i]['nid'],
                icon_url=
                "https://cdn.discordapp.com/icons/840042875805892649/edc19c9bde59d03a4b90f89c43e83e6f.png?size=128"
            )

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
            try:
                await message.channel.send(embed=embed)
            except:
                await message.channel.send(
                    "**Missed skin please visit store to find the missing one from the listing**"
                )
    msg_content = message.content.lower()

    # # delete curse word if match with the list
    for i in msg_content.split():
        if i in curseWord:
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
