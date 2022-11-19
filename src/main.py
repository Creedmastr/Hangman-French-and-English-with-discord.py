import random
import discord
from discord.ext import commands
from protected.disToken import tokenn
import os
import unicodedata


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=";", intents=intents)
isGameRunning = False
foundedChar = 0


@bot.event
async def on_ready():
    print(u"Rédi")

@bot.command()
async def hangman(ctx, arg):
    if arg == "en":
        await ctx.send("You started a hangman game.")
        global wordlist
        global secretWord
        global letter
        global life
        global foundedChar
        global isGameRunning
        global foundedChar

        if arg == "fr":
            os.getcwd()
            f1 = open(u"./wordlist_fr", "r")
            wordlist = f1.readlines()
        if arg == None or arg == "en":
            f1 = open(u"./wordlist_en", "r")
            wordlist = f1.readlines()
        
        secretWord = random.choice(wordlist)
        secretWord = secretWord.lower()
        unicodedata.normalize("NFD", secretWord).encode('ascii', 'ignore')
            
        letter = list(secretWord)
        life = 8
        
        foundedChar = 0
        foundedLetters = u""
                
        while foundedChar < len(letter):
            await ctx.send(u"Please try a letter")
            def check(m):
                return ctx.author == m.author #To make sure it is the only message author is getting
            msge = await bot.wait_for('message', timeout=60.0, check=check) #Message hatched after the command, probably the character typed after the command
            msg = msge.content.lower()
            
            if len(list(str(msg))) >= 2 and str(msg).count(" ") == 0: #If it is a word in the message after the command, test it
                if msg == secretWord:
                    await ctx.send(u"Hurray, you founded a word !")
                    
                elif not msg == secretWord: 
                    
                    await ctx.send(u"Thats not it...")
                    
                    await ctx.send("You have {life} lives left".format(life=str(life)))
                    if life == 0:
                        ctx.send("You doesn't have lives anymore...")
                        break
            else: #If it is really a character
                if msg in letter:
                    await ctx.send("Hurray, that's a letter !")
                    foundedLetters = foundedLetters + str(msg)
                    await ctx.send("You have founded the letters: " + foundedLetters + ".")
                    foundedChar = foundedChar + 1
                elif not msg in letter:
                    await ctx.send("Thats not it sorry...")
                    life = life - 1
                    await ctx.send("You have {life} lives left".format(life=str(life)))
                    if life == 0:
                        await ctx.send("You doesn't have lives anymore...")
                        break         
        
        await ctx.send("You founded all the letters ! The word is : " + str(letter).replace("[", "").replace("]", '').replace("'", '') + "!")
    else:
        await ctx.send("Vous avez commencé un pendu")
        global wordlist
        global secretWord
        global letter
        global life
        global foundedChar
        global isGameRunning
        global foundedChar

        if arg == "fr":
            os.getcwd()
            f1 = open(u"./wordlist_fr", "r")
            wordlist = f1.readlines()
        if arg == None or arg == "en":
            f1 = open(u"./wordlist_en", "r")
            wordlist = f1.readlines()
        
        secretWord = random.choice(wordlist)
        secretWord = secretWord.lower()
        unicodedata.normalize("NFD", secretWord).encode('ascii', 'ignore')
            
        print(secretWord)
        letter = list(secretWord)
        life = 8
        
        foundedChar = 0
        foundedLetters = u""
                
        while foundedChar < len(letter):
            await ctx.send(u"Essayer une lettre")
            def check(m):
                return ctx.author == m.author #To make sure it is the only message author is getting
            msge = await bot.wait_for('message', timeout=60.0, check=check) #Message hatched after the command, probably the character typed after the command
            msg = msge.content.lower()
            
            if len(list(str(msg))) >= 2 and str(msg).count(" ") == 0: #If it is a word in the message after the command, test it
                if msg == secretWord:
                    await ctx.send(u"Incroyable, vous avez trouvé le mot !")
                    
                elif not msg == secretWord: 
                    
                    await ctx.send(u"Ce n'est pas ça...")
                    
                    await ctx.send("Vous avez {life} vies restantes.".format(life=str(life)))
                    if life == 0:
                        ctx.send("Vous n'avez plus de vie...")
                        break
            else: #If it is really a character
                if msg in letter:
                    await ctx.send("C'est une lêttre du mot !")
                    foundedLetters = foundedLetters + str(msg)
                    await ctx.send("Vous avez trouvé les lettres: " + foundedLetters + ".")
                    foundedChar = foundedChar + 1
                elif not msg in letter:
                    await ctx.send("Ce n'est pas ça, désolé...")
                    life = life - 1
                    await ctx.send("Vous avez {life} vies restantes.".format(life=str(life)))
                    if life == 0:
                        await ctx.send("Vous n'avez plus de vie...")
                        break         
        
        await ctx.send("Vous avez trouvé toutes les lettres, les voici : " + str(letter).replace("[", "").replace("]", '').replace("'", '') + "!")
bot.run(tokenn)