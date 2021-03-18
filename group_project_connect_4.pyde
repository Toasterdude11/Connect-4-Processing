circleSize = 130
selectorX = 740

One = False
Two = False
Three = False
Four = False
Five = False
Six = False
Seven = False
Right = False
Left = False
Drop = False


def setup():
    size(1500, 1200)
    background(255)
    noStroke()
    global selectorX, circleSize, Drop, player1, Left, Right

        
def draw():
    global selectorX, circleSize, Drop, player1, Left, Right
    
    gameboard()

    
   

    if Right:
        if selectorX <= 1100:
            background(255)
            gameboard()
            selectorX += 180
            player1(selectorX,100)
            Right = False
        elif selectorX > 1100:
            Right = False
        
        
    if Left:
        if selectorX >= 380:
            background(255)
            gameboard()
            selectorX -= 180
            player1(selectorX,100)
            Left = False
        elif selectorX < 380:    
            Left = False
    
    else:
        background(255)
        gameboard()
        player1(selectorX,100)


     
        
   
    #elif Drop:
        #background(255)
        #gameboard()
        #Drop = False


def gameboard():
    fill(18, 7, 178) #blue
    stroke(18, 7, 130)
    strokeWeight(5)
    quad(105, 205, 130, 180, 1370, 180, 1395, 205)
    fill(255)
    noStroke()
    for x in range(135, 1350, 180):
        quad(x, 195, x + 15, 185, x + 115, 185, x + 130, 195)
    fill(18, 7, 178) #blue
    stroke(18, 7, 130)
    strokeWeight(5)
    rect(100, 200, width-200, height-200, 20)
    #outline of gameboard holes
    for y in range(300, height, 160):
        for x in range(200, width-200, 180):
            stroke(18, 7, 130)
            strokeWeight(5)
            fill(18, 7, 178) #lighter blue
            ellipse(x, y, circleSize*1.15, circleSize*1.15)
    #gameboard holes
    for y in range(300, height, 160):
        for x in range(200, width-200, 180):
            noStroke()
            fill(255) #white
            ellipse(x, y, circleSize, circleSize)
            
def player1(x, y):
    global selectorX
    
    fill(255, 0, 0)
    ellipse(selectorX, y, circleSize, circleSize)
    stroke(200, 0, 0)
    strokeWeight(5)
    ellipse(selectorX, y, circleSize / 1.3, circleSize / 1.3)
    strokeWeight(1)
    ellipse(selectorX, y, circleSize / 1.5, circleSize / 1.5)



def keyPressed():
    global selectorX, circleSize, player1, Drop, Left, Right
    
    
    if keyCode == RIGHT:
        Right = True
    elif keyCode == LEFT:
        Left = True
   
    
        
    if key == ' ':
        Drop = True
