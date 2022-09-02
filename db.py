import nextcord,random,asyncio,json
from nextcord.ext import commands,tasks
from google_currency import convert
from nextcord.ext.commands import CommandNotFound

bot = commands.Bot(command_prefix = '!',case_insensitive=True)
@bot.event
async def on_ready():
    print('Logged on')
    changestatus.start()
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
@tasks.loop(seconds=5.0)
async def changestatus():
    c=json.loads(convert('eur', 'rub', 1))
    flan=float(c["amount"])
    flan+= random.randrange(50)
    await bot.change_presence(activity=nextcord.Game("flan-->credit: {0:.2f}".format(flan)))

@bot.command(name='roll',brief="Drops roll")
async def roll(ctx):
    for i in range(5):
        l = l+random.randrange(0, 21)
    await ctx.send(f"```{l}```")
@bot.command(name='coin',brief="Toss a coin")
async def coin(ctx):
    l=random.randrange(0,2)
    username = ctx.message.author.name
    await ctx.message.delete()
    await ctx.send(f"```{username} подкинул монетку!```")
    await asyncio.sleep(5)
    if l==1:
        await ctx.send("`Решка!`")
    else:
        await ctx.send("`Орёл!`")

bot.run('',reconnect=True)
