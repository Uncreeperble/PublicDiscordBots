#This file was created for Chicken God.
# IF USED PLEASE REFERENCE ORIGINAL AUTHOR WITHOUT COMPENSATION!
import random
import discord			#Imports the discord module
from discord.ext import commands                                                        #we tell it we dont want all of discord just the commands part
from discord.ext.commands import has_permissions, MissingPermissions, when_mentioned_or # we tell it not all of the commands part just the things we need.
bot = commands.Bot(command_prefix=when_mentioned_or("$bock "))#this sets the prefix to %, or when mentioned.



possibilities = ["{} walked off a cliff trying to catch an eve on Pokémon go","{} ate a living rat and died","{} ate Bart Simpsons shorts down died"] #put in the death messages (note: the user killed is {}, to make it say the user who sent the command contact me.)
@bot.event #on a bot event, etc. reaction, restart, load etc.
async def on_ready():    #define the event in this case on_ready, the first thing ran when the bot starts
    print("Bot running with:")              # 
    print("Username: ", bot.user.name)         #        sends the bot name to the console as well as id in case you need it.
    print("User ID: ", bot.user.id)     #
    
@bot.event
async def on_message(message):

    if message.content == "$bock":
        print(f"{message.author} ran the bock command")
        await message.channel.send("Chickens are Epic and Legendary Gods.")
    else:
        await bot.process_commands(message)

@bot.command()
async def kill(ctx, user = None): #we are also taking in a user, by default it = None (empty)
    print(f"{ctx.author.name} ran the kill command", user)
    if user is not None:
        maxG = len(possibilities) - 1
        numberGot = random.randint(0, maxG)
        deathmessage = possibilities[numberGot]
        await ctx.send(deathmessage.format(user))
    else:
        await ctx.send("please provide a user.")




bot.run("BOT TOKEN WAS HERE") #login to the bot and continue detecting for the commands
