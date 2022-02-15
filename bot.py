import discord
from discord.ext import commands, tasks
import random
from riotwatcher import LolWatcher, ApiError
import pandas as pd
import csv
import time
import sys

#VARIABLES
api_key = 'INSERT API KEY HERE' # here please put in-between the quotes your Riot API Developer Key
watcher = LolWatcher(api_key)
my_region = 'euw1'
region = 'europe'
current_time = int(time.time())
last = (current_time - 86400)
week = (current_time - 604800)
two = (current_time - 172800)
print(current_time)
print(last)

#PUUIDS ----------------------------------
top_id = 'fQwRacUndeCleiOeQi4qm4WTFuoqSZg7SXnQWeAepWZPZ6teQ7Aytl5wAoAG3ltsM_ZcNT904BbIUg' # here write the puuid of your toplaner
jgl_id = 'Kae9k0d4l2o6sKblB36Pm-IuPjgDNFLu2Vz0ODNcOG2PaNVXRWL27j82I7-UKGCwDgifz82RrT6zQA' # here write the puuid of your jungler
mid_id = '4B_9lFf5JU4onY__sQyZY6RVVNrXnsCsX6vqYgjWKjlFqnGj4Vb0gxCa0mUMWU8uK_6NM-IeqaB_ag' # here write the puuid of your midlaner
adc_id = 'eCze5I2zMSyG4x84qyVrlbJjQOdyr6cn6IPah6AOjpZA7x6LBm4EtdMUJzjR8EAZBazCsGqSy7-oTw' # here write the puuid of your ad carry
sup_id = 'IQYpa2gn6ocPcdte-LHXNk8VTVSrcFY6EzfJqux4Nw33wonDXugp6bChZm3bY5-hC2d-2g_17HfMGg' # here write the puuid of your support
oplon = [top_id, jgl_id, mid_id, adc_id, sup_id]

#CALCULS ----------------------------------
player_name = ['Toplaner', 'Jungler', 'Midlaner', 'ADCarry', 'Support']
game_nbrs = []

# DAY COMMAND ----------------------------------
if sys.argv[1] == "day":
    topmh = list(watcher.match.matchlist_by_puuid(region, top_id, type="ranked", start_time=last, end_time=current_time, count=100))
    jglmh = list(watcher.match.matchlist_by_puuid(region, jgl_id, type="ranked", start_time=last, end_time=current_time, count=100))
    midmh = list(watcher.match.matchlist_by_puuid(region, mid_id, type="ranked", start_time=last, end_time=current_time, count=100))
    adcmh = list(watcher.match.matchlist_by_puuid(region, adc_id, type="ranked", start_time=last, end_time=current_time, count=100))
    supmh = list(watcher.match.matchlist_by_puuid(region, sup_id, type="ranked", start_time=last, end_time=current_time, count=100))

# WEEK COMMAND ----------------------------------
if sys.argv[1] == "week":
    topmh = list(watcher.match.matchlist_by_puuid(region, top_id, type="ranked", start_time=week, end_time=current_time, count=100))
    jglmh = list(watcher.match.matchlist_by_puuid(region, jgl_id, type="ranked", start_time=week, end_time=current_time, count=100))
    midmh = list(watcher.match.matchlist_by_puuid(region, mid_id, type="ranked", start_time=week, end_time=current_time, count=100))
    adcmh = list(watcher.match.matchlist_by_puuid(region, adc_id, type="ranked", start_time=week, end_time=current_time, count=100))
    supmh = list(watcher.match.matchlist_by_puuid(region, sup_id, type="ranked", start_time=week, end_time=current_time, count=100))

#LAST TWO DAYS COMMAND ----------------------------------
if sys.argv[1] == "two":
    topmh = list(watcher.match.matchlist_by_puuid(region, top_id, type="ranked", start_time=two, end_time=current_time, count=100))
    jglmh = list(watcher.match.matchlist_by_puuid(region, jgl_id, type="ranked", start_time=two, end_time=current_time, count=100))
    midmh = list(watcher.match.matchlist_by_puuid(region, mid_id, type="ranked", start_time=two, end_time=current_time, count=100))
    adcmh = list(watcher.match.matchlist_by_puuid(region, adc_id, type="ranked", start_time=two, end_time=current_time, count=100))
    supmh = list(watcher.match.matchlist_by_puuid(region, sup_id, type="ranked", start_time=two, end_time=current_time, count=100))

# API DATAFRAME CREATION ----------------------------------
game_nbrs.append(len(topmh))
game_nbrs.append(len(jglmh))
game_nbrs.append(len(midmh))
game_nbrs.append(len(adcmh))
game_nbrs.append(len(supmh))

df = pd.DataFrame(
    {'Player': player_name,
    'phrase': "has played",
    'Games': game_nbrs,
    'last': "games of soloQ in the last 24 hours.",
})

print(df)

i = 0
df1 = df.loc[[i]]


#DISCORD BOT COMMANDS ----------------------------------
bot = commands.Bot(command_prefix = "!", description = "SoloQ Bot")

@bot.event
async def on_ready():
	print("Your soloQ bot is ready for use !")

@bot.command()
async def soloQ(ctx):
    for i in range(5):
        df1 = df.loc[[i]]
        await ctx.send(df1.to_string(header=False, index=False))
        i = i + 1

bot.run("INSERT DISCORD BOT TOKEN HERE")