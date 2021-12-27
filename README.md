# ev.io-cosmetics-bot
- This bot lists skin roation of a halo based online first person shooter browser game ev.io .
- The bot uses a endpoint provided by the developer[Forgeable]. The bots functionality was enxtended after the public release.
- Uses discord api to estabilish connection to the bot, invite the bot to your discord server. [Invite bot](https://discord.com/api/oauth2/authorize?client_id=892386694987395073&permissions=2048&scope=bot)
- This bot was created in a short span of time with limited resources.(About 36 hours) 
- Was paid 40 dollar ingame credit for creating the bot
#### Few fun facts
- My first working discord bot
- Completed the bot within 3 days
- Was blocked by Discord for testing the bot too quick 
- Currently hosted in a replit free tire replit
- Working on chat profainity filters 
#### Updates
- Can now scrap for imbd data using imdbpy wrapper and display a gist of the movie.
- Dynamically show time (24H format) updates every minute for various timezone and discord api to edit the message, this can be pinned in a server and it will never stop till the owner stops the code. Manually tweaked so as to avoid discord api access ban. So, it is safe to use.
- Scraps ev.io/clans and dynamically displays the clan points against clan name overlayed upon an image used pillow python, refreshed every 10 minutes to avoid caching of data.

#### Updates on Standby
- Write text over custom image link
- A motivation rooster invoked a command
- Cross-hair scrapper from a player's username
- Abilities identifier from a player's username


#### Libraries Used
- flask
- threading
- discord
- os
- requests
- json
- asyncio
- random
- pprint
- discord.ext
- better_profanity 
- replit 
- imdb
- bs4 
- requests_html 
- pytz
- pandas

