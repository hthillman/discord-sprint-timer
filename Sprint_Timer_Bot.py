import discord
import time
import schedule
from discord.ext import commands
from threading import Event

TOKEN = 'TOKEN'

bot = commands.Bot(command_prefix='$', description='A bot that yells at us about how much time we have left in sprints.')
exit = Event()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def info():
    msg = "Hello! To start the sprint timer, please type '$start #'. To stop the sprint timer, please type $stop"
    await bot.say(msg)

@bot.command()
async def stop():
    timerOn = False
    exit.set()
    msg = 'Sprint timer off!'
    await bot.say(msg)



@bot.command()
async def start(days : int):
    global timerOn
    timerOn = True
    daysLeft = days
    hourCounter = 24
    msg = 'Sprint timer on!'
    await bot.say(msg)
    while timerOn and daysLeft >1 and not exit.is_set():
        msg = "Sprint time check! You have " + str(daysLeft) + " days left in the sprint!"
        await bot.say(msg)
        time.sleep(86400) #86400
        daysLeft -= 1
        if daysLeft == 1:
            break
    while timerOn and daysLeft > 0 and not exit.is_set():
        msg = "Sprint time check! You have " + str(hourCounter) + " hours left in the sprint!"
        await bot.say(msg)
        time.sleep(3600) #3600
        hourCounter -= 1
        if hourCounter == 0:
            daysLeft = 0
        if daysLeft == 0:
            break
    msg = "Sprint is over! Congratulations!"
    await bot.say(msg)
    timerOn = False

bot.run(TOKEN)
