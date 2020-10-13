import discord
import logging
import asyncio
client=discord.Client()
#If you want to use my code as a base then go ahead but don't copy the exact code, change the values


@client.event
async def on_message(message):
    ...
    if message.content == "!botinfo":
        embed = discord.Embed(title="Pirate Naigator Info", description="Yaar! Know who I am!")
        embed.add_field(name="Developed on", value="August 2020")
        embed.add_field(name="Programming Language", value="Python")
        embed.add_field(name="Developed by", value="Watch_Doge")
        embed.add_field(name="Version", value="1.1.1")
        embed.add_field(name="Source Code", value="https://github.com/HeliumSpectrum/Pirate-Navigator-Source-Code")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!games-ac":
        embed = discord.Embed(title="Here are some games for ya, pirate", description="Remember to use a torrent client")       
        embed.add_field(name="Assassin's Creed Odyssey", value=" https://fitgirl-repacks.site/assassins-creed-odyssey/")
        embed.add_field(name="Assassin's Creed Origins", value=" https://fitgirl-repacks.site/assassins-creed-origins/")
        embed.add_field(name="Assassin's Creed Syndicate", value=" https://fitgirl-repacks.site/assassins-creed-syndicate-gold-edition/")
        embed.add_field(name="Assassin's Creed Rogue", value="https://fitgirl-repacks.site/assassins-creed-rogue/")
        embed.add_field(name="Assassin's Creed 3 Remastered", value="https://fitgirl-repacks.site/assassins-creed-3-remastered/")
        embed.add_field(name="Assassin's Creed 4 ", value="https://fitgirl-repacks.site/assassins-creed-iv-black-flag-jackdaw-edition/")
        embed.add_field(name="Assassin's Creed Unity", value="https://fitgirl-repacks.site/assassins-creed-unity-v1-5-0-dlcs/")
        embed.add_field(name="Assassin's Creed Chronicles", value="https://fitgirl-repacks.site/assassins-creed-chronicles-trilogy/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!games":
        embed = discord.Embed(title="Here are some commands for games collections", description="Use the commands for games")
        embed.add_field(name="Assassin's Creed Collection", value="!games-ac")
        embed.add_field(name="GTA collection", value="!games-gta")
        embed.add_field(name="Free to play Games", value="!games-free")
        embed.add_field(name="Far Cry Collection", value="!games-farcry")
        embed.add_field(name="Watch Dogs Collection", value="!games-watchdogs")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!games-gta":
        embed = discord.Embed(title="Here are some GTA Games for you", description="Remember to use a torrent client")
        embed.add_field(name="GTA 5", value="https://fitgirl-repacks.site/grand-theft-auto-v/")
        embed.add_field(name="GTA 4", value=" https://fitgirl-repacks.site/grand-theft-auto-iv-complete-edition/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!games-free":
        embed = discord.Embed(title="Here are some Free games to download", description="You dont need torrent for these")
        embed.add_field(name="PUBG PC Lite", value=" https://lite.pubg.com/download/")
        embed.add_field(name="Valorant", value="https://playvalorant.com/en-us/")
        embed.add_field(name="COD Warzone", value="https://www.callofduty.com/warzone/download")
        embed.add_field(name="Apex Legends", value="https://www.ea.com/games/apex-legends/play-now-for-free")
        embed.add_field(name="Fortnite", value="https://www.epicgames.com/fortnite/en-US/download?sessionInvalidated=true")
        embed.add_field(name="Rocket League", value="https://www.epicgames.com/store/en-US/product/rocket-league/home")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!games-farcry":
        embed = discord.Embed(title="Here are some Far Cry Games", description="Remember to use a torrent client")
        embed.add_field(name="Far Cry Primal", value=" https://fitgirl-repacks.site/far-cry-primal-apex-edition-v1-3-3-dlcs-ultra-hd-textures/")
        embed.add_field(name="Far Cry 5", value=" https://fitgirl-repacks.site/far-cry-5/")
        embed.add_field(name="Far Cry 3+Blood Dragon", value=" https://fitgirl-repacks.site/far-cry-3-duology/")
        embed.add_field(name="Far Cry New Dawn", value=" https://fitgirl-repacks.site/far-cry-new-dawn/")
        embed.add_field(name="Far Cry 4", value=" https://fitgirl-repacks.site/far-cry-4-gold-edition/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!games-watchdogs":
        embed = discord.Embed(title="Here are some Watch dogs Games", description="remember to use a torrent client")
        embed.add_field(name="Watch_dogs1", value=" https://fitgirl-repacks.site/watch-dogs-v1-06-329-all-dlcs/")
        embed.add_field(name="Watch_Dogs2", value=" https://fitgirl-repacks.site/watch-dogs-2-gold-edition/")
        await message.channel.send(content=None, embed=embed)
    ...
client.run('token')