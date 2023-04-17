import os
import sys
try: 
  os.system("pip --version")
except:
  print("PIP IS NOT INSTALLED, PLEASE INSTALL PIP BEFORE PROCEEDING")
l = ['discord','openai','DiscordUtils']
for i in l:
  os.system('pip install ',i)
