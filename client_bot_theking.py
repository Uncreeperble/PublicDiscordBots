import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, when_mentioned_or
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
bot = commands.Bot(command_prefix=when_mentioned_or("%"))
bot.remove_command("help")




rulesL = ["No racism of any kind.", "No racism of any kind.",
 "No jokes about mental or physical disabilities.",
 "No posting  explicit content. Doing so will result in a ban.","Post content and text in the appropriate channels -- Descriptions posted below.",
 "English only. If you wish to chat in your native, or any other language, do so in DMs.",
 "Do not insult or personally attack others. Use common sense while chatting.",
 "No mention of self harm and drugs",
 "No racist, explicit, disrespectful, or offensive nicknames, profile pictures, or custom statuses.",
 "No begging, asking, or posting links .",
 "No micro-modding whether you are new or a regular. Let the Moderators and Server Moderators handle all situations as they see fit.",
 "No misusing the bots in the server",
 "Do not self-promote your Twitch, YouTube, Discord, Mixer, or ANY Social media channels. This includes your custom status on Discord.",
 "No symbols in your name that puts you at the top of the viewer list, for example ---> ( ! - ` . ), or any numbers. Also no excessive amount of symbols in your username.",
 "Listen to the Moderators and Server Moderators at all times -- If you have questions/issues or open a Ticket. ~ ~",
 "You have to reach Level 30 on @Amaribot and you will get a private channel ",
 "Just for the private channel it doesn't meant to spam to level up. Don't try that it wont work.",
 "Please use the commands the in specified channel which is clearly mentioned in the channel names. not doing so will result in a warn",
 "If a person has more than 10 warns  they will get a soft ban and 20 warns is a permanent ban",
 "We enforce Discords ToS and CG. Breaking any of these rules will result in a permanent ban from this server",
 "If you are found breaking these rules even in the voice channels you will be warned and may risk a ban",
 "If you server boost you will get a exclusive server booster role and also will get a private channel.",
 "If you are found sniping a god event which is rare and you didn’t trigger it you will get soft banned.",
 "If you are found sniping a god event two or more times, then you will be permanent banned. "]
@bot.event
async def on_ready():
    print("Bot running with:")
    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)



def page1():
        
    embed=discord.Embed(title=f"Server Rules. Page 1/4", description=f"The Following are a list of the server rules.", color=0x0085fa)
    embed.add_field(name=f"Rule #1", value=f"{rulesL[0]}", inline=False) 
    embed.add_field(name=f"Rule #2", value=f"{rulesL[1]}", inline=False) 
    embed.add_field(name=f"Rule #3", value=f"{rulesL[2]}", inline=False) 
    embed.add_field(name=f"Rule #4", value=f"{rulesL[3]}", inline=False)
    embed.add_field(name=f"Rule #5", value=f"{rulesL[4]}", inline=False) 
    embed.add_field(name=f"Rule #6", value=f"{rulesL[5]}", inline=False) 
    return(embed)
def page2():
        
    embed=discord.Embed(title=f"Server Rules. Page 2/4", description=f"The Following are a list of the server rules.", color=0x0085fa)
    embed.add_field(name=f"Rule #7", value=f"{rulesL[6]}", inline=False) 
    embed.add_field(name=f"Rule #8", value=f"{rulesL[7]}", inline=False) 
    embed.add_field(name=f"Rule #9", value=f"{rulesL[8]}", inline=False) 
    embed.add_field(name=f"Rule #10", value=f"{rulesL[9]}", inline=False)
    embed.add_field(name=f"Rule #11", value=f"{rulesL[10]}", inline=False) 
    embed.add_field(name=f"Rule #12", value=f"{rulesL[11]}", inline=False)
    return(embed)
def page3():
        
    embed=discord.Embed(title=f"Server Rules. Page 3/4", description=f"The Following are a list of the server rules.", color=0x0085fa)
    embed.add_field(name=f"Rule #13", value=f"{rulesL[12]}", inline=False) 
    embed.add_field(name=f"Rule #14", value=f"{rulesL[13]}", inline=False) 
    embed.add_field(name=f"Rule #15", value=f"{rulesL[14]}", inline=False) 
    embed.add_field(name=f"Rule #16", value=f"{rulesL[15]}", inline=False)
    embed.add_field(name=f"Rule #17", value=f"{rulesL[16]}", inline=False) 
    embed.add_field(name=f"Rule #18", value=f"{rulesL[17]}", inline=False)
    return(embed)
def page4():
        
    embed=discord.Embed(title=f"Server Rules. Page 4/4", description=f"The Following are a list of the server rules.", color=0x0085fa)
    embed.add_field(name=f"Rule #19", value=f"{rulesL[18]}", inline=False) 
    embed.add_field(name=f"Rule #20", value=f"{rulesL[19]}", inline=False) 
    embed.add_field(name=f"Rule #21", value=f"{rulesL[20]}", inline=False) 
    embed.add_field(name=f"Rule #22", value=f"{rulesL[21]}", inline=False)
    embed.add_field(name=f"Rule #23", value=f"{rulesL[22]}", inline=False) 
    embed.add_field(name=f"Rule #24", value=f"{rulesL[23]}", inline=False) 
    return(embed)
@bot.command()
async def rule(ctx, rule = None):
    try:
        
        if rule is not None:
            try:

                ruleID = int(rule)
                if ruleID <= 0:
                    embed=discord.Embed(title="Incorrect Rule ID", description="Please check the ID and try again.", color=0xff0000)
                    await ctx.send(embed=embed)
                else:    
                    embed=discord.Embed(title=f"Rule #{ruleID}", description=f"{rulesL[ruleID-1]}", color=0x0085fa)
                    await ctx.send(embed=embed)
            except:
                embed=discord.Embed(title="Incorrect Rule ID", description="Please check the ID and try again.", color=0xff0000)
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Please Provide the Rule ID", description="To view a specific rule, please provide it's ID.", color=0xff0000)
            await ctx.send(embed=embed)
    except:
        await ctx.send("The bot needs permission to `Send Embedded Content`.")
@bot.command()
async def rules(ctx):

    pages = 4
    cur_page = 1
    contents = [page1(), page2(), page3(), page4()]

    message = await ctx.send(embed = contents[cur_page-1])
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"


    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                print(contents[cur_page-1])
                await message.edit(embed=contents[cur_page-1])
                await message.remove_reaction(reaction, user)
                

                

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(embed=contents[cur_page-1])
                await message.remove_reaction(reaction, user)

                

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except:
            await message.delete()
            break
bot.run("Nzk5MTQyMjYwNjI0NzE5OTAy.X__ROg.H7MveMs3uT8xLTyC7GtYBebuM0s") 