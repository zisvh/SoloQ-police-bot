import discord
from discord.ext import commands, tasks
import random
from riotwatcher import LolWatcher, ApiError
import pandas as pd
import csv
import time
import sys

#VARIABLES
api_key = 'key1' # here please put in-between the quotes your Riot API Developer Key
watcher = LolWatcher(api_key)

current_time = int(time.time())
last = (current_time - 86400)
week = (current_time - 604800)
two = (current_time - 172800)
teamArr = []

def regionSelectorSmallBig(regionInput):
    print("we are in region selector")
    if "eu" in regionInput:
        regionInput = "europe"
    if "na" in regionInput:
        regionInput = "americas"
    if "as" in regionInput:
        regionInput = "asia"

    print("Returning: " + str(regionInput))
    return regionInput

def getSummonerByRegionName(region, name):
    return watcher.summoner.by_name(region, name)

def getPuuidBySummonerInternal(summoner):
    return summoner['puuid']

def getNameBySummonerInternal(summoner):
    return summoner['name']

def getMatchListByRegionAndIdAndTimeFrame(region, puuId, startTime):

    return list(watcher.match.matchlist_by_puuid(region, puuId, type="ranked", start_time=startTime, end_time=current_time, count=100))

def getTimeByStringInternal(input):
    if input == "1":
        return last

    if input == "2":
        return two

    if input == "week":
        return week

def getTimeStringFromInput(input):
    if input == "1":
        return "the last day"

    if input == "2":
        return "the last two days"

    if input == "week":
        return "the last week"

def addPlayerToTeamInternal(region, name):
    playervalues = createPlayerKeyInternal(region,name)
    
    if playervalues not in teamArr:
        teamArr.append(playervalues)
        return True
    return False

def removePlayerFromTeamInternal(region, name):
    playervalues = createPlayerKeyInternal(region,name)
    
    if playervalues in teamArr:
        teamArr.remove(playervalues)
        return True
    return False

def listTeamInternal():
    returnValue = "Players in Team:"
    if len(teamArr) > 0:
        for player in teamArr:
            sliced = slicePlayerKey(player)
            returnValue = returnValue + "\n"
            returnValue = returnValue + "" + sliced[0] + " | " + sliced[1]
    else:
        print("team was 0")
    
    print("Returning from list team: \n" + returnValue)
    return returnValue

def slicePlayerKey(playerKey):
    index = playerKey.find(",,--")
    region = playerKey[:index]
    name = playerKey[index+4:len(playerKey)]
    return (region, name)


def createPlayerKeyInternal(region, name):
    return region + ",,--" + name

#DISCORD BOT COMMANDS ----------------------------------
bot = commands.Bot(command_prefix = "!", description = "SoloQ Bot")

@bot.event
async def on_ready():
	print("Your soloQ bot is ready for use !")

@bot.command(name="gp")
async def getPlayer(ctx,arg1,arg2):
    try: 
        region = arg1
        playerName = arg2
        await ctx.send(getSummonerByRegionName(region, playerName))
    except Exception as e:
        print(str(e))
        await ctx.send("Error: ")
        await ctx.send(str(e))

@bot.command(name="mc")
async def getPlayerMatchCount(ctx,arg1,arg2,arg3):
    try:
        region = arg1
        playerName = arg2
        timeframe = arg3
        print(arg1 + arg2 + arg3)
        summoner = getSummonerByRegionName(region, playerName)
        print(summoner)
        print(region)
        name = getNameBySummonerInternal(summoner)
        puuId = getPuuidBySummonerInternal(summoner)
        timestring = getTimeStringFromInput(timeframe)

        timeframe = getTimeByStringInternal(timeframe)
        #use the region selector for correct api. very simple..
        region = regionSelectorSmallBig(region)
        matchlist = getMatchListByRegionAndIdAndTimeFrame(region,puuId, timeframe)

        await ctx.send(name + " has played " + str(len(matchlist)) + "games " + timestring)
    except Exception as e:
        print(str(e))
        await ctx.send("Error: ")
        await ctx.send(str(e))

@bot.command(name="police")
async def teamCheckup(ctx, timeframe):
    try:
        returnValue = ""
        timestring = getTimeStringFromInput(timeframe)
        timeframe = getTimeByStringInternal(timeframe)
        for playerKey in teamArr:

            sliced = slicePlayerKey(playerKey)
            summoner = getSummonerByRegionName(sliced[0], sliced[1])
            puuId = getPuuidBySummonerInternal(summoner)
            mlRegion = regionSelectorSmallBig(sliced[0])
            matchlist = getMatchListByRegionAndIdAndTimeFrame(mlRegion,puuId,timeframe)

            returnValue = returnValue + "\n"
            returnValue = returnValue + "Player: " + sliced[0] + " | " + sliced[1] + " has played " + str(len(matchlist)) + "games " + timestring
        await ctx.send(returnValue)
    except Exception as e:
        print(str(e))
        await ctx.send("Error: ")
        await ctx.send(str(e))
        

@bot.command(name="lt")
async def listTeam(ctx):
    try:
        await ctx.send(listTeamInternal())
    except Exception as e:
        print(str(e))
        await ctx.send("Error: ")
        await ctx.send(str(e))


@bot.command(name="add")
async def addPlayer(ctx,arg1,arg2):
    try: 
        region = arg1
        name = arg2
        addPlayerToTeamInternal(region, name)
        await ctx.send("Player added to team")

    except Exception as e:
        print(str(e))
        await ctx.send("Error: ")
        await ctx.send(str(e))

@bot.command(name="rm")
async def removePlayerFromTeam(ctx, arg1, arg2):
    try:
        region = arg1
        name = arg2
        removePlayerFromTeamInternal(region, name)
        await ctx.send("Player Removed")
    except Exception as e:
        print(str(e))
        await ctx.send("Error: ")
        await ctx.send(str(e))



bot.run("key2") # here paste in-between double quotes your discord bot token