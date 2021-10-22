# -h for help
# -n for name

RedColor     = "\033[1;31m"
GreenColor   = "\033[1;32m"
YellowColor  = "\033[1;33m"
BlueColor    = "\033[1;34m"
WhiteColor   = "\u001b[37m"
def showHelp():
    print (GreenColor + "Welcome to purpleanime CLI")
    print (YellowColor + "Instructions :")
    print ("1) For help, use -h")
    print ("2) To specify anime, use -n")
    print (BlueColor + "Example : purpleanime -n attack on titan")
    print (WhiteColor, end="")
import sys
arguments = sys.argv
numOfArguments = len (sys.argv) - 1
filename = arguments[0]
arguments = arguments[1:]
NAME = None

if "-h" in arguments:
    showHelp()
    exit(-1)

if "-n" in arguments:
    NAME = extractName(arguments)
    foundAnime = findAnime(NAME)
    if foundAnime:
        pass
    else :
        print ("Sorry, this anime could not be found")
        exit (-1)
else :
    NAME = input("Enter Name of Anime : ")