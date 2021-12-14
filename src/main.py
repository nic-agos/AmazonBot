#!/usr/bin/python3

"""app.py: Primitive webscraping script"""

#from configFile import * #REVIEW
import bot
import parseConfig

if __name__ == '__main__':
    getToken = parseConfig.ParseJson()
    botToken = getToken.getConfig()
    print("Token: ", botToken)
    theBot = bot.RespondToCommands(botToken)
    theBot.initializeBot()

