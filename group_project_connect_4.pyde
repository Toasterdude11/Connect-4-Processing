
circleSize = 130
selectorX = 740

def setup():
    size(1500, 1200)
    background(255)
    noStroke()
    global selectorX, circleSize, player, Left, Right, One, Two
    
    One = False
    Two = False
    Right = False
    Left = False
 
               
def draw():
    global selectorX, circleSize, player, Left, Right, One, Two
    
    #draw the gameboard
    gameboard()

    #if right arrow is True, player (yellow or red) moves one slot to the right and has to stop at the end of the gameboard
    if Right:
        if selectorX <= 1100:
            background(255)
            gameboard()
            selectorX += 180
            player(selectorX, 100)
            Right = False
        elif selectorX > 1100:
            Right = False
 
    #if left arrow is True, player (red or yellow) moves one slot to the left and has to stop at the end of the gameboard
    if Left:
        if selectorX >= 380:
            background(255)
            gameboard()
            selectorX -= 180
            player(selectorX,100)
            Left = False
        elif selectorX < 380:    
            Left = False
    
    else:
        background(255)
        gameboard()
        player(selectorX,100)


#gameboard drawing
def gameboard():
    fill(18, 7, 178) #blue
    stroke(18, 7, 130) #darker blue
    strokeWeight(5)
    #top of the gameboard
    quad(105, 205, 130, 180, 1370, 180, 1395, 205)
    fill(255)
    noStroke()
    #slots in the top of the gameboard
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

#player1 or 2 drawing, 1 is red, 2 is yellow          
def player(x, y):
    global selectorX
    #player1 is red
    if One:
        fill(255, 0, 0)
        ellipse(selectorX, y, circleSize, circleSize)
        stroke(200, 0, 0) #darker red
    #player2 is yellow
    elif Two:
        fill(255, 255, 0)
        ellipse(selectorX, y, circleSize, circleSize)
        stroke(200, 200, 0)
    strokeWeight(5)
    ellipse(selectorX, y, circleSize / 1.3, circleSize / 1.3)
    strokeWeight(1)
    ellipse(selectorX, y, circleSize / 1.5, circleSize / 1.5)


def keyPressed():
    global selectorX, circleSize, player1, Drop, Left, Right, One, Two
    
    #if 1 is pressed player1 (red) is True, if 2 is pressed player2 (yellow) is True
    if key == '1':
        One = True
        Two = False
    elif key == '2':
        Two = True
        One = False
        
    #if right arrow key is pressed it's True, if left arrow key is pressed it's True
    if keyCode == RIGHT:
        Right = True
    elif keyCode == LEFT:
        Left = True
