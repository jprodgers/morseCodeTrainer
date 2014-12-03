class Button(object):
    def __init__(self, displayText):
        self.xPos = 0
        self.yPos = 0
        self.bWidth = 0
        self.bHeight = 0
        self.displayText = displayText
        self.morseCode = ""
        self.clickToggle = False
        
    def size(self, newWidth, newHeight):
        self.bWidth = newWidth
        self.bHeight = newHeight
        
    def move(self, newX, newY):
        self.xPos = newX
        self.yPos = newY
        
    def display(self, bColor, tColor):
        fill(bColor)
        rect(self.xPos, self.yPos, self.bWidth, self.bHeight, 7)
        fill(tColor)
        text(self.displayText, self.xPos + (self.bWidth * .3), self.yPos + (self.bHeight * .75))
