import discord
import logging
import asyncio
client=discord.Client()


@client.event
async def on_message(message):
    ...
    if message.content == "!botinfo":
        embed = discord.Embed(title="Pirate Navigator Info", description="Yaar! Know who I am!")
        embed.add_field(name="Developed on", value="August 2020")
        embed.add_field(name="Programming Language", value="Python")
        embed.add_field(name="Developed by", value="Watch_Doge")
        embed.add_field(name="Version", value="1.3")
        embed.add_field(name="Source Code", value="https://github.com/HeliumSpectrum/Pirate-Navigator-Source-Code")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!games":
        embed = discord.Embed(title="Here are some games collections", description="Pick your choice!")
        embed.add_field(name="Repacks", value="!repacks")
        embed.add_field(name="Direct Download Links(Work in progress)", value="!DDL")
        embed.add_field(name="Important Software(Work in progress)", value="!soft")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-ac":
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
    if message.content == "!repacks":
        embed = discord.Embed(title="Here are some commands for repacks collections", description="Use the commands for repacks")
        embed.add_field(name="Assassin's Creed Repack Collection", value="!repacks-ac")
        embed.add_field(name="GTA Repack collection", value="!repacks-gta")
        embed.add_field(name="Free to play Games", value="!games-free")
        embed.add_field(name="Far Cry Repack Collection", value="!repacks-farcry")
        embed.add_field(name="Watch Dogs Repack Collection", value="!repacks-watchdogs")
        embed.add_field(name="Need For Speed Repack Collection", value='!repacks-nfs')
        embed.add_field(name="Tom Clancy Repack Collection", value="!repacks-splintercell")
        embed.add_field(name="Among Us", value="!repacks-amongus")
        embed.add_field(name="Mass Effect Repack Collection", value="!repacks-masseffect")
        embed.add_field(name="Star Wars Repack Collection", value="!repacks-starwars")
        embed.add_field(name="Lego Games Repack Collection", value="!repacks-lego")
        embed.add_field(name="Marvel Repack Collection", value="!repacks-marvel")
        embed.add_field(name="Ghost Recon Repack Collection", value="!repacks-ghostrecon")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-gta":
        embed = discord.Embed(title="Here are some GTA Repacks for you", description="Remember to use a torrent client")
        embed.add_field(name="GTA 5", value="https://fitgirl-repacks.site/grand-theft-auto-v/")
        embed.add_field(name="GTA 4", value=" https://fitgirl-repacks.site/grand-theft-auto-iv-complete-edition/")
        embed.add_field(name="GTA Vice City", value="https://dodi-repacks.site/index.php/2020/06/03/638-grand-theft-auto-vice-city-10-year-anniversary-pc-edition-v1-0-multi5-dodi-repack/")
        embed.add_field(name="GTA 3", value="https://dodi-repacks.site/index.php/2020/06/02/637-grand-theft-auto-iii-10-year-anniversary-hd-edition-v1-1-multi6-dodi-repack/")
        embed.add_field(name="GTA San Andreas", value="https://dodi-repacks.site/index.php/2020/05/26/632-grand-theft-auto-san-andreas-v1-0-0-22-multi5-dodi-repack/")
        embed.add_field(name="GTA 2", value="https://dodi-repacks.site/index.php/2020/06/04/639-grand-theft-auto-ii-v9-6-multi2-dodi-repack/")
        embed.add_field(name="GTA 1", value="https://dodi-repacks.site/index.php/2020/06/04/640-grand-theft-auto-v1-0-0-1-multi4-dodi-repack/")
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
    if message.content == "!repacks-farcry":
        embed = discord.Embed(title="Here are some Far Cry Games Repacks", description="Remember to use a torrent client")
        embed.add_field(name="Far Cry Primal", value=" https://fitgirl-repacks.site/far-cry-primal-apex-edition-v1-3-3-dlcs-ultra-hd-textures/")
        embed.add_field(name="Far Cry 5", value=" https://fitgirl-repacks.site/far-cry-5/")
        embed.add_field(name="Far Cry 3+Blood Dragon", value=" https://fitgirl-repacks.site/far-cry-3-duology/")
        embed.add_field(name="Far Cry New Dawn", value=" https://fitgirl-repacks.site/far-cry-new-dawn/")
        embed.add_field(name="Far Cry 4", value=" https://fitgirl-repacks.site/far-cry-4-gold-edition/")
        embed.add_field(name="Far Cry 1", value="https://dodi-repacks.site/index.php/2019/06/14/382-far-cry-dodi-repack/")
        embed.add_field(name="Far Cry 2 - Fortune's Edition", value='https://dodi-repacks.site/index.php/2019/01/09/242-far-cry-2-fortunes-edition-v-1-3-all-dlcs-multi5-from-2-gb-dodi-repack/')
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-watchdogs":
        embed = discord.Embed(title="Here are some Watch dogs Games Repacks", description="remember to use a torrent client")
        embed.add_field(name="Watch_dogs1", value=" https://fitgirl-repacks.site/watch-dogs-v1-06-329-all-dlcs/")
        embed.add_field(name="Watch_Dogs2", value=" https://fitgirl-repacks.site/watch-dogs-2-gold-edition/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-nfs":
        embed = discord.Embed(title="Here are some need for speed games repacks", description="Remember to use a torrent client")
        embed.add_field(name="Need For Speed Payback", value="https://fitgirl-repacks.site/need-for-speed-payback-deluxe-edition/")
        embed.add_field(name="Need For Speed Hot Pursuit", value="https://fitgirl-repacks.site/need-speed-hot-pursuit-v1-0-5-0s-dlcs/")
        embed.add_field(name="Need For Speed Most Wanted 2012", value="https://fitgirl-repacks.site/need-speed-wanted-limited-edition-v-1-5-0-0-dlcs/")
        embed.add_field(name="Need For Speed Heat", value="https://dodi-repacks.site/index.php/2019/12/27/503-need-for-speed-heat-deluxe-edition-dodi-repack/")
        embed.add_field(name="Need For Speed: The Run", value="https://dodi-repacks.site/index.php/2019/07/03/399-need-for-speed-the-run-limited-editiondlc-multi11-dodi-repack-from-4-2-gb/")
        embed.add_field(name="Need For Speed Rivals", value="https://dodi-repacks.site/index.php/2019/07/03/398-need-for-speed-rivals-complete-edition-v1-4-0-0-dodi-repack/")
        embed.add_field(name="Need For Speed Most Wanted 2005: Black Edition", value="https://dodi-repacks.site/index.php/2018/10/02/123-need-for-speed-most-wanted-black-edition-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-splintercell":
        embed = discord.Embed(title="Here are some Splinter Cell games repacks", description="Remember to use torrent client")
        embed.add_field(name="Tom Clancy's Splinter Cell Blacklist", value="https://fitgirl-repacks.site/tom-clancys-splinter-cell-blacklist-digital-deluxe-edition-v1-03-2-dlcs/")   
        embed.add_field(name="Tom Clancy's Splinter Cell Conviction", value="https://dodi-repacks.site/index.php/2020/04/11/264-tom-clancys-splinter-cell-conviction-deluxe-edition-v1-4-insurgency-pack-dodi-repack/")
        embed.add_field(name="Tom Clancy's Splinter Cell Double Agent", value="https://dodi-repacks.site/index.php/2020/04/11/588-tom-clancys-splinter-cell-double-agent-v1-02a-multi5-dodi-repack/")    
        embed.add_field(name="Tom Clancy's Splinter Cell Pandora Tomorrow", value="https://dodi-repacks.site/index.php/2020/04/10/587-tom-clancys-splinter-cell-pandora-tomorrow-v1-31-hd-texture-widescreenfix-dodi-repack/")
        embed.add_field(name="Tom Clancy's Splinter Cell Chaos Theory", value="https://dodi-repacks.site/index.php/2020/04/07/584-tom-clancys-splinter-cell-chaos-theory-v1-05-157-multi5-dodi-repack/")
        embed.add_field(name="Tom Clancy's Spinter Cell", value="https://dodi-repacks.site/index.php/2020/03/27/574-tom-clancys-splinter-cell-v1-3-dlc-hd-wide-fix-multi6-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-amongus":
        embed = discord.Embed(title="Download link for Among US", description="You need a new gmail account for this")
        embed.add_field(name="Among US", value="https://masquerade.site/among-us/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-masseffect":
        embed = discord.Embed(title="Here's the Mass Effect Collection repacks", description="Use a torrent client to download")
        embed.add_field(name="Mass Effect 1", value="https://fitgirl-repacks.site/mass-effect/")
        embed.add_field(name="Mass Effect 2", value="https://fitgirl-repacks.site/mass-effect-2/")
        embed.add_field(name="Mass Effect 3", value="https://fitgirl-repacks.site/mass-effect-3/")
        embed.add_field(name="Mass Effect: Andromeda", value="https://fitgirl-repacks.site/mass-effect-andromeda-super-deluxe-edition/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-starwars":
        embed = discord.Embed(title="Here's the Star Wars Collection repacks", description="Use a torrent client to download")
        embed.add_field(name="Star Wars: Jedi Fallen Order", value="https://fitgirl-repacks.site/star-wars-jedi-fallen-order/")
        embed.add_field(name="Star Wars: Battlefront 2", value="https://fitgirl-repacks.site/star-wars-battlefront-ii/")
        embed.add_field(name="Lego Star Wars: Force Awakens", value="https://fitgirl-repacks.site/lego-star-wars-force-awakens-v1-03-build-1-0-0-33084-12-dlcs/")
        embed.add_field(name="Star Wars: Battlefront 2(Classic)", value="https://dodi-repacks.site/index.php/2020/07/29/709-star-wars-battlefront-2-classic-2005-multi5-dodi-repack/")
        embed.add_field(name="Star Wars: Battlefront(Classic)", value="https://dodi-repacks.site/index.php/2020/07/29/708-star-wars-battlefront-classic-2004-dodi-repack/")
        embed.add_field(name="Star Wars: Republic Commando", value="https://dodi-repacks.site/index.php/2020/07/29/star-wars-republic-commando-dodi-repack/")
        embed.add_field(name="Star Wars: Knights Of The Old Republic", value="https://dodi-repacks.site/index.php/2020/07/25/star-wars-knights-of-the-old-republic-collection-dodi-repacks/")
        embed.add_field(name="Star Wars: Jedi Knight II", value="https://dodi-repacks.site/index.php/2020/07/14/685-star-wars-jedi-knight-ii-jedi-outcast-dodi-repack/")
        embed.add_field(name="Star Wars: Jedi Knight: Dark Forces II", value="https://dodi-repacks.site/index.php/2020/07/14/682-star-wars-jedi-knight-dark-forces-ii-dodi-repack/")
        embed.add_field(name="Star Wars: The Force Unleashed", value="https://dodi-repacks.site/index.php/2020/07/07/star-wars-the-force-unleashed-collection-gog-multi7-dodi-repacks/")
        embed.add_field(name="Star Wars: The Force Unleashed II", value="https://dodi-repacks.site/index.php/2020/07/06/673-star-wars-the-force-unleashed-ii-gog-multi7-from-3-5-gb-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...
    
    ...
    if message.content == "!repacks-lego":
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
    if message.content == "!repacks-marvel":
        embed = discord.Embed(title="Here's the Marvel Collection", description="Use a torrent client to download")
        embed.add_field(name="Marvel vs Capcom: Infinite", value="https://fitgirl-repacks.site/marvel-vs-capcom-infinite/")
        embed.add_field(name="Marvel's Guardians Of The Galaxy: Telltale Edition", value="https://fitgirl-repacks.site/marvels-guardians-of-the-galaxy-the-telltale-series-complete-season/")
        embed.add_field(name="Ultimate Marvel Vs Capcom 3", value="https://fitgirl-repacks.site/ultimate-marvel-vs-capcom-3/")
        embed.add_field(name="Marvel's Ultimate Alliance", value="https://fitgirl-repacks.site/marvel-ultimate-alliance-bundle-1-2/")
        await message.channel.send(content=None, embed=embed)
    ...
    
    ...
    if message.content == "!repacks-ghostrecon":
        embed = discord.Embed(title="Here's the Ghost Recon Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Tom Clancy's Ghost Recon Wildlands", value="https://fitgirl-repacks.site/tom-clancys-ghost-recon-wildlands/")
        embed.add_field(name="Tom Clancy's Ghost Recon Future Soldier ", value="https://dodi-repacks.site/index.php/2019/04/20/333-tom-clancys-ghost-recon-future-soldier-complete-edition-v1-8-all-dlcs-multi12-dodi-repack-from-7-9-gb/")
        await message.channel.send(content=None, embed=embed)
    ...
client.run('token')