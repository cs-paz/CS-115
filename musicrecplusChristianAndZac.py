#Christian Szablewski-Paz
#CS 115
#I pledge my honor that I have abided by the Stevens Honor System.
#In collaboration with 

from pathlib import *

'''global variables'''
dataBase = {}
name = ""

'''boolean functions'''
def nameInDatabase(): #return true or false if name is in database
    global name #name is defined within function by input, (no parameter)
    while name == "":
        name = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    if name not in dataBase:
        dataBase[name] = []
        return False
    return True

def isPrivate(n): #returns true if user is private
    return n[-1] == '$'
            
def isSimilar(user1, user2): #returns true if the two users are similar
    count = 0
    for artist in user1:
        if artist in user2:
            count +=1
    if count >= 2 and count != len(user1) and count != len(user2):
        return True
    else:
        return False
    
'''get functions'''
def getPopArtists(): #returns most popular artists 
    global dataBase
    totalPrefs = []
    for user in dataBase:
        totalPrefs += dataBase[user]
    totalPrefs = sorted(totalPrefs)

    artistRank = {} 
    holder = ""
    for artist in totalPrefs:
        if artist != holder:
            holder = artist
            artistRank[artist] = 0
        artistRank[artist] += 1

    fnLst = []
    likes = 0
    for artist in artistRank:
        if artistRank[artist] > likes:
            fnLst = [artist]
            likes = artistRank[artist]
        elif artistRank[artist] == likes:
            fnLst.append(artist)
    fnLst = sorted(set(fnLst))
    return (likes, fnLst)

def getUserPref(): #take user's preferences and sort them into database
    global name, dataBase
    artistLst = []
    while True:
        artist = input("Enter an artist that you like (Enter to finish):")
        if artist != "":
            artistLst.append(artist)
        else:
            break
    if name != "":
        dataBase[name] = sorted(list(set(artistLst)))

'''Printer functions'''
def printPopArtists(): #printer for getPopArtists
    for artist in getPopArtists()[1]:
        print(artist)

def printPopVal(): #prints value of most popular artist in list
    print(getPopArtists()[0])

def printRecs(): #prints recomended artists in alphabetical order
    artistLst = []
    recArtists = []
    for user in dataBase:
        if isSimilar(dataBase[name], dataBase[user]) and not isPrivate(user):
            artistLst += dataBase[user]
    for x in artistLst:
        if x not in dataBase[name]:
            recArtists.append(x)
    if recArtists != []:
        for artist in sorted(list(set(recArtists))):
            print(artist)
    else:
        print("No recommendations available at this time")

def printUsersForRecs(): #print user names with the most preferences for recomendations
    lst = []
    maximum = 0
    for key in dataBase:
        if not isPrivate(key):
            if len(dataBase[key]) >= maximum: #if number of artists >= maximum
                if len(dataBase[key]) > maximum:
                    lst.clear()
                lst.append(key)
                maximum = len(dataBase[key])

    if maximum == 0:
        print("Sorry, no user found")
    else:
        for user in sorted(lst):
            print(user)

def printMenu(): #prints menu to console
    print("""Enter a letter to choose an option:
    e - Enter preferences
    r - Get recommendations
    p - Show most popular artists
    h - How popular is the most popular
    m - Which user has the most likes
    q - Save and quit""")

'''file functions'''
def saveFile(fileName): #creates file with data from ........
    #returns true if its already a file, false otherwise
    f = Path(fileName)
    if f.is_file():
        file = open(f, "w+")
        convertDataBaseToFile(file)
        file.close()
        return
    file = open(f, "w+")
    file.close()
    return

def convertDataBaseToFile(file): #converts dataBase into file format
    for user in dataBase:
        artists = ""
        for artist in sorted(dataBase[user]):
            artists += (artist + ",")
        artists = artists[:-1]
        file.write(user + ":" + artists + "\n")

def convertFileToDataBase(file): #takes file format and converts to dataBase
    dct = {}
    for line in file.read().splitlines():
        name, artists = line.split(':')
        artistLst = artists.split(',')
        dct[name] = sorted(artistLst)
    return dct

def prepareToEditFile(fileName): #checks to see if the name of file is
    global dataBase
    f = Path(fileName)
    if f.is_file():
        file = open(f, "r")
        dataBase = convertFileToDataBase(file)
        file.close()
        return 
    file = open(f, "w+")
    file.close()
    return 

if __name__ == '__main__':
    prepareToEditFile("musicrecplus.txt")

    if not nameInDatabase(): #prompt user for name then check if in dataBase
        getUserPref() #set preferences if not in data base
        
    while True: #main do-while loop for entire program
        printMenu()
        uIn = input() #user input for menu
        if uIn == 'e':
            setPreferences()
        elif uIn == 'r':
            printRecs()
        elif uIn == 'p':
            printPopArtists()
        elif uIn == 'h':
            printPopVal()
        elif uIn == 'm':
            printUsersForRecs()
        elif uIn == 'q':
            break

    if dataBase != {}:
        saveFile("musicrecplus.txt")
