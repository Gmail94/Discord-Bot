<html>
<head>
<title>bot.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6a8759;}
.s3 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
bot.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">discord</span>
<span class="s0">from </span><span class="s1">discord.ext </span><span class="s0">import </span><span class="s1">commands</span>




<span class="s1">client = commands.Bot(command_prefix=</span><span class="s2">&quot;!&quot;</span><span class="s1">)</span>

<span class="s1">rules = [ </span><span class="s2">&quot; :one: Discord TOS and Guidelines: Make sure to follow Discord Terms of service and guidelines. Any violation will result in a ban. :link: https://discordapp.com/terms :link:https://discordapp.com/guidelines&quot;</span><span class="s0">,</span>

 <span class="s2">&quot;:two: No spamming or flooding the chat with messages.&quot;</span><span class="s0">,</span>

 <span class="s2">&quot;:three: Be respectful and courteous to all members, and avoid toxic behavior (slurs, racism, and homophobia).&quot;</span><span class="s0">,</span>

 <span class="s2">&quot;:four: Do not commit to/threaten harming others in any form whether this be physical harm, or harm through the use of cyber bullying, malware, or doxxing.&quot;</span><span class="s0">,</span>

 <span class="s2">&quot;:five: Do not leak any information. Any content/information shared within the sever is meant to benefit tenants and only the tenants.&quot;</span><span class="s0">,</span>

 <span class="s2">&quot;:six: If you need any help please create a ticket and ill be glad to help you&quot;</span><span class="s1">]</span>

<span class="s1">filtered_words = [</span><span class="s2">&quot;swear words&quot;</span><span class="s1">]</span>



<span class="s1">@client.event</span>
<span class="s0">async def </span><span class="s1">on_ready():</span>
    <span class="s1">print(</span><span class="s2">&quot;Bot is ready&quot;</span><span class="s1">)</span>

<span class="s1">@client.event</span>
<span class="s0">async def </span><span class="s1">on_message(message):</span>
    <span class="s0">for </span><span class="s1">word </span><span class="s0">in </span><span class="s1">filtered_words:</span>
        <span class="s0">if </span><span class="s1">word </span><span class="s0">in </span><span class="s1">message.content:</span>
            <span class="s0">await </span><span class="s1">message.delete()</span>

    <span class="s0">await </span><span class="s1">client.process_commands(message)</span>


<span class="s1">@client.event</span>
<span class="s0">async def </span><span class="s1">on_command_error(ctx</span><span class="s0">,</span><span class="s1">error):</span>
    <span class="s0">if </span><span class="s1">isinstance(error</span><span class="s0">, </span><span class="s1">commands.MissingPermissions):</span>
        <span class="s0">await </span><span class="s1">ctx.send(</span><span class="s2">&quot;You can't do that ;-;&quot;</span><span class="s1">)</span>
        <span class="s0">await </span><span class="s1">ctx.message.delete()</span>
    <span class="s0">elif </span><span class="s1">isinstance(error</span><span class="s0">, </span><span class="s1">commands.MissingRequiredArgument):</span>
            <span class="s0">await </span><span class="s1">ctx.send(</span><span class="s2">&quot;Please enter all the required arguments&quot;</span><span class="s1">)</span>
            <span class="s0">await </span><span class="s1">ctx.message.delete()</span>

<span class="s1">@client.command(aliases=[</span><span class="s2">'rules'</span><span class="s0">,</span><span class="s2">'rul'</span><span class="s1">])</span>
<span class="s0">async def </span><span class="s1">rule(ctx</span><span class="s0">,</span><span class="s1">*</span><span class="s0">,</span><span class="s1">number):</span>
    <span class="s0">await </span><span class="s1">ctx.send(rules[int(number)-</span><span class="s3">1</span><span class="s1">])</span>

<span class="s1">@client.command()</span>
<span class="s0">async def </span><span class="s1">rental(ctx):</span>
    <span class="s0">await </span><span class="s1">ctx.send (</span><span class="s2">&quot;`calculating the remaining days of your rental..please hold`&quot;</span><span class="s1">)</span>
<span class="s1">@client.command()</span>
<span class="s0">async def </span><span class="s1">hello(ctx):</span>
    <span class="s0">await </span><span class="s1">ctx.send(</span><span class="s2">&quot;Hey you handsome devil ;)&quot;</span><span class="s1">)</span>

<span class="s1">@client.event</span>
<span class="s0">async def </span><span class="s1">on_message(message):</span>
    <span class="s0">if </span><span class="s1">message.content.startswith(</span><span class="s2">'Im the captain Now'</span><span class="s1">):</span>
        <span class="s0">await </span><span class="s1">message.channel.send(</span><span class="s2">&quot;Not a Chance Mate!&quot;</span><span class="s1">)</span>

<span class="s1">@client.command(aliases=[</span><span class="s2">'c'</span><span class="s1">])</span>
<span class="s0">async def </span><span class="s1">clear(ctx</span><span class="s0">, </span><span class="s1">amount=</span><span class="s3">2</span><span class="s1">):</span>
    <span class="s0">await </span><span class="s1">ctx.channel.purge(limit=amount)</span>

<span class="s1">@client.command(aliases=[</span><span class="s2">'k'</span><span class="s1">])</span>
<span class="s1">@commands.has_permissions(kick_members = </span><span class="s0">True</span><span class="s1">)</span>
<span class="s0">async def </span><span class="s1">kick(ctx</span><span class="s0">,</span><span class="s1">member : discord.Member</span><span class="s0">, </span><span class="s1">* </span><span class="s0">,</span><span class="s1">reason= </span><span class="s2">&quot;No reason provided&quot;</span><span class="s1">):</span>
    <span class="s0">try</span><span class="s1">:</span>
        <span class="s0">await </span><span class="s1">member.send (</span><span class="s2">&quot;You have been kicked from Chamillion's Wrath Rental, because: &quot; </span><span class="s1">+reason)</span>
    <span class="s0">except</span><span class="s1">:</span>
        <span class="s0">await </span><span class="s1">ctx.send (</span><span class="s2">&quot;The member has their dms closed.&quot;</span><span class="s1">)</span>

    <span class="s0">await </span><span class="s1">member.kick(reason= reason)</span>

<span class="s1">@client.command(aliases=[</span><span class="s2">'b'</span><span class="s1">])</span>
<span class="s1">@commands.has_permissions(ban_members = </span><span class="s0">True</span><span class="s1">)</span>
<span class="s0">async def </span><span class="s1">ban(ctx</span><span class="s0">,</span><span class="s1">member : discord.Member</span><span class="s0">, </span><span class="s1">* </span><span class="s0">,</span><span class="s1">reason= </span><span class="s2">&quot;No reason provided&quot;</span><span class="s1">):</span>
    <span class="s0">await </span><span class="s1">member.send (</span><span class="s2">&quot;You have been banned from Chamillion's Wrath Rental, because: &quot; </span><span class="s1">+reason)</span>
    <span class="s0">await </span><span class="s1">member.ban(reason=reason)</span>

<span class="s1">@client.command()</span>
<span class="s1">@commands.has_permissions(ban_members=</span><span class="s0">True</span><span class="s1">)</span>
<span class="s0">async def </span><span class="s1">unban(ctx</span><span class="s0">,</span><span class="s1">*</span><span class="s0">,</span><span class="s1">member):</span>
    <span class="s1">banned_users = </span><span class="s0">await </span><span class="s1">ctx.guild.bans()</span>
    <span class="s1">member_name</span><span class="s0">, </span><span class="s1">member_discriminator = member.split(</span><span class="s2">'#'</span><span class="s1">)</span>

    <span class="s0">for </span><span class="s1">banned_entry </span><span class="s0">in </span><span class="s1">banned_users:</span>
        <span class="s1">user = banned_entry.user</span>

        <span class="s0">if</span><span class="s1">(user.name</span><span class="s0">, </span><span class="s1">user.discriminator)==(member_name</span><span class="s0">, </span><span class="s1">member_discriminator):</span>

            <span class="s0">await </span><span class="s1">ctx.guild.unban(user)</span>
            <span class="s0">await </span><span class="s1">ctx.send(member_name + </span><span class="s2">&quot; has been unbanned!&quot;</span><span class="s1">)</span>
            <span class="s0">return</span>

    <span class="s0">await </span><span class="s1">ctx.send(member + </span><span class="s2">&quot; was not found&quot;</span><span class="s1">)</span>

<span class="s1">@client.command(aliases=[</span><span class="s2">'m'</span><span class="s1">])</span>
<span class="s1">@commands.has_permissions(kick_members=</span><span class="s0">True</span><span class="s1">)</span>
<span class="s0">async def </span><span class="s1">mute(ctx</span><span class="s0">, </span><span class="s1">member : discord.Member):</span>
    <span class="s1">muted_role = ctx.guild.get_role(</span><span class="s3">788248486444269588</span><span class="s1">)</span>

    <span class="s0">await </span><span class="s1">member.add_roles(muted_role)</span>

    <span class="s0">await </span><span class="s1">ctx.send(member.mention + </span><span class="s2">&quot; has been muted&quot;</span><span class="s1">)</span>

<span class="s1">@client.command(aliases=[</span><span class="s2">'um'</span><span class="s1">])</span>
<span class="s1">@commands.has_permissions(kick_members=</span><span class="s0">True</span><span class="s1">)</span>
<span class="s0">async def </span><span class="s1">unmute(ctx</span><span class="s0">, </span><span class="s1">member : discord.Member):</span>
    <span class="s1">muted_role = ctx.guild.get_role(</span><span class="s3">788248486444269588</span><span class="s1">)</span>

    <span class="s0">await </span><span class="s1">member.remove_roles()</span>

    <span class="s0">await </span><span class="s1">ctx.send(member.mention + </span><span class="s2">&quot; has been unmuted&quot;</span><span class="s1">)</span>

<span class="s1">@client.command(aliases=[</span><span class="s2">'user'</span><span class="s0">,</span><span class="s2">'info'</span><span class="s1">])</span>
<span class="s1">@commands.has_permissions(kick_members=</span><span class="s0">True</span><span class="s1">)</span>
<span class="s0">async def </span><span class="s1">whois(ctx</span><span class="s0">, </span><span class="s1">member : discord.Member):</span>
    <span class="s1">embed = discord.Embed(title = member.name </span><span class="s0">, </span><span class="s1">description = member.mention</span><span class="s0">, </span><span class="s1">color = discord.Colour.dark_red())</span>
    <span class="s1">embed.add_field(name = </span><span class="s2">&quot;ID&quot; </span><span class="s0">, </span><span class="s1">value = member.id </span><span class="s0">, </span><span class="s1">inline = </span><span class="s0">True</span><span class="s1">)</span>
    <span class="s1">embed.set_thumbnail(url = member.avatar_url)</span>
    <span class="s1">embed.set_footer(icon_url= ctx.author.avatar_url</span><span class="s0">, </span><span class="s1">text= </span><span class="s2">f&quot;Lurked by </span><span class="s0">{</span><span class="s1">ctx.author.name</span><span class="s0">}</span><span class="s2">&quot;</span><span class="s1">)</span>
    <span class="s0">await </span><span class="s1">ctx.send(embed=embed)</span>


<span class="s1">@client.event</span>
<span class="s0">async def </span><span class="s1">on_member_join(ctx):</span>
    <span class="s1">role = discord.utils.get(ctx.guild.roles</span><span class="s0">, </span><span class="s1">name = </span><span class="s2">&quot;Client&quot;</span><span class="s1">)</span>
    <span class="s0">await </span><span class="s1">ctx.add_roles(role)</span>

<span class="s1">@client.event</span>
<span class="s0">async def </span><span class="s1">on_message(message):</span>
    <span class="s0">if </span><span class="s1">message.content.startswith(</span><span class="s2">'drop'</span><span class="s1">):</span>
        <span class="s1">embedVar = discord.Embed(title=</span><span class="s2">&quot;__Shopify 4/26 Overview__&quot;</span><span class="s0">, </span><span class="s1">description=</span><span class="s2">&quot;**Name** = `Nike Dunk Low Green` &quot;</span><span class="s0">, </span><span class="s1">color=</span><span class="s3">0x00ff00</span><span class="s1">)</span>
        <span class="s1">embedVar.set_footer(text= </span><span class="s2">'Chamillion Guides'</span><span class="s1">)</span>
        <span class="s1">embedVar.add_field(name=</span><span class="s2">&quot;Retail&quot;</span><span class="s0">, </span><span class="s1">value=</span><span class="s2">&quot;`$55`&quot;</span><span class="s0">, </span><span class="s1">inline=</span><span class="s0">False</span><span class="s1">)</span>
        <span class="s1">embedVar.add_field(name=</span><span class="s2">&quot;**Stock X**&quot;</span><span class="s0">, </span><span class="s1">value=</span><span class="s2">&quot;https://stockx.com/yeezy-slide-core&quot;</span><span class="s0">, </span><span class="s1">inline= </span><span class="s0">False</span><span class="s1">)</span>
        <span class="s1">embedVar.add_field(name=</span><span class="s2">'Main Keywords'</span><span class="s0">, </span><span class="s1">value=</span><span class="s2">&quot; `+yeezy,+slide,+core`&quot;</span><span class="s0">, </span><span class="s1">inline= </span><span class="s0">False</span><span class="s1">)</span>
        <span class="s1">embedVar.set_image(url=</span><span class="s2">'https://images.stockx.com/images/adidas-Yeezy-Slide-Pure.jpg?fit=fill&amp;bg=FFFFFF&amp;w=700&amp;h=500&amp;auto=format,compress&amp;q=90&amp;dpr=2&amp;trim=color&amp;updated_at=1618336644'</span><span class="s1">)</span>
        <span class="s0">await </span><span class="s1">message.channel.send(embed=embedVar)</span>




<span class="s1">client.run(</span><span class="s2">&quot;ODE2MzcyNzYzNDQyOTM3ODg2.YD6AYg.tttzBkpEGfAaNciyVXmPw9gTn0M&quot;</span><span class="s1">)</span>
</pre>
</body>
</html>