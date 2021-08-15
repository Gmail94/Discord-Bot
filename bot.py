import discord
from discord.ext import commands




client = commands.Bot(command_prefix="!")

rules = [ " :one: Discord TOS and Guidelines: Make sure to follow Discord Terms of service and guidelines. Any violation will result in a ban. :link: https://discordapp.com/terms :link:https://discordapp.com/guidelines",

 ":two: No spamming or flooding the chat with messages.",

 ":three: Be respectful and courteous to all members, and avoid toxic behavior (slurs, racism, and homophobia).",

 ":four: Do not commit to/threaten harming others in any form whether this be physical harm, or harm through the use of cyber bullying, malware, or doxxing.",

 ":five: Do not leak any information. Any content/information shared within the sever is meant to benefit tenants and only the tenants.",

 ":six: If you need any help please create a ticket and ill be glad to help you"]

filtered_words = ["swear words"]



@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    for word in filtered_words:
        if word in message.content:
            await message.delete()

    await client.process_commands(message)


@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't do that ;-;")
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter all the required arguments")
            await ctx.message.delete()

@client.command(aliases=['rules','rul'])
async def rule(ctx,*,number):
    await ctx.send(rules[int(number)-1])

@client.command()
async def rental(ctx):
    await ctx.send ("`calculating the remaining days of your rental..please hold`")
@client.command()
async def hello(ctx):
    await ctx.send("Hey you handsome devil ;)")

@client.event
async def on_message(message):
    if message.content.startswith('Im the captain Now'):
        await message.channel.send("Not a Chance Mate!")

@client.command(aliases=['c'])
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member, * ,reason= "No reason provided"):
    try:
        await member.send ("You have been kicked from Chamillion's Wrath Rental, because: " +reason)
    except:
        await ctx.send ("The member has their dms closed.")

    await member.kick(reason= reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member, * ,reason= "No reason provided"):
    await member.send ("You have been banned from Chamillion's Wrath Rental, because: " +reason)
    await member.ban(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name, member_discriminator):

            await ctx.guild.unban(user)
            await ctx.send(member_name + " has been unbanned!")
            return

    await ctx.send(member + " was not found")

@client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(788248486444269588)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " has been muted")

@client.command(aliases=['um'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(788248486444269588)

    await member.remove_roles()

    await ctx.send(member.mention + " has been unmuted")

@client.command(aliases=['user','info'])
@commands.has_permissions(kick_members=True)
async def whois(ctx, member : discord.Member):
    embed = discord.Embed(title = member.name , description = member.mention, color = discord.Colour.dark_red())
    embed.add_field(name = "ID" , value = member.id , inline = True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url= ctx.author.avatar_url, text= f"Lurked by {ctx.author.name}")
    await ctx.send(embed=embed)

@client.event
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name = "Client")
    await ctx.add_roles(role)

@client.event
async def on_message(message):
    if message.content.startswith('drop'):
        embedVar = discord.Embed(title="__Shopify 4/26 Overview__", description="**Name** = `Nike Dunk Low Green` ", color=0x00ff00)
        embedVar.set_footer(text= 'Chamillion Guides')
        embedVar.add_field(name="Retail", value="`$55`", inline=False)
        embedVar.add_field(name="**Stock X**", value="https://stockx.com/yeezy-slide-core", inline= False)
        embedVar.add_field(name='Main Keywords', value=" `+yeezy,+slide,+core`", inline= False)
        embedVar.set_image(url='https://images.stockx.com/images/adidas-Yeezy-Slide-Pure.jpg?fit=fill&bg=FFFFFF&w=700&h=500&auto=format,compress&q=90&dpr=2&trim=color&updated_at=1618336644')
        await message.channel.send(embed=embedVar)




client.run
