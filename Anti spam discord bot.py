#This code is originally from youtube but it was bugged, so i fixed it!
from discord import Intents
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix="?",intents=Intents. all())
@client.event
async def on_ready():
    print("Online")
    while True:
        print("cleared")
        await asyncio.sleep(10)
        with open("spam_detect.txt", "r+") as file:
            file.truncate(0)

@client.event
async def on_message(message):
    counter = 0
    with open("spam_detect.txt", "r+") as file:
        for lines in file:
            if lines.strip("\n") == str(message.author.id):
                counter+=1
    
        file.writelines(f"{str(message.author.id)}\n")
        if counter > 2:
            await message.guild.ban(message.author, reason = "spam")
            await asyncio.sleep(10)
            await message.guild.unban(message.author)
            print("Banned!")
    
client.run("Token is here")

