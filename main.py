import webbrowser
import os
import time
import datetime as dt

print("Welcome! The time is " + dt.datetime.now().strftime("%I:%M:%S %p") + ". The date is " + dt.datetime.now().strftime("%A %B %d, %Y"))
print("Note: please do not include \"http://\" while typing in the URL's. Also, every time you re-run the program, \nyou will have to re-enter the websites to block.  Thank you!\n")

countofwebs = int(input("How many website(s) would you like to block? Enter here: "))

websites = []

for i in range(countofwebs):
    webs = input("Enter website to block: ")
    websites.append("http://" + webs)

print("Saving...")
time.sleep(0.5)
print("Saved! Activating website blocker...")
time.sleep(1)
os.system("clear")

while True:
    openweb = input("Which website would you like to open? ")
    openweb = "http://" + openweb

    if openweb in websites:
        print("Website blocker has been initiated. This website has been blocked.")
        time.sleep(1.5)
        os.system("clear")
    else:
        if "." in openweb or "localhost" in openweb:
            print("You are allowed to open this website! Opening...")
            webbrowser.open(openweb)
            time.sleep(1.5)
            os.system("clear")
        else:
            print("Failed to open this website. Invalid URL.")
