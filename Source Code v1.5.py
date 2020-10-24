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
        embed.add_field(name="Version", value="1.5")
        embed.add_field(name="Source Code", value="https://github.com/HeliumSpectrum/Pirate-Navigator-Source-Code")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!games":
        embed = discord.Embed(title="Here are some games collections", description="Pick your choice!")
        embed.add_field(name="Repacks", value="!repacks")
        embed.add_field(name="Direct Download Links(Work in progress)", value="!ddl")
        embed.add_field(name="Important Software(Work in progress)", value="!soft")
        embed.add_field(name="Pirate Handbook", value="!handbook")
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
        embed.add_field(name="Assassin's Creed", value="https://dodi-repacks.site/index.php/2019/05/08/345-assassins-creed-directors-cut-edition-build-252091-multi5-dodi-repack-from-1-6-gb/")
        embed.add_field(name="Assassin's Creed 2", value="https://dodi-repacks.site/index.php/2019/05/09/346-assassins-creed-2-deluxe-editionmulti12-dodi-repack-from-2-2-gb/")
        embed.add_field(name="Assassin's Creed Revelations", value="https://dodi-repacks.site/index.php/2019/05/10/347-assassins-creed-revelations-gold-edition-all-dlcs-multi15-dodi-repack-from-3-2-gb/")
        embed.add_field(name="Assassin's Creed Brotherhood", value="https://dodi-repacks.site/index.php/2019/05/09/346-assassins-creed-brotherhood-digital-deluxe-edition-multi14-dodi-repack-from-2-5-gb/ ")
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
        embed.add_field(name="Mafia Repack Collection", value="!repacks-mafia")
        embed.add_field(name="Doom Repack Collection", value="!repacks-doom")
        embed.add_field(name="Spiderman Repack Collection", value="!repacks-spiderman")
        embed.add_field(name="Battlefield Repack Collection", value="!repacks-battlefield")
        embed.add_field(name="Call Of Duty Repack Collection", value="!repacks-cod")
        embed.add_field(name="Call Of Juarez Repack Collection", value="!repacks-callofjuarez")
        embed.add_field(name="Batman Repack Collection", value="!repacks-batman")
        embed.add_field(name="Bioshock Repack Collection", value="!repacks-bioshock")
        embed.add_field(name="Borderlands Repack Collection", value="!repacks-borderlands")
        embed.add_field(name="Deadspace Repack Collection", value="!repacks-deadspace")
        embed.add_field(name="Crysis Repack Collection", value="!repacks-crysis")
        embed.add_field(name="More Repacks", value="repacks-2")
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
        embed.add_field(name="Marvel's Avengers", value="https://dodi-repacks.site/index.php/2020/10/19/814-marvels-avengers-deluxe-edition-v1-3-3-build-13-38-dlcs-ultra-texture-pack-multi15-from-60-gb-fast-install-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...
    
    ...
    if message.content == "!repacks-ghostrecon":
        embed = discord.Embed(title="Here's the Ghost Recon Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Tom Clancy's Ghost Recon Wildlands", value="https://fitgirl-repacks.site/tom-clancys-ghost-recon-wildlands/")
        embed.add_field(name="Tom Clancy's Ghost Recon Future Soldier ", value="https://dodi-repacks.site/index.php/2019/04/20/333-tom-clancys-ghost-recon-future-soldier-complete-edition-v1-8-all-dlcs-multi12-dodi-repack-from-7-9-gb/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-mafia":
        embed = discord.Embed(title="Here are some Mafia Repacks Collection", description="Remember to use a torrent client")
        embed.add_field(name="Mafia: Definitive Edition", value="https://fitgirl-repacks.site/mafia-definitive-edition-v1-0-1-chicago-outfit-pack-dlc-windows-7-fix/")
        embed.add_field(name="Mafia 2", value="https://fitgirl-repacks.site/mafia-2-digital-deluxe-edition-v-1-0-0-1/")
        embed.add_field(name="Mafia 3", value="https://fitgirl-repacks.site/mafia-3-digital-deluxe-edition/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-doom":
        embed = discord.Embed(title="Here's the Doom Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Doom 3: BFG Edition", value="https://dodi-repacks.site/index.php/2020/06/30/667-doom-3-bfg-edition-v20191007-dlcs-multi6-dodi-repack/")
        embed.add_field(name="Doom 64 ", value="https://fitgirl-repacks.site/doom-64/")
        embed.add_field(name="Doom 1&2", value="https://fitgirl-repacks.site/doom-doom-2-classic-bundle/")
        embed.add_field(name="Doom 2016", value="https://fitgirl-repacks.site/doom/")
        embed.add_field(name="Doom Eternal", value="https://fitgirl-repacks.site/doom-eternal/")
        await message.channel.send(content=None, embed=embed)
    ...
    
    ...
    if message.content == "!repacks-spiderman":
        embed = discord.Embed(title="Here's the Spiderman Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Spiderman: Shattered Dimensions", value="https://fitgirl-repacks.site/spider-man-shattered-dimensions/")
        embed.add_field(name="The Amazing Spiderman ", value="https://dodi-repacks.site/index.php/2020/04/29/611-the-amazing-spider-man-update1-all-dlcs-fixes-multi6-dodi-repack/")
        embed.add_field(name="The Amazing Spiderman 2", value="https://dodi-repacks.site/index.php/2020/04/29/612-the-amazing-spider-man-2-bundle-all-dlcs-multi6-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-battlefield":
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
    if message.content == "!repacks-cod":
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
    if message.content == "!repacks-callofjuarez":
        embed = discord.Embed(title="Here's the Call Of Juarez Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Call Of Juarez: Bound In Blood", value="https://dodi-repacks.site/index.php/2019/12/04/489-call-of-juarez-bound-in-blood-v1-1-0-0-dodi-repack/")
        embed.add_field(name="Call Of Juarez: Gunslinger", value="https://dodi-repacks.site/index.php/2019/11/27/486-call-of-juarez-gunslinger-update-v1-05-dlcs-multi9-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-batman":
        embed = discord.Embed(title="Here's the Batman Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Batman Arkham Knight", value="https://dodi-repacks.site/index.php/2019/04/30/339-batman-arkham-knight-premium-edition-v1-6-2-0-all-dlcs-multi10-dodi-repack-from-28-gb/")
        embed.add_field(name="Batman Arkham Origins", value="https://dodi-repacks.site/index.php/2019/04/28/338-batman-arkham-origins-complete-edition-dodi-repack/")
        embed.add_field(name="Batman Arkham City", value="https://dodi-repacks.site/index.php/2019/04/28/337-batman-arkham-city-complete-edition-dodi-repack/")
        embed.add_field(name="Batman Arkham Asylum", value="https://dodi-repacks.site/index.php/2019/04/25/336-batman-arkham-asylum-game-of-the-year-edition-dodi-repack/")
        embed.add_field(name="Batman The Enemy Within", value="https://dodi-repacks.site/index.php/2018/10/23/152-batman-the-enemy-within-complete-season-multi9-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-bioshock":
        embed = discord.Embed(title="Here's the Bioshock Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Bioshock Remastered", value="https://dodi-repacks.site/index.php/2020/07/31/712-bioshock-remastered-v1-0-122872-multi6-from-4-7-gb-dodi-repack/")
        embed.add_field(name="Bioshock 2 Remastered", value="https://dodi-repacks.site/index.php/2020/07/31/713-bioshock-2-remastered-v1-0-122864-dlcs-multi7-from-6-7-gb-dodi-repack/")
        embed.add_field(name="Bioshock Infinite", value="https://dodi-repacks.site/index.php/2020/07/31/711-bioshock-infinite-the-complete-edition-multi11-from-12-5-gb-dodi-repack/" )
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-borderlands":
        embed = discord.Embed(title="Here's the Borderlands Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Borderlands: Game Of The Year Edition", value="https://dodi-repacks.site/index.php/2018/12/23/225-borderlands-game-of-the-year-edition-v1-5-0-all-dlcs-multi5-dodi-repack/")
        embed.add_field(name="Borderlands 2", value="https://dodi-repacks.site/index.php/2018/12/23/226-borderlands-2-v1-8-3-dlcs-multi8-dodi-repack/")
        embed.add_field(name="Borderlands 3", value="https://dodi-repacks.site/index.php/2020/10/04/782-borderlands-3-super-deluxe-edition-build-5382210-all-dlcs-multi11-fast-install-from-77-7-gb-dodi-repack/" )
        await message.channel.send(content=None, embed=embed)
    ...
    
    ...
    if message.content == "!repacks-deadspace":
        embed = discord.Embed(title="Here's the Deadspace Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Deadspace", value="https://dodi-repacks.site/index.php/2019/01/10/243-dead-space-multi11-dodi-repack-from-2-9-gb/")
        embed.add_field(name="Deadspace 2", value="https://dodi-repacks.site/index.php/2019/01/10/244-dead-space-2-multi11-dodi-repack-from-4-9-gb/")
        embed.add_field(name="Deadspace 3", value="https://dodi-repacks.site/index.php/2019/01/10/245-dead-space-3-v1-0-0-1-awakened-dlc-multi11-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-crysis":
        embed = discord.Embed(title="Here's the Crysis Repack Collection", description="Use a torrent client to download")
        embed.add_field(name="Crysis", value="https://dodi-repacks.site/index.php/2019/03/04/290-crysis-v1-1-1-6156-multi11-dodi-repack-from-3-4-gb/")
        embed.add_field(name="Crysis 2: Maximum Edition", value="https://dodi-repacks.site/index.php/2019/03/05/292-crysis-2-maximum-edition-v1-9-multi11-dodi-repack-from-4-8-gb/")
        embed.add_field(name="Crysis 3", value="https://dodi-repacks.site/index.php/2019/03/05/293-crysis-3-digital-deluxe-edition-v-1-3-bonus-multi10-dodi-repack-from-8-4-gb/")
        embed.add_field(name="Crysis Warhead", value="https://dodi-repacks.site/index.php/2019/03/04/291-crysis-warhead-v1-1-1-711-multi11-dodi-repack-from-3-3-gb/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-2":
        embed = discord.Embed(title="Here's some more Repack Collection", description="Pick your choice!")
        embed.add_field(name="Fallout Repack Collection", value="!repacks-fallout")
        embed.add_field(name="Forza Repack Collection", value="!repacks-forza")
        embed.add_field(name="Mortal Combat Repack Collection", value="!repacks-mortalkombat" )
        embed.add_field(name="Witcher Repack Collection", value="!repacks-witcher")
        embed.add_field(name="Red Dead Redemption 2 Repack", value="!repacks-rdr2")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-fallout":
        embed = discord.Embed(title="Here's some Fallout Repack Collection", description="Pick your choice")
        embed.add_field(name="Fallout 3", value="https://masquerade.site/fallout-3-game-of-the-year-edition/")
        embed.add_field(name="Fallout New Vegas", value="https://masquerade.site/fallout-new-vegas-ultimate-edition/")
        embed.add_field(name="Fallout 4", value="https://fitgirl-repacks.site/fallout-4/" )
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-forza":
        embed = discord.Embed(title="Here's some Forza Repack Collection", description="Remember to use a torrent client")
        embed.add_field(name="Forza Horizon 4", value="https://dodi-repacks.site/index.php/2020/09/03/429-forza-horizon-4-ultimate-edition-v1-332-904-2-all-expansions-missing-dlc-multi16-dodi-repack-from-44-3-gb/")
        embed.add_field(name="Forza Horizon 3", value="https://dodi-repacks.site/index.php/2019/06/10/379-forza-horizon-3-v1-0-119-1002-44-dlcs-multi13-dodi-repack/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-mortalkombat":
        embed = discord.Embed(title="Here's some Mortal Kombat Repack Collection", description="Remember to use a torrent client")
        embed.add_field(name="Mortal Kombat 11", value="https://fitgirl-repacks.site/mortal-kombat-11/")
        embed.add_field(name="Mortal Kombat XL", value="https://fitgirl-repacks.site/mortal-kombat-xl/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!repacks-witcher":
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
        embed.add_field(name="Assassin's Creed DDL Collection", value="ddl-ac")
        embed.add_field(name="Red Dead Redemption 2 DDL ", value="ddl-rdr2")
        embed.add_field(name="Mass Effect DDL Collection", value="ddl-masseffect")
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
    if message.content == "!repacks-rdr2":
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
    


client.run('token')