import discord, random, asyncio
from discord.ext import commands

client = commands.Bot(command_prefix=(">>>"), self_bot=True)

@client.event
async def on_ready():
    print(f'''We have logged in as {client.user}\nLogged in {len(client.guilds)} servers''')

@client.command()
async def dank(ctx):
    while True:
        randomlist = []
        for i in range(0,5):
                #   Random await speed
            n = random.randint(40,60)
            randomlist.append(n)
            print(f"Delay is on {n}")

                #   Discord stuff
            discordchannelid = discord.utils.get(ctx.guild.channels, id=ya channel id)
            await discordchannelid.send("pls hunt")
            await asyncio.sleep(5)
            await discordchannelid.send("pls fish")
            await asyncio.sleep(5)
            await discordchannelid.send("pls dig")

                #   Await 
            await asyncio.sleep(n)

client.run('ya token', bot = False)
