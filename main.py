import discord
from discord.ext import commands
import openai
import DiscordUtils

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('openai')

completion = openai.Completion()

def Reply(question):
  prompt = f'You: {question}\n Harleon: '
  response = completion.create(prompt=prompt,
                               engine="text-davinci-003", 
                               stop=['\You'],
                               max_tokens=200)
  answer = response.choices[0].text.strip()
  return answer

client = commands.Bot(command_prefix="?", intents=discord.Intents.all())
STATUS = "?l for your fantasies"
@client.event
async def on_ready():
    await client.tree.sync() 
    await client.change_presence(status=discord.Status.idle,activity=discord.Game(STATUS))
    print("Harleon has been connected")
    
@client.tree.command(name="slasher", description="nothing much, go do something else")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Bruh")

@client.command()
async def l(ctx, *, question):
   await ctx.send(Reply(question))
        
client.run(os.getenv('TOKEN'))
