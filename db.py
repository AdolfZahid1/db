import discord,random,asyncio #,numge
from discord.ext import commands
from discord.ext.commands import CommandNotFound

bot = commands.Bot(command_prefix = '!',case_insensitive=True)
@bot.event
async def on_ready():
    print('Logged on')
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
"""
@bot.command(name='rob',brief='Counts robs(dont use)')
async def rob(ctx,*,arg):
    db = MySQLdb.connect(user="BOB",host="localhost",port=3306, passwd="1234", db="users")
    c = db.cursor()
    l = "<@" + str(ctx.author.id) + ">"
    c.execute("SELECT ID, COUNT(*) FROM users.f1 WHERE ID=%s GROUP BY ID", [l])
    row_count = c.rowcount
    if row_count > 0:
        c.execute("SELECT Crimes FROM users.f1 WHERE ID=%s", [l])
        j = c.fetchone()
        j = int(j[0]) + 1
        c.execute("UPDATE users.f1 SET Crimes=%s WHERE ID=%s", (j, [l]))
        db.commit()
    else:
        c.execute("Insert into users.f1(ID,Crimes) Values(%s,1)", [l])
        db.commit()
    c.close()
@bot.command(name='print',brief='Prints table out!')
async def print(ctx):
    db = MySQLdb.connect(user="BOB",host="localhost",port=3306, passwd="1234", db="users")
    c = db.cursor()
    c.execute("SELECT * FROM users.f1")
    result = c.fetchall()
    p=[]
    for row in result:
        p.append(row)
    await ctx.send(p)
    c.close()

@bot.command(name='clear',brief="Clears messages in channel(maximum 200 and not older than 2 weeks)")
@commands.has_permissions(manage_channels=True)
async def clr(ctx, number):
    await ctx.channel.purge(limit=int(number))
@bot.command(name='namegen',brief='')
async def namegen(ctx,arg:int):
    c=""
    if arg<=10 and arg>0:
        for i in range(arg):
            c+=numge.namegen()+"\n"
        await ctx.send(f"```{c}```")
    else:
        await ctx.send("Блять,пошел нахуй. Я не хочу больше падать!")

@namegen.error
async def namegen_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"```{numge.namegen()}```")
"""
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

bot.run('ODc5MDU5MTE2ODU1NzkxNjI3.YSKNmQ.3uVrIOXwresjs-vkEe52Adwwuos')