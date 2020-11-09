import discord
import logging
import asyncio
client=discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!games to pirate"))
    print("Bot is ready!")

#This is the unfinished version of the bot thative been working on before suspending the updates

@client.event
async def on_message(message):
    ...
    if message.content == "!botinfo":
        embed = discord.Embed(title="Pirate Navigator Info", description="Yaar! Know who I am!")
        embed.add_field(name="Developed on", value="August 2020")
        embed.add_field(name="Programming Language", value="Python")
        embed.add_field(name="Developed by", value="@Doom_Doge#3738 and @shastha#1835")
        embed.add_field(name="Version", value="1.7")
        embed.add_field(name="Source Code", value="https://github.com/HeliumSpectrum/Pirate-Navigator-Source-Code")
        embed.add_field(name="Bot Invite Link", value="https://discord.com/oauth2/authorize?client_id=749139984321347674&scope=bot")
        embed.add_field(name="Visit Support Server", value="https://discord.gg/ZVNdzff")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!games":
        embed = discord.Embed(title="Here are some games collections", description="Pick your choice!")
        embed.add_field(name="Repacks", value="!repacks")
        embed.add_field(name="Direct Download Links", value="!ddl")
        embed.add_field(name="Important Software", value="!soft")
        embed.add_field(name="Pirate Handbook", value="!handbook")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-ac":
        embed = discord.Embed(title="Here are some repacks for ya, pirate", description="Remember to use a torrent client")       
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
    if message.content == "!fitgirl":
        embed = discord.Embed(title="Here are some commands for repacks collections", description="Use the commands for repacks")
        embed.add_field(name="Assassin's Creed FitgirlRepacks Collection", value="!fitgirl-ac")
        embed.add_field(name="GTA Fitgirl Repacks collection", value="!fitgirl-gta")
        embed.add_field(name="Far Cry Fitgirl Repack Collection", value="!fitgirl-farcry")
        embed.add_field(name="Watch Dogs Fitgirl Repack Collection", value="!fitgirl-watchdogs")
        embed.add_field(name="Need For Speed Fitgirl Repack Collection", value='!fitgirl-nfs')
        embed.add_field(name="Tom Clancy Fitgirl Repack Collection", value="!fitgirl-splintercell")
        embed.add_field(name="Mass Effect Fitgirl Repack Collection", value="!fitgirl-masseffect")
        embed.add_field(name="Star Wars Fitgirl Repack Collection", value="!fitgirl-starwars")
        embed.add_field(name="Lego Games Fitgirl Repack Collection", value="!fitgirl-lego")
        embed.add_field(name="Marvel Fitgirl Repack Collection", value="!fitgirl-marvel")
        embed.add_field(name="Ghost Recon Fitgirl Repack Collection", value="!fitgirl-ghostrecon")
        embed.add_field(name="Mafia Fitgirl Repack Collection", value="!fitgirl-mafia")
        embed.add_field(name="Doom Fitgirl Repack Collection", value="!fitgirl-doom")
        embed.add_field(name="Spiderman Fitgirl Repack Collection", value="!fitgirl-spiderman")
        embed.add_field(name="Fallout Fitgirl Repack Collection", value="!fitgirl-fallout")
        embed.add_field(name="Mortal Kombat Fitgirl Repack Collection", value="!fitgirl-mortalkombat")
        embed.add_field(name="Witcher Fitgirl Repack Collection", value="!fitgirl-witcher")
        embed.add_field(name="RDR2 Fitgirl Repack Collection",value="!fitgirl-rdr2")
        embed.add_field(name="Dark Souls Fitgirl Repack Collection", value="!fitgirl-darksouls")
        embed.add_field(name="DiRT Fitgirl Repack Collection", value="!fitgirl-dirt")
        embed.add_field(name="Dishonoured Fitgirl Repack Collection", value="!fitgirl-dishonoured")
        embed.add_field(name="Devil May Cry Fitgirl Repack Collection", value="!fitgirl-dmc")
        embed.add_field(name="Deus EX Fitgirl Repack Collection", value="!fitgirl")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-gta":
        embed = discord.Embed(title="Here are some GTA Repacks for you", description="Remember to use a torrent client")
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
    if message.content == "!fitgirl-farcry":
        embed = discord.Embed(title="Here are some Far Cry Games Repacks", description="Remember to use a torrent client")
        embed.add_field(name="Far Cry Primal", value=" https://fitgirl-repacks.site/far-cry-primal-apex-edition-v1-3-3-dlcs-ultra-hd-textures/")
        embed.add_field(name="Far Cry 5", value=" https://fitgirl-repacks.site/far-cry-5/")
        embed.add_field(name="Far Cry 3+Blood Dragon", value=" https://fitgirl-repacks.site/far-cry-3-duology/")
        embed.add_field(name="Far Cry New Dawn", value=" https://fitgirl-repacks.site/far-cry-new-dawn/")
        embed.add_field(name="Far Cry 4", value=" https://fitgirl-repacks.site/far-cry-4-gold-edition/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-watchdogs":
        embed = discord.Embed(title="Here are some Watch dogs Games Repacks", description="remember to use a torrent client")
        embed.add_field(name="Watch_dogs1", value=" https://fitgirl-repacks.site/watch-dogs-v1-06-329-all-dlcs/")
        embed.add_field(name="Watch_Dogs2", value=" https://fitgirl-repacks.site/watch-dogs-2-gold-edition/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-nfs":
        embed = discord.Embed(title="Here are some need for speed games repacks", description="Remember to use a torrent client")
        embed.add_field(name="Need For Speed Payback", value="https://fitgirl-repacks.site/need-for-speed-payback-deluxe-edition/")
        embed.add_field(name="Need For Speed Hot Pursuit", value="https://fitgirl-repacks.site/need-speed-hot-pursuit-v1-0-5-0s-dlcs/")
        embed.add_field(name="Need For Speed Most Wanted 2012", value="https://fitgirl-repacks.site/need-speed-wanted-limited-edition-v-1-5-0-0-dlcs/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-splintercell":
        embed = discord.Embed(title="Here are some Splinter Cell games repacks", description="Remember to use torrent client")
        embed.add_field(name="Tom Clancy's Splinter Cell Blacklist", value="https://fitgirl-repacks.site/tom-clancys-splinter-cell-blacklist-digital-deluxe-edition-v1-03-2-dlcs/")   
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!masquerade-amongus":
        embed = discord.Embed(title="Download link for Among US", description="You need a new gmail account for this")
        embed.add_field(name="Among US(Masquerade)", value="https://masquerade.site/among-us/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-masseffect":
        embed = discord.Embed(title="Here's the Mass Effect Collection repacks", description="Use a torrent client to download")
        embed.add_field(name="Mass Effect 1", value="https://fitgirl-repacks.site/mass-effect/")
        embed.add_field(name="Mass Effect 2", value="https://fitgirl-repacks.site/mass-effect-2/")
        embed.add_field(name="Mass Effect 3", value="https://fitgirl-repacks.site/mass-effect-3/")
        embed.add_field(name="Mass Effect: Andromeda", value="https://fitgirl-repacks.site/mass-effect-andromeda-super-deluxe-edition/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-starwars":
        embed = discord.Embed(title="Here's the Star Wars Collection repacks", description="Use a torrent client to download")
        embed.add_field(name="Star Wars: Jedi Fallen Order", value="https://fitgirl-repacks.site/star-wars-jedi-fallen-order/")
        embed.add_field(name="Star Wars: Battlefront 2", value="https://fitgirl-repacks.site/star-wars-battlefront-ii/")
        embed.add_field(name="Lego Star Wars: Force Awakens", value="https://fitgirl-repacks.site/lego-star-wars-force-awakens-v1-03-build-1-0-0-33084-12-dlcs/")
        await message.channel.send(content=None, embed=embed)
    ...
    
    ...
    if message.content == "!fitgirl-lego":
        embed = discord.Embed(title="Here's the Lego games collection", description="Use a torrent client to download and make sure you have uBlock Origin")
        embed.add_field(name="Lego DC Super Villains", value="https://fitgirl-repacks.site/lego-dc-super-villains/")
        embed.add_field(name="Lego Movie 2 Videogame", value="https://fitgirl-repacks.site/the-lego-movie-2-videogame/")
        embed.add_field(name="Lego: The Incredibles", value="https://fitgirl-repacks.site/lego-the-incredibles/")
        embed.add_field(name="Lego Marvel Super Heroes", value="https://fitgirl-repacks.site/lego-marvel-super-heroes-2/")
        embed.add_field(name="Lego Ninjago", value="https://fitgirl-repacks.site/the-lego-ninjago-movie-video-game/")
        embed.add_field(name="Lego City Undercover", value="https://fitgirl-repacks.site/lego-city-undercover-update-1/")
        embed.add_field(name="Lego Worlds", value="https://fitgirl-repacks.site/lego-worlds/")
        embed.add_field(name="Lego Avengers", value="https://fitgirl-repacks.site/lego-marvels-avengers-v1-0-0-28133-11-dlc/")
        embed.add_field(name="Lego Jurassic World", value="https://fitgirl-repacks.site/lego-jurassic-world-update-1-all-dlcs/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-marvel":
        embed = discord.Embed(title="Here's the Marvel Collection", description="Use a torrent client to download")
        embed.add_field(name="Marvel vs Capcom: Infinite", value="https://fitgirl-repacks.site/marvel-vs-capcom-infinite/")
        embed.add_field(name="Marvel's Guardians Of The Galaxy: Telltale Edition", value="https://fitgirl-repacks.site/marvels-guardians-of-the-galaxy-the-telltale-series-complete-season/")
        embed.add_field(name="Ultimate Marvel Vs Capcom 3", value="https://fitgirl-repacks.site/ultimate-marvel-vs-capcom-3/")
        embed.add_field(name="Marvel's Ultimate Alliance", value="https://fitgirl-repacks.site/marvel-ultimate-alliance-bundle-1-2/")
        await message.channel.send(content=None, embed=embed)
    ...
    
    ...
    if message.content == "!fitgirl-ghostrecon":
        embed = discord.Embed(title="Here's the Ghost Recon Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Tom Clancy's Ghost Recon Wildlands", value="https://fitgirl-repacks.site/tom-clancys-ghost-recon-wildlands/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-mafia":
        embed = discord.Embed(title="Here are some Mafia Repacks Collection", description="Remember to use a torrent client")
        embed.add_field(name="Mafia: Definitive Edition", value="https://fitgirl-repacks.site/mafia-definitive-edition-v1-0-1-chicago-outfit-pack-dlc-windows-7-fix/")
        embed.add_field(name="Mafia 2", value="https://fitgirl-repacks.site/mafia-2-digital-deluxe-edition-v-1-0-0-1/")
        embed.add_field(name="Mafia 3", value="https://fitgirl-repacks.site/mafia-3-digital-deluxe-edition/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-doom":
        embed = discord.Embed(title="Here's the Doom Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Doom 3: BFG Edition", value="https://dodi-repacks.site/index.php/2020/06/30/667-doom-3-bfg-edition-v20191007-dlcs-multi6-dodi-repack/")
        embed.add_field(name="Doom 64 ", value="https://fitgirl-repacks.site/doom-64/")
        embed.add_field(name="Doom 1&2", value="https://fitgirl-repacks.site/doom-doom-2-classic-bundle/")
        embed.add_field(name="Doom 2016", value="https://fitgirl-repacks.site/doom/")
        embed.add_field(name="Doom Eternal", value="https://fitgirl-repacks.site/doom-eternal/")
        await message.channel.send(content=None, embed=embed)
    ...
    
    ...
    if message.content == "!fitgirl-spiderman":
        embed = discord.Embed(title="Here's the Spiderman Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Spiderman: Shattered Dimensions", value="https://fitgirl-repacks.site/spider-man-shattered-dimensions/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!dodi-battlefield":
        embed = discord.Embed(title="Here's the Battlefield Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Battlefield 1", value="https://dodi-repacks.site/index.php/2019/02/06/271-battlefield-1-digital-deluxe-edition-update-3-all-dlcs-multi12-dodi-repack-from-18-6-gb/")
        embed.add_field(name="Battlefield 3", value="https://dodi-repacks.site/index.php/2019/05/28/363-battlefield-3-v1-4-0-multi10-dodi-repack-from-7-8-gb/  ")
        embed.add_field(name="Battlefield V", value="https://dodi-repacks.site/index.php/2018/12/13/214-battlefield-v-deluxe-edition-dodi-repack/")
        embed.add_field(name="Battlefield 4", value="https://dodi-repacks.site/index.php/2019/06/08/378-battlefield-4-update-12-v1-2-0-1-multi12-dodi-repack-from-17-6-gb/")
        embed.add_field(name="Battlefield Hardline", value="https://dodi-repacks.site/index.php/2019/06/15/383-battlefield-hardline-digital-deluxe-edition-1-07-15-00-crackfix-multi12-dodi-repack-from-26-7-gb/")
        embed.add_field(name="Battlefield Bad Company 2", value="https://dodi-repacks.site/index.php/2019/07/13/408-battlefield-bad-company-2-ultimate-digital-edition-v1-0-build-795745-dlc-multi9-dodi-repack-from-3-2-gb/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!dodi-cod":
        embed = discord.Embed(title="Here's the Call Of Duty Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Call Of Duty 1 + United Offensive", value="https://dodi-repacks.site/index.php/2020/08/02/716-call-of-duty-deluxe-edition-united-offensive-dodi-repack/")
        embed.add_field(name="Call Of Duty 2 ", value="https://dodi-repacks.site/index.php/2020/08/02/717-call-of-duty-2-dodi-repack/")
        embed.add_field(name="Call Of Duty Advanced Warfare", value="https://dodi-repacks.site/index.php/2019/06/04/372-call-of-duty-advanced-warfare-complete-pack-dodi-repack/")
        embed.add_field(name="Call Of Duty Ghosts", value="https://dodi-repacks.site/index.php/2018/12/21/222-call-of-duty-ghosts-deluxe-edition-update-21-build-749678-dodi-repack/")
        embed.add_field(name="Call Of Duty Infinite Warfare", value="https://dodi-repacks.site/index.php/2019/02/18/278-call-of-duty-infinite-warfare-dodi-repack/")
        embed.add_field(name="Call Of Duty Black Ops 3", value="https://dodi-repacks.site/index.php/2019/05/22/360-call-of-duty-black-ops-3-v88-0-0-0-all-dlcs-dodi-repack/")
        embed.add_field(name="Call Of Duty Modern Warfare 2 Remastered", value="https://dodi-repacks.site/index.php/2020/05/07/618-call-of-duty-modern-warfare-2-campaign-remastered-v1-1-2-12792-92-multi13-dodi-repack/")
        embed.add_field(name="Call Of Duty World At War", value="https://dodi-repacks.site/index.php/2019/06/04/373-call-of-duty-world-at-war-dodi-repack/")
        embed.add_field(name="Call Of Duty WW2", value="https://dodi-repacks.site/index.php/2020/03/12/554-call-of-duty-wwii-digital-deluxe-edition-build-7831931-all-dlcs-multiplayer-zombies-multi12-fast-install-from-69-6-gb-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!dodi-callofjuarez":
        embed = discord.Embed(title="Here's the Call Of Juarez Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Call Of Juarez: Bound In Blood", value="https://dodi-repacks.site/index.php/2019/12/04/489-call-of-juarez-bound-in-blood-v1-1-0-0-dodi-repack/")
        embed.add_field(name="Call Of Juarez: Gunslinger", value="https://dodi-repacks.site/index.php/2019/11/27/486-call-of-juarez-gunslinger-update-v1-05-dlcs-multi9-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!dodi-batman":
        embed = discord.Embed(title="Here's the Batman Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Batman Arkham Knight", value="https://dodi-repacks.site/index.php/2019/04/30/339-batman-arkham-knight-premium-edition-v1-6-2-0-all-dlcs-multi10-dodi-repack-from-28-gb/")
        embed.add_field(name="Batman Arkham Origins", value="https://dodi-repacks.site/index.php/2019/04/28/338-batman-arkham-origins-complete-edition-dodi-repack/")
        embed.add_field(name="Batman Arkham City", value="https://dodi-repacks.site/index.php/2019/04/28/337-batman-arkham-city-complete-edition-dodi-repack/")
        embed.add_field(name="Batman Arkham Asylum", value="https://dodi-repacks.site/index.php/2019/04/25/336-batman-arkham-asylum-game-of-the-year-edition-dodi-repack/")
        embed.add_field(name="Batman The Enemy Within", value="https://dodi-repacks.site/index.php/2018/10/23/152-batman-the-enemy-within-complete-season-multi9-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!dodi-bioshock":
        embed = discord.Embed(title="Here's the Bioshock Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Bioshock Remastered", value="https://dodi-repacks.site/index.php/2020/07/31/712-bioshock-remastered-v1-0-122872-multi6-from-4-7-gb-dodi-repack/")
        embed.add_field(name="Bioshock 2 Remastered", value="https://dodi-repacks.site/index.php/2020/07/31/713-bioshock-2-remastered-v1-0-122864-dlcs-multi7-from-6-7-gb-dodi-repack/")
        embed.add_field(name="Bioshock Infinite", value="https://dodi-repacks.site/index.php/2020/07/31/711-bioshock-infinite-the-complete-edition-multi11-from-12-5-gb-dodi-repack/" )
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!dodi-borderlands":
        embed = discord.Embed(title="Here's the Borderlands Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Borderlands: Game Of The Year Edition", value="https://dodi-repacks.site/index.php/2018/12/23/225-borderlands-game-of-the-year-edition-v1-5-0-all-dlcs-multi5-dodi-repack/")
        embed.add_field(name="Borderlands 2", value="https://dodi-repacks.site/index.php/2018/12/23/226-borderlands-2-v1-8-3-dlcs-multi8-dodi-repack/")
        embed.add_field(name="Borderlands 3", value="https://dodi-repacks.site/index.php/2020/10/04/782-borderlands-3-super-deluxe-edition-build-5382210-all-dlcs-multi11-fast-install-from-77-7-gb-dodi-repack/" )
        await message.channel.send(content=None, embed=embed)
    ...
    
    ...
    if message.content == "!dodi-deadspace":
        embed = discord.Embed(title="Here's the Deadspace Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Deadspace", value="https://dodi-repacks.site/index.php/2019/01/10/243-dead-space-multi11-dodi-repack-from-2-9-gb/")
        embed.add_field(name="Deadspace 2", value="https://dodi-repacks.site/index.php/2019/01/10/244-dead-space-2-multi11-dodi-repack-from-4-9-gb/")
        embed.add_field(name="Deadspace 3", value="https://dodi-repacks.site/index.php/2019/01/10/245-dead-space-3-v1-0-0-1-awakened-dlc-multi11-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!dodi-crysis":
        embed = discord.Embed(title="Here's the Crysis Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Crysis", value="https://dodi-repacks.site/index.php/2019/03/04/290-crysis-v1-1-1-6156-multi11-dodi-repack-from-3-4-gb/")
        embed.add_field(name="Crysis 2: Maximum Edition", value="https://dodi-repacks.site/index.php/2019/03/05/292-crysis-2-maximum-edition-v1-9-multi11-dodi-repack-from-4-8-gb/")
        embed.add_field(name="Crysis 3", value="https://dodi-repacks.site/index.php/2019/03/05/293-crysis-3-digital-deluxe-edition-v-1-3-bonus-multi10-dodi-repack-from-8-4-gb/")
        embed.add_field(name="Crysis Warhead", value="https://dodi-repacks.site/index.php/2019/03/04/291-crysis-warhead-v1-1-1-711-multi11-dodi-repack-from-3-3-gb/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!masquerade-fallout":
        embed = discord.Embed(title="Here's some Fallout Repack Collection", description="Pick your choice")
        embed.add_field(name="Fallout 3", value="https://masquerade.site/fallout-3-game-of-the-year-edition/")
        embed.add_field(name="Fallout New Vegas", value="https://masquerade.site/fallout-new-vegas-ultimate-edition/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!dodi-forza":
        embed = discord.Embed(title="Here's some Forza Repack Collection", description="Remember to use a torrent client")
        embed.add_field(name="Forza Horizon 4", value="https://dodi-repacks.site/index.php/2020/09/03/429-forza-horizon-4-ultimate-edition-v1-332-904-2-all-expansions-missing-dlc-multi16-dodi-repack-from-44-3-gb/")
        embed.add_field(name="Forza Horizon 3", value="https://dodi-repacks.site/index.php/2019/06/10/379-forza-horizon-3-v1-0-119-1002-44-dlcs-multi13-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-mortalkombat":
        embed = discord.Embed(title="Here's some Mortal Kombat Repack Collection", description="Remember to use a torrent client")
        embed.add_field(name="Mortal Kombat 11", value="https://fitgirl-repacks.site/mortal-kombat-11/")
        embed.add_field(name="Mortal Kombat XL", value="https://fitgirl-repacks.site/mortal-kombat-xl/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-witcher":
        embed = discord.Embed(title="Here's some Witcher Repack Collection", description="Remember to use a torrent client")
        embed.add_field(name="Witcher: Enhanced Edition", value="https://fitgirl-repacks.site/the-witcher-enhanced-edition/")
        embed.add_field(name="Witcher 2: Assassins of the Kings", value="https://fitgirl-repacks.site/the-witcher-2-assassins-of-kings-enhanced-edition/")
        embed.add_field(name="Witcher 3: Wild Hunt", value="https://fitgirl-repacks.site/witcher-3-wild-hunt-game-year-edition/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!soft":
        embed = discord.Embed(title="Here's some required/important software for pirating", description="Some of these are a must")
        embed.add_field(name="qBittorent", value="https://www.qbittorrent.org/download.php")
        embed.add_field(name="uBlock Origin for Firefox", value="https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/")
        embed.add_field(name="uBlock Origin For Chrome", value="https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm?hl=en")
        embed.add_field(name="JDownloader2(FOR DDL)", value="https://jdownloader.org/jdownloader2")
        embed.add_field(name="7Zip Archive", value=" https://www.7-zip.org/download.html")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!ddl":
        embed = discord.Embed(title="Here's some DDL games links", description="Must use uBlock Origin and JDownloader2")
        embed.add_field(name="Assassin's Creed DDL Collection", value="!ddl-ac")
        embed.add_field(name="Red Dead Redemption 2 DDL ", value="!ddl-rdr2")
        embed.add_field(name="Mass Effect DDL Collection", value="!ddl-masseffect")
        embed.add_field(name="Crysis DDL Collection", value="!ddl-crysis")
        embed.add_field(name="GTA DDL Collection", value="!ddl-gta")
        embed.add_field(name="Borderlands DDL Collection", value="!ddl-borderlands")
        embed.add_field(name="Mafia DDL Collection", value="!ddl-mafia")
        embed.add_field(name="Doom DDL Collection", value='!ddl-doom')
        embed.add_field(name="Far Cry DDL Collection", value="!ddl-farcry")
        embed.add_field(name="Tom Clancy DDL Collection", value="!ddl-tomclancy")
        embed.add_field(name="Watch Dogs DDL Collection", value="!ddl-watchdogs")
        embed.add_field(name="Need For Speed DDL Collection", value="!ddl-nfs")
        embed.add_field(name="Call Of Duty DDL Collection", value="!ddl-cod")
        embed.add_field(name="Deadspace DDL Collection", value="!ddl-deadspace")
        embed.add_field(name="Battlefield DDL Collection", value="!ddl-battlefield")
        embed.add_field(name="Star wars DDL Collection", value="!ddl-starwars")
        embed.add_field(name="Batman DDL Collection", value="!ddl-batman")
        embed.add_field(name="Spiderman DDL Collection", value="!ddl-spiderman")
        embed.add_field(name="Marvel DDL Collection", value="!ddl-marvel")
        embed.add_field(name="Bioshock DDL Collection", value="!ddl-bioshock")
        embed.add_field(name="Lego DDL Collection", value="!ddl-lego")
        embed.add_field(name="More DDL Collections", value="!ddl-2")
        await message.channel.send(content=None, embed=embed)
    ... 

    ...
    if message.content == "!ddl-ac":
        embed = discord.Embed(title="Here's some Assassins creed DDL links", description="Must use uBlock Origin and JDownloader2")
        embed.add_field(name="Assassin's Creed 3 Remastered", value="https://www.ovagames.com/assassins-creed-iii-remastered-multi13-elamigos.html")
        embed.add_field(name="Assassin's Creed Syndicate", value="https://www.ovagames.com/assassins-creed-syndicate-gold-edition-multi16-elamigos.html")
        embed.add_field(name="Assassin's Creed Odyssey", value="https://www.ovagames.com/assassins-creed-odyssey-gold-edition-multi15-elamigos.html")
        embed.add_field(name="Assassin's Creed Origins", value="https://www.ovagames.com/assassins-creed-origins-the-curse-of-the-pharaohs-codex.html")
        embed.add_field(name="Assassin's Creed Rogue", value="https://www.ovagames.com/assassins-creed-rogue-codex.html")
        embed.add_field(name="Assassin's Creed Unity", value="https://www.ovagames.com/assassins-creed-unity-gold-edition-multi13-elamigos.html")
        embed.add_field(name="Assassin's Creed Liberation", value="https://www.ovagames.com/assassins-creed-liberation-hd-skidrow.html")
        embed.add_field(name="Assassin's Creed 4: Black Flag", value="https://www.ovagames.com/assassins-creed-iv-black-flag-jackdaw-edition-multi19-elamigos.html")
        embed.add_field(name="Assassin's Creed 3", value="https://www.ovagames.com/assassins-creed-iii-complete-edition-multi17-elamigos.html")
        embed.add_field(name="Assassin's Creed Revelations", value="https://www.ovagames.com/assassins-creed-revelations-gold-edition-multi13-elamigos.html")
        embed.add_field(name="Assassin's Creed Brotherhood", value="https://www.ovagames.com/assassins-creed-brotherhood-complete-edition-multi13-elamigos.html")
        embed.add_field(name="Assassin's Creed 2", value="https://www.ovagames.com/assassins-creed-ii-deluxe-edition-multi11-elamigos.html")
        embed.add_field(name="Assassin's Creed 1", value="https://www.ovagames.com/assassins-creed-directors-cut-gog.html")
        await message.channel.send(content=None, embed=embed)
    ... 

    ...
    if message.content == "!ddl-rdr2":
        embed = discord.Embed(title="Here's some DDL games links", description="Must use uBlock Origin and JDownloader2")
        embed.add_field(name="Red Dead Redemption 2", value="https://www.ovagames.com/red-dead-redemption-2-multi13-elamigos.html")
        await message.channel.send(content=None, embed=embed)
    ... 

    ...
    if message.content == "!fitgirl-rdr2":
        embed = discord.Embed(title="Here's some RDR2 games links", description="Remember to use torrent client")
        embed.add_field(name="Red Dead Redemption 2", value="https://fitgirl-repacks.site/red-dead-redemption-2/")
        await message.channel.send(content=None, embed=embed)
    ... 
    
    ...
    if message.content == "!ddl-masseffect":
        embed = discord.Embed(title="Here's some DDL games links", description="MUst use uBlock Origin and JDownloader2")
        embed.add_field(name="Mass Effect Andromeda ", value="https://www.ovagames.com/mass-effect-andromeda-cpy-253.html")
        embed.add_field(name="Mass Effect", value="https://www.ovagames.com/mass-effect-ultimate-edition-multi6-elamigos-977.html")
        embed.add_field(name="Mass Effect 2", value="https://www.ovagames.com/mass-effect-2-ultimate-edition-multi9-elamigos-062.html")
        embed.add_field(name="Mass Effect 3", value="https://www.ovagames.com/mass-effect-3-complete-edition-multi8-elamigos-843.html")
        await message.channel.send(content=None, embed=embed)
    ... 

    ...
    if message.content == "!ddl-crysis":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Crysis Remastered", value="https://www.ovagames.com/crysis-remastered-multi12-elamigos.html")
        embed.add_field(name="Crysis 3", value= "https://www.ovagames.com/crysis-3-reloaded.html")
        embed.add_field(name="Crysis 2",value= " https://www.ovagames.com/crysis-2-maximum-edition-prophet.html")
        embed.add_field(name="Crysis Warhead",value= "https://www.ovagames.com/crysis-warhead-gog.html")
        embed.add_field(name= "Crysis 1",value = "https://www.ovagames.com/crysis-warhead-gog.html")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!ddl-gta":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="GTA 5", value="https://www.ovagames.com/grand-theft-auto-v-multi12-elamigos.html")
        embed.add_field(name="GTA Vice City", value="https://www.ovagames.com/grand-theft-auto-vice-city-multi10-elamigos.html")
        embed.add_field(name="GTA San Andreas",value="https://www.ovagames.com/grand-theft-auto-san-andreas-multi10-elamigos.html")
        embed.add_field(name="GTA 4",value="https://www.ovagames.com/grand-theft-auto-iv-complete-edition-multi5-prophet.html")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!ddl-borderlands":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Borderlands 3",value="https://www.ovagames.com/borderlands-3-multi7-elamigos.html")
        embed.add_field(name="Borderlands Game Of The Year Edition",value=" https://www.ovagames.com/borderlands-game-of-the-year-enhanced-plaza.html")
        embed.add_field(name="Borderlands The Pre Sequel Remastered",value="https://www.ovagames.com/borderlands-the-pre-sequel-remastered-plaza.html")
        embed.add_field(name="Borderlands 2 Remastered",value="https://www.ovagames.com/borderlands-2-remastered-plaza.html")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!ddl-mafia":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Mafia Definitive Edition",value="https://www.ovagames.com/mafia-definitive-edition-multi14-elamigos.html")
        embed.add_field(name="Mafia 3 Definitive Edition",value="https://www.ovagames.com/mafia-iii-definitive-edition-codex.html")
        embed.add_field(name="Mafia 2",value="https://www.ovagames.com/mafia-ii-multi8-plaza.html")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!ddl-doom":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Doom 3 BFG Edition",value="https://www.ovagames.com/doom-3-bfg-edition-gog.html")
        embed.add_field(name="Doom Eternal",value="https://www.ovagames.com/doom-eternal-codex.html")
        embed.add_field(name="Doom 2016",value="https://www.ovagames.com/doom-2016-multi10-elamigos.html")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!ddl-farcry":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Far Cry New Dawn",value="https://www.ovagames.com/far-cry-new-dawn-codex-732.html")
        embed.add_field(name="Far Cry Primal",value="https://www.ovagames.com/far-cry-primal-cpy-231.html")
        embed.add_field(name="Far Cry 5",value="https://www.ovagames.com/far-cry-5-dead-living-zombies-codex-420.html")
        embed.add_field(name="Far Cry 4",value="https://www.ovagames.com/far-cry-4-gold-edition-multi15-elamigos-505.html")
        embed.add_field(name="Far Cry 3 Blood Dragon",value="https://www.ovagames.com/far-cry-3-blood-dragon-reloaded-801.html")
        embed.add_field(name="Far Cry 3",value="https://www.ovagames.com/far-cry-3-complete-collection-multi13-elamigos-277.html")
        embed.add_field(name="Far Cry 2",value="https://www.ovagames.com/far-cry-2-fortunes-edition-gog.html")
        embed.add_field(name="Far Cry 1",value="https://www.ovagames.com/far-cry-gog.html")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!ddl-tomclancy": 
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Tom Clancys Rainbow Six Siege",value="https://www.ovagames.com/tom-clancys-rainbow-six-siege-operation-wind-bastion-plaza.html")
        embed.add_field(name="Tom Clancys Rainbow Six Vegas 2",value="https://www.ovagames.com/tom-clancys-rainbow-six-vegas-2-reloaded.html")
        embed.add_field(name="Tom Clancys Splinter Cell Blacklist",value="https://www.ovagames.com/tom-clancys-splinter-cell-blacklist-complete-multi14-elamigos.html")
        embed.add_field(name="Tom Clancys Splinter Cell Conviction",value="https://www.ovagames.com/tom-clancys-splinter-cell-conviction-complete-multi11-elamigos.html")
        embed.add_field(name="Tom Clancys Splinter Cell Double Agent",value="https://www.ovagames.com/tom-clancys-splinter-cell-double-agent-multi6-elamigos.html")
        embed.add_field(name="Tom Clancys Ghost Recon Wildlands",value="https://www.ovagames.com/tom-clancys-ghost-recon-wildlands-gold-edition-multi16-elamigos.html")
        embed.add_field(name="Tom Clancys Splinter Cell Chaos Theory",value="https://www.ovagames.com/tom-clancys-splinter-cell-chaos-theory-multi6-elamigos.html")
        embed.add_field(name="Tom Clancys Splinter Cell Pandora Tomorrow",value="https://www.ovagames.com/tom-clancys-splinter-cell-pandora-tomorrow-multi6-elamigos.html")
        embed.add_field(name="Tom Clancys Ghost Recon Future Soldier",value="https://www.ovagames.com/tom-clancys-ghost-recon-future-soldier-complete-edition-multi12-elamigos.html")
        embed.add_field(name="Tom Clancys Endwar",value="https://www.ovagames.com/tom-clancys-endwar-multi6-elamigos.html")
        embed.add_field(name="Tom Clancys Ghost Recon Advanced Fighter 2",value="https://www.ovagames.com/ghost-recon-advanced-warfighter-2-skidrow.html")
        embed.add_field(name="Tom Clancys Ghost Recon Advanced Fighter",value="https://www.ovagames.com/ghost-recon-advanced-warfighter-reloaded.html")
        await message.channel.send(content=None, embed=embed)
    ... 

    ...
    if message.content == "!handbook":
        embed = discord.Embed(title="Here's the handy dandy handbook!", description="Very essential for a pirate")
        embed.add_field(name="r/PiratedGames Megathread",value="https://www.reddit.com/r/PiratedGames/comments/i2uun1/rpiratedgames_mega_thread/")
        embed.add_field(name="Biggest Megathread For Piracy",value="https://www.reddit.com/r/FREEMEDIAHECKYEAH/wiki/index")
        embed.add_field(name="Beginner's Guide for Pirating",value="https://github.com/Bonfire-GTK/newpirates/blob/master/README.md")
        await message.channel.send(content=None, embed=embed)
    ...   
    
    ...
    if message.content == "!fitgirl-darksouls":
        embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
        embed.add_field(name="Dark Souls Remastered",value="https://fitgirl-repacks.site/dark-souls-remastered/")
        embed.add_field(name="Dark Souls 2",value="https://fitgirl-repacks.site/dark-souls-2-scholar-of-the-first-sin/")
        embed.add_field(name="Dark Souls 3",value="https://fitgirl-repacks.site/dark-souls-2-scholar-of-the-first-sin/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-dirt":
        embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
        embed.add_field(name="Dirt 3", value="https://fitgirl-repacks.site/dirt-3-complete-edition/")
        embed.add_field(name="Dirt 4", value="https://fitgirl-repacks.site/dirt-4/")
        embed.add_field(name="Dirt Rally",value="https://fitgirl-repacks.site/dirt-rally/")
        embed.add_field(name="Dirt Rally 2.0",value="https://fitgirl-repacks.site/dirt-rally-2-0/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-dishonoured":
        embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
        embed.add_field(name="Dishonoured",value="https://fitgirl-repacks.site/dishonored-complete-collection/")
        embed.add_field(name="Dishonoured Definitive Edition",value="https://fitgirl-repacks.site/dishonored-game-of-the-year-edition/")
        embed.add_field(name="Dishonoured 2",value=" https://fitgirl-repacks.site/dishonored-2/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-dmc":
        embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
        embed.add_field(name="DMC",value="https://fitgirl-repacks.site/devil-may-cry-hd-collection/")
        embed.add_field(name="DMC 4",value="https://fitgirl-repacks.site/devil-may-cry-4-special-edition/")
        embed.add_field(name="DMC 5",value="https://fitgirl-repacks.site/devil-may-cry-5/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-deusex":
        embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
        embed.add_field(name="Dues Ex Human Revolution",value=" https://fitgirl-repacks.site/deus-ex-human-revolution-twin-pack/")
        embed.add_field(name="Dues Ex Mankind Divided",value="https://fitgirl-repacks.site/deus-ex-mankind-divided/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-dragonball":
        embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
        embed.add_field(name="Dragon Ball Fighter Z",value="https://fitgirl-repacks.site/dragon-ball-fighterz/")
        embed.add_field(name="Dragon Ball Z Karakot",value="https://fitgirl-repacks.site/dragon-ball-z-kakarot/")
        embed.add_field(name="Dragon Ball Xenoverse",value="https://fitgirl-repacks.site/dragon-ball-xenoverse-bundle-edition-v1-07-4-dlcs/")
        embed.add_field(name="Dragon Ball Xenoverse 2",value="https://fitgirl-repacks.site/dragon-ball-xenoverse-2/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-f1":
        embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
        embed.add_field(name="F1 2015",value="https://fitgirl-repacks.site/f1-2015-update-2/")
        embed.add_field(name="F1 2016",value="https://fitgirl-repacks.site/f1-2016/")
        embed.add_field(name="F1 2017",value="https://fitgirl-repacks.site/f1-2017/")
        embed.add_field(name="F1 2018",value="https://fitgirl-repacks.site/f1-2018/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-gearsofwar":
        embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
        embed.add_field(name="Gears Of War 4",value="https://fitgirl-repacks.site/gears-of-war-4/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-fifa":
        embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
        embed.add_field(name="FIFA 15",value="https://fitgirl-repacks.site/fifa-15-ultimate-team-edition/")
        embed.add_field(name="FIFA 16",value="https://fitgirl-repacks.site/fifa-16-super-deluxe-edition-not-cracked/")
        embed.add_field(name="FIFA 17",value="https://fitgirl-repacks.site/fifa-17/")
        embed.add_field(name="FIFA 18",value="https://fitgirl-repacks.site/fifa-18/")
        embed.add_field(name="FIFA 19",value="https://fitgirl-repacks.site/fifa-19/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-finalfantasy":
        embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
        embed.add_field(name="Final Fantasy IV",value="https://fitgirl-repacks.site/final-fantasy-iv-the-after-years/")
        embed.add_field(name="Final Fantasy V",value="https://fitgirl-repacks.site/final-fantasy-v/")
        embed.add_field(name="Final Fantasy VIII",value="https://fitgirl-repacks.site/final-fantasy-viii-remastered/")
        embed.add_field(name="Final Fantasy X",value="https://fitgirl-repacks.site/final-fantasy-xx-2-hd-remaster/")
        embed.add_field(name="Final Fantasy XII",value="https://fitgirl-repacks.site/final-fantasy-xii-the-zodiac-age/")
        embed.add_field(name="Final Fantasy XIII",value="https://fitgirl-repacks.site/final-fantasy-xiii/")
        await message.channel.send(content=None, embed=embed)
    ...
    ...
    if message.content == "!fitgirl-fm":
        embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
        embed.add_field(name="Football Manager 2015", value="https://fitgirl-repacks.site/football-manager-2015-v15-3-2/")
        embed.add_field(name="Football Manager 2016", value="https://fitgirl-repacks.site/football-manager-2016-v16-2-0/")
        embed.add_field(name="Football Manager 2017",value="https://fitgirl-repacks.site/football-manager-2017/")
        embed.add_field(name="Football Manager 2018",value="https://fitgirl-repacks.site/football-manager-2018/")
        embed.add_field(name="Football Manager 2019",value="https://fitgirl-repacks.site/football-manager-2019/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-halo":
        embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
        embed.add_field(name="Halo Wars 2", value="https://fitgirl-repacks.site/halo-wars-2-complete-edition/")
        embed.add_field(name="Halo Spartan Strike", value="https://fitgirl-repacks.site/halo-spartan-strike/")
        embed.add_field(name="Halo Master Chief Collection",value="https://fitgirl-repacks.site/halo-the-master-chief-collection/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-hitman":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Hitman 2",value="https://fitgirl-repacks.site/hitman-2/")
       embed.add_field(name="Hitman GO",value="https://fitgirl-repacks.site/hitman-go-definitive-edition/")
       embed.add_field(name="Hitman 2016",value="https://fitgirl-repacks.site/hitman-game-of-the-year-edition/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-mgs":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Metal Gear Solid 5",value="phantom pain: https://fitgirl-repacks.site/metal-gear-solid-v-phantom-pain/")
       embed.add_field(name="Metal Gear Solid Ground Zero",value="https://fitgirl-repacks.site/metal-gear-solid-v-ground-zeroes-v1-0-0-5-crackfix/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-minecraft":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Minecraft Dungeons",value="https://fitgirl-repacks.site/minecraft-dungeons/")
       embed.add_field(name="Minecraft Story Mode Season 1",value="https://fitgirl-repacks.site/minecraft-story-mode-complete-season-episodes-1-8/")
       embed.add_field(name="Minecraft Story Mode Season 2",value="https://fitgirl-repacks.site/minecraft-story-mode-season-2/")
       embed.add_field(name="Minecraft Java Edition",value="https://tlauncher.org/en/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-motogp":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Moto GP 14",value="https://fitgirl-repacks.site/motogp-14-complete-edition-v1-001-4-dlcs/")
       embed.add_field(name="Moto GP 15",value="https://fitgirl-repacks.site/motogp-15-complete/")
       embed.add_field(name="Moto GP 17",value="https://fitgirl-repacks.site/motogp-17/")
       embed.add_field(name="Moto GP 18",value="https://fitgirl-repacks.site/motogp-18/")
       embed.add_field(name="Moto GP 19",value="https://fitgirl-repacks.site/motogp-19/")
       embed.add_field(name="Moto GP 20",value="https://fitgirl-repacks.site/motogp-20/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-nba":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="NBA 2K16",value="https://fitgirl-repacks.site/nba-2k16-update-1/")
       embed.add_field(name="NBA 2K17",value="https://fitgirl-repacks.site/nba-2k17-update-1-working-online/")
       embed.add_field(name="NBA 2K18",value="https://fitgirl-repacks.site/nba-2k18/")
       embed.add_field(name="NBA 2K19",value="https://fitgirl-repacks.site/nba-2k19-20th-anniversary-edition/")
       embed.add_field(name="NBA 2K20",value="https://fitgirl-repacks.site/nba-2k20/")
       embed.add_field(name="NBA 2K21",value="https://fitgirlrepacks.site/nba-2k21/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-pes":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="PES 2016",value="https://fitgirl-repacks.site/pro-evolution-soccer-2016-v1-05-data-pack-4-0/")
       embed.add_field(name="PES 2017",value="https://fitgirl-repacks.site/pro-evolution-soccer-2017-v1-01-00/")
       embed.add_field(name="PES 2018",value="https://fitgirl-repacks.site/pro-evolution-soccer-2018/")
       embed.add_field(name="PES 2019",value="https://fitgirl-repacks.site/pro-evolution-soccer-2019/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-projectcars":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Project Cars",value="https://fitgirl-repacks.site/project-cars/")
       embed.add_field(name="Project Cars 2",value="https://fitgirl-repacks.site/project-cars-2/")
       embed.add_field(name="Project Cars 3",value="https://fitgirl-repacks.site/project-cars-3/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-prototype":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Prototype",value="https://fitgirl-repacks.site/prototype/")
       embed.add_field(name="Prototype 2",value="https://fitgirl-repacks.site/prototype-2/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-residentevil":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Resident Evil Remastered",value="https://fitgirl-repacks.site/resident-evil-hd-remaster/")
       embed.add_field(name="Resident Evil 2",value="https://fitgirl-repacks.site/resident-evil-2-deluxe-edition/")
       embed.add_field(name="Resident Evil 3",value="https://fitgirl-repacks.site/resident-evil-3/")
       embed.add_field(name="Resident Evil 4", value="https://fitgirl-repacks.site/resident-evil-4-ultimate-hd-edition/")
       embed.add_field(name="Resident Evil 5",value="https://fitgirl-repacks.site/resident-evil-5-gold-edition/")
       embed.add_field(name="Resident Evil 6",value="https://fitgirl-repacks.site/resident-evil-6/")
       embed.add_field(name="Resident Evil 7",value="https://fitgirl-repacks.site/resident-evil-7-biohazard/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-saintsrow":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Saints Row Gat Out Of Hell",value="https://fitgirl-repacks.site/saints-row-gat-out-of-hell-update-1-included/")
       embed.add_field(name="Saints Row iv",value="https://fitgirl-repacks.site/saints-row-iv-game-of-the-century-edition/")
       embed.add_field(name="Saints Row The Third",value="https://fitgirl-repacks.site/saints-row-the-third-remastered/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-serioussam":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Serious Sam 3 BFE Edition",value="https://fitgirl-repacks.site/serious-sam-3-bfe-v233089-jewel-of-the-nile-dlc/")
       embed.add_field(name="Serious Sam 4",value="https://fitgirl-repacks.site/serious-sam-4/")
       embed.add_field(name="Serious Sam The Second Encounter",value="https://fitgirl-repacks.site/serious-sam-hd-the-second-encounter/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-sniperelite":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Sniper Elite V2",value="https://fitgirl-repacks.site/sniper-elite-v2-v1-13-5-dlcs/")
       embed.add_field(name="Sniper Elite 3",value="https://fitgirl-repacks.site/sniper-elite-3-v1-15a-dlcs-multiplayer/")
       embed.add_field(name="Sniper Elite 4",value="https://fitgirl-repacks.site/sniper-elite-4-deluxe-edition/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-skyrim":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Elder Scrolls V",value="https://fitgirl-repacks.site/elder-scrolls-skyrim-special-edition/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-evilwithin":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="The Evil Within",value="https://fitgirl-repacks.site/the-evil-within/")
       embed.add_field(name="The Evil Within 2",value="https://fitgirl-repacks.site/the-evil-within-2/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-walkingdead":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Walking Dead Final Season",value="https://fitgirl-repacks.site/the-walking-dead-the-final-season/")
       embed.add_field(name="Walking Dead Telltale Definitive Series",value="https://fitgirl-repacks.site/the-walking-dead-the-telltale-definitive-series/")
       embed.add_field(name="Walking Dead New Frontier",value="https://fitgirl-repacks.site/walking-dead-new-frontier-complete-season/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-sims":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Sims 3",value="https://fitgirl-repacks.site/the-sims-3/")
       embed.add_field(name="Sims 4",value="https://fitgirl-repacks.site/sims-4-deluxe-edition/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-wolfenstein":
       embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
       embed.add_field(name="Wolfenstein ii New Collossus",value="https://fitgirl-repacks.site/wolfenstein-ii-the-new-colossus/")
       embed.add_field(name="Wolfenstein The Old Blood",value="https://fitgirl-repacks.site/wolfenstein-the-old-blood/")
       embed.add_field(name="Wolfenstein Youngblood",value="https://fitgirl-repacks.site/wolfenstein-youngblood/")
       await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!fitgirl-wwe":
      embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
      embed.add_field(name="WWE 2K Battlegrounds",value="https://fitgirl-repacks.site/wwe-2k-battlegrounds/")
      embed.add_field(name="WWE 2K15",value="https://fitgirl-repacks.site/wwe-2k15-all-dlcs/")
      embed.add_field(name="WWE 2K16",value="https://fitgirl-repacks.site/wwe-2k16-all-dlcs/")
      embed.add_field(name="WWE 2K17",value="https://fitgirl-repacks.site/wwe-2k17-digital-deluxe-edition-6-dlc-update-1/")
      embed.add_field(name="WWE 2K18",value="https://fitgirl-repacks.site/wwe-2k18/")
      embed.add_field(name="WWE 2K19",value="https://fitgirl-repacks.site/wwe-2k19/")
      embed.add_field(name="WWE 2K20",value="https://fitgirl-repacks.site/wwe-2k20/")
      await message.channel.send(content=None, embed=embed)
    ...
    if message.content == "!fitgirl-xcom":
      embed = discord.Embed(title="Here is a repack collection for you", description="Use a torrent client to download")
      embed.add_field(name="XCOM Chimera Squad",value="https://fitgirl-repacks.site/xcom-chimera-squad/")
      embed.add_field(name="XCOM 2",value="https://fitgirl-repacks.site/xcom-2-digital-deluxe-edition/")
      embed.add_field(name="XCOM Enemy Unknown",value="https://fitgirl-repacks.site/xcom-enemy-unknown-the-complete-edition/")
      await message.channel.send(content=None, embed=embed)
    ... 
    ...
    if message.content == "!ddl-watchdogs":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Watch Dogs 1",value="https://www.ovagames.com/144-watch-dogs-complete-edition-multi19-elamigos.html")
        embed.add_field(name="Watch Dogs 2",value="https://www.ovagames.com/watch-dogs-2-multi16-plaza-453.html")
        await message.channel.send(content=None, embed=embed)
    ...  
    ...
    if message.content == "!ddl-nfs":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="NFS Payback",value="https://www.ovagames.com/need-for-speed-payback-deluxe-edition-multi10-elamigos.html")
        embed.add_field(name="NFS The Run",value="https://www.ovagames.com/need-for-speed-the-run-limited-edition-multi11-elamigos.html")
        embed.add_field(name="NFS Rivals", value="https://www.ovagames.com/need-for-speed-rivals-complete-edition-multi11-elamigos-742.html")
        embed.add_field(name="NFS Shift 2 Unleashed", value="https://www.ovagames.com/need-for-speed-shift-2-unleashed-reloaded-944.html")
        embed.add_field(name="NFS Shift", value="https://www.ovagames.com/need-for-speed-shift-reloaded-698.html")
        embed.add_field(name="NFS Hot Pursuit", value="https://www.ovagames.com/need-for-speed-hot-pursuit-multi12-prophet-857.html")
        embed.add_field(name="NFS Carbon", value="https://www.ovagames.com/need-for-speed-carbon-collectors-edition-razor1911-379.html")
        embed.add_field(name="NFS Heat", value="https://www.ovagames.com/need-for-speed-heat-multi7-elamigos.html")
        embed.add_field(name="NFS ProStreet", value="https://www.ovagames.com/need-for-speed-prostreet-multi13-elamigos.html")
        embed.add_field(name="NFS Most Wanted 2012", value="https://www.ovagames.com/need-for-speed-most-wanted-limited-edition-plaza.html")
        embed.add_field(name="NFS Undercover", value="https://www.ovagames.com/need-for-speed-undercover-multi13-prophet.html")
        await message.channel.send(content=None, embed=embed)
    ...
    ...
    if message.content == "!ddl-cod":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="COD WW2",value="https://www.ovagames.com/call-of-duty-wwii-multi12-prophet.html")
        embed.add_field(name="COD BO3 + Zombies Chronicles",value="https://www.ovagames.com/call-of-duty-black-ops-iii-zombies-chronicles-reloaded-213.html")
        embed.add_field(name="COD Infinite Warfare", value="https://www.ovagames.com/call-of-duty-infinite-warfare-reloaded.html")
        embed.add_field(name="COD Modern Warfare Remastered", value="https://www.ovagames.com/call-of-duty-modern-warfare-remastered-codex.html")
        embed.add_field(name="COD Advanced Warfare", value="https://www.ovagames.com/call-of-duty-advanced-warfare-multi8-prophet.html")
        embed.add_field(name="COD Ghosts", value="https://www.ovagames.com/call-of-duty-ghosts-multi6-prophet.html")
        embed.add_field(name="COD 4: Modern Warfare", value="https://www.ovagames.com/call-of-duty-4-modern-warfare-multi7-elamigos-890.html")
        embed.add_field(name="COD Black Ops 2", value="https://www.ovagames.com/call-of-duty-black-ops-ii-multi5-plaza-718.html")
        embed.add_field(name="COD MW3", value="https://www.ovagames.com/call-of-duty-modern-warfare-3-multi6-plaza.html")
        embed.add_field(name="COD MW2", value="https://www.ovagames.com/call-of-duty-modern-warfare-2-multi7-prophet.html")
        embed.add_field(name="COD Black Ops", value="https://www.ovagames.com/call-of-duty-black-ops-multi6-plaza.html")
        embed.add_field(name="COD World At War", value="https://www.ovagames.com/call-of-duty-world-at-war-multi7-elamigos.html")
        embed.add_field(name="COD Deluxe Edition", value="https://www.ovagames.com/call-of-duty-deluxe-edition-multi7-elamigos.html")
        await message.channel.send(content=None, embed=embed)
    ...
    ...
    if message.content == "!ddl-deadspace":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Dead Space 1",value="https://www.ovagames.com/dead-space-gog.html")
        embed.add_field(name="Dead Space  2",value="https://www.ovagames.com/dead-space-2-flt.html")
        embed.add_field(name="Dead Space 3", value="https://www.ovagames.com/dead-space-3-reloaded.html")
        await message.channel.send(content=None, embed=embed)
    ... 
    ...
    if message.content == "!ddl-battlefield":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Battlefield V",value="https://www.ovagames.com/battlefield-v-cpy.html")
        embed.add_field(name="Battlefield 1",value="https://www.ovagames.com/battlefield-1-ultimate-edition-multi12-elamigos.html")
        embed.add_field(name="Battlefield 4", value="https://www.ovagames.com/battlefield-4-reloaded.html")
        embed.add_field(name="Battlefield 3", value="https://www.ovagames.com/battlefield-3-reloaded.html")
        embed.add_field(name="Battlefield Bad Company 2", value="https://www.ovagames.com/battlefield-bad-company-2-multi9-elamigos.html")
        embed.add_field(name="Battlefield 2142", value="https://www.ovagames.com/battlefield-2142-razor1911.html")
        embed.add_field(name="Battlefield Hardline", value="https://www.ovagames.com/battlefield-hardline-cpy.html")
        await message.channel.send(content=None, embed=embed)
    ...  
    ...
    if message.content == "!ddl-starwars":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Star Wars: Jedi Fallen Order",value="https://www.ovagames.com/star-wars-jedi-fallen-order-codex-187.html")
        embed.add_field(name="Star Wars Force Unleashed 2",value="https://www.ovagames.com/star-wars-the-force-unleashed-ii-gog-629.html")
        embed.add_field(name="Star Wars Force Unleashed", value="https://www.ovagames.com/star-wars-the-force-unleashed-ultimate-sith-edition-gog-849.html")
        embed.add_field(name="Star Wars Battlefront II", value="https://www.ovagames.com/star-wars-battlefront-ii-codex.html")
        embed.add_field(name="Star Wars Battlefront II Classic", value="https://www.ovagames.com/star-wars-battlefront-ii-gog.html")
        await message.channel.send(content=None, embed=embed)
    ...
    ...
    if message.content == "!ddl-batman":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Batman Arkham Knight",value="https://www.ovagames.com/batman-arkham-knight-complete-edition-multi8-elamigos.html")
        embed.add_field(name="Batman Arkham VR",value="https://www.ovagames.com/batman-arkham-vr-vrex.html")
        embed.add_field(name="Batman The Enemy Within", value="https://www.ovagames.com/batman-the-enemy-within-the-telltale-series-shadows-edition-codex.html")
        embed.add_field(name="Batman Arkham City", value="https://www.ovagames.com/batman-arkham-city-game-of-the-year-edition-multi9-prophet.html")
        embed.add_field(name="Batman Arkham Origins", value="https://www.ovagames.com/batman-arkham-origins-the-complete-edition-prophet.html")
        embed.add_field(name="Batman Arkham Asylum", value="https://www.ovagames.com/batman-arkham-asylum-game-of-the-year-edition-multi6-prophet.html")
        await message.channel.send(content=None, embed=embed)
    ...
    ...
    if message.content == "!ddl-spiderman":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Spiderman Shattered Dimensions",value="https://www.ovagames.com/203-spiderman-shattered-dimensions-reloaded.html")
        embed.add_field(name="The Amazing SpiderMan",value="https://www.ovagames.com/the-amazing-spider-man-skidrow.html")
        embed.add_field(name="The Amazing Spiderman 2", value="https://www.ovagames.com/the-amazing-spider-man-2-bundle-plaza.html")
        await message.channel.send(content=None, embed=embed)
    ...
    ...
    if message.content == "!ddl-marvel":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Marvel Avengers",value="https://www.ovagames.com/marvels-avengers-deluxe-edition-multi15-elamigos.html")
        embed.add_field(name="Marvel Ultimate Alliance 2",value="https://www.ovagames.com/688-marvel-ultimate-alliance-2-codex.html")
        embed.add_field(name="Marvel Ulitmate Alliance", value="https://www.ovagames.com/749-marvel-ultimate-alliance-codex.html")
        embed.add_field(name="Marvel vs Capcom Infinite", value="https://www.ovagames.com/marvel-vs-capcom-infinite-deluxe-edition-plaza-888.html")
        embed.add_field(name="Marvel Guardians of the galaxy: Episode 5", value="https://www.ovagames.com/marvels-guardians-of-the-galaxy-episode-5-codex.html")
        embed.add_field(name="Marvel vs Capcom 3", value="https://www.ovagames.com/ultimate-marvel-vs-capcom-3-codex.html")
        await message.channel.send(content=None, embed=embed)
    ...
    ...
    if message.content == "!ddl-bioshock":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Bioshock Remastered",value="https://www.ovagames.com/bioshock-remastered-gog.html")
        embed.add_field(name="Bioshock 2 Remastered",value="https://www.ovagames.com/bioshock-2-remastered-gog.html")
        embed.add_field(name="Bioshock Infinite", value="https://www.ovagames.com/bioshock-infinite-complete-edition-prophet.html")
        await message.channel.send(content=None, embed=embed)
    ...
    ...
    if message.content == "!ddl-lego":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Lego Star Wars force Awakens",value="https://www.ovagames.com/lego-star-wars-the-force-awakens-v1-03-incl-dlc-codex-880.html")
        embed.add_field(name="Lego Worlds",value="https://www.ovagames.com/lego-worlds-monsters-codex.html")
        embed.add_field(name="Lego Jurrasic World", value="https://www.ovagames.com/lego-jurassic-world-multi10-elamigos.html")
        embed.add_field(name="Lego The Hobbit", value="https://www.ovagames.com/lego-the-hobbit-multi10-elamigos.html")
        embed.add_field(name="Lego DC super villains", value="https://www.ovagames.com/lego-dc-super-villains-shazam-codex.html")
        embed.add_field(name="Lego Movie 2 Videogame", value="https://www.ovagames.com/the-lego-movie-2-videogame-galactic-adventures-codex.html")
        embed.add_field(name="Lego Marvel Avengers", value="https://www.ovagames.com/lego-marvels-avengers-deluxe-edition-multi10-elamigos.html")
        embed.add_field(name="Lego Incredibles", value="https://www.ovagames.com/lego-the-incredibles-codex.html")
        embed.add_field(name="Lego Marvel Super Heroes 2", value="https://www.ovagames.com/lego-marvel-super-heroes-2-infinity-war-codex.html")
        embed.add_field(name="Lego Pirates of the Caribbean", value="https://www.ovagames.com/lego-pirates-of-the-caribbean-the-video-game-gog.html")
        embed.add_field(name="Lego Indiana Jones 2", value="https://www.ovagames.com/lego-indiana-jones-2-the-adventure-continues-gog.html")
        embed.add_field(name="Lego Indiana Jones", value="https://www.ovagames.com/lego-indiana-jones-the-original-adventures-gog.html")
        embed.add_field(name="Lego Ninjago Movie Videogame", value="https://www.ovagames.com/the-lego-ninjago-movie-video-game-codex.html")
        embed.add_field(name="Lego Harry Potter Years5-7", value="https://www.ovagames.com/lego-harry-potter-years-5-7-reloaded.html")
        embed.add_field(name="Lego Harry Potter Years 1-4", value="https://www.ovagames.com/lego-harry-potter-years-1-4-reloaded.html")
        embed.add_field(name="Lego City Undercover", value="https://www.ovagames.com/lego-city-undercover-codex.html")
        embed.add_field(name="Lego Star Wars The Complete Edition", value="https://www.ovagames.com/lego-star-wars-the-complete-saga-reloaded.html")
        embed.add_field(name="Lego Batman 3: Beyond Gotham", value="https://www.ovagames.com/lego-batman-3-beyond-gotham-proper-reloaded.html")
        embed.add_field(name="Lego Star Wars 3 Clone Wars", value="https://www.ovagames.com/lego-star-wars-iii-the-clone-wars-skidrow.html")
        embed.add_field(name="Lego Movie Videogame", value="https://www.ovagames.com/the-lego-movie-videogame-flt.html")
        embed.add_field(name="Lego Batman 2 DC Super Heroes", value="https://www.ovagames.com/lego-batman-2-dc-super-heroes-reloaded.html")
        embed.add_field(name="Lego Marvel Super Heroes",value="https://www.ovagames.com/lego-marvel-super-heroes-flt.html")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!ddl-2":
        embed = discord.Embed(title="Here is a DDL collection for you", description="Use JDownloader2 for better experience")
        embed.add_field(name="Fallout DDL Collection",value="!ddl-fallout")
        embed.add_field(name="Forza DDL Collection",value="!ddl-forza")
        embed.add_field(name="Witcher DDL Collection", value="!ddl-witcher")
        embed.add_field(name="Fifa DDL Collection", value="!ddl-fifa")
        embed.add_field(name="Deus Ex DDL Collection", value="!ddl-deusex")
        embed.add_field(name="Gears of War DDL Collection", value="!ddl-gearsofwar")
        embed.add_field(name="DiRT DDL Collection", value="!ddl-dirt")
        embed.add_field(name="Dishonoured DDL Collection", value="!ddl-dishonoured")
        embed.add_field(name="Dragon Ball DDL Collection", value="!ddl-dragonball")
        embed.add_field(name="Dark Souls DDL Collection", value='!ddl-darksouls')
        embed.add_field(name="Devil May Cry DDL Collection", value="!ddl-dmc")
        embed.add_field(name="F1 DDL Collection", value="!ddl-f1")
        embed.add_field(name="Final Fantasy DDL Collection", value="!ddl-finalfantasy")
        await message.channel.send(content=None, embed=embed)
    ...





client.run('token')