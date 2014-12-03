#This is a program I'm writing to learn python with, and git apparently.
add_library('minim')
import string
import time
import random
from Button import Button
from MorseCodes import morseCodes
buttons = []
tempWidth = 50
tempHeight = 50
tempTextSize = 30
tempRowColum = 4
delayTime = 12
lastTime = time.clock()-delayTime+2
minim = Minim(this)
dotLength = .1
currentRandom = 0

def setup():
    background(51)
    textSize(tempTextSize)
    currentRandom = random.randint(0, len(buttons))
    for k,i in enumerate(morseCodes):
        b = Button(i[0])
        b.morseCode = i[1]
        b.size(tempWidth, tempHeight)
        b.move((k%tempRowColum)*tempWidth+10, (k/tempRowColum)*tempHeight+10)
        buttons.append(b)
    if len(buttons)%tempRowColum:
        sizeY = (len(buttons)/tempRowColum)*tempHeight+tempHeight+20
    else:
        sizeY = (len(buttons)/tempRowColum)*tempHeight+20
    size(tempRowColum*tempWidth+20, sizeY)
    
def draw():
    currentTime = time.clock()
    background(51)
    for k,i in enumerate(buttons):
        if mousePressed and mouseX > i.xPos and mouseX < i.xPos + tempWidth and mouseY > i.yPos and mouseY < i.yPos + tempHeight:
            i.display(color(255,0,0), color(0,0,0))
            i.clickToggle = True
            #playCode(i.morseCode)
            if k == currentRandom:
                currentRandom = random.randint(0, len(buttons))
                lastTime - delayTime
        else:
            i.display(color(255,255,255), color(0,0,0))
            i.clickToggle = False
    if currentTime - lastTime > delayTime:
        lastTime = currentTime
        playCode(buttons[currentRandom].morseCode)
    
def playCode(tempCode):
    tempLength = dotLength
    for i in tempCode:
        if i == "*":
            player = minim.loadFile("short.wav")
            tempLength = dotLength
        elif i == "-":
            player = minim.loadFile("long.wav")
            tempLength = dotLength * 4
        player.play()
        time.sleep(tempLength)
