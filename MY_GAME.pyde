x = 0
y = 50
a = 740
b = 50
c = 375
d = 375
speedx = 2
speedy = 1.5
scoreleft = 0
scoreright = 0
points = 1

def setup():
    size(750,750)
    background(0,0,0)
    
def draw():
    global x,y,a,b,c,d,speedx,speedy,scoreleft,scoreright, points
    background(0,0,0)
    rect(x,y,10,50)
    rect(a,b,740,50)
    circle(c, d, 15)
    c = speedx + c
    d = d + speedy
    
    if  d + 15 > 750:
        speedy = speedy * -1
    if  d - 15 < 0:
        speedy = speedy * -1
    if  c + 15 > 765:
        c = 375
        d = 375
        scoreleft += points
    if  c - 15 < -10:
        c = 375
        d = 375
        scoreright += points
        
        
        
        
    if c >= x and c <= x + 15 and d >= y and d <= y + 50:
        speedx = speedx * -1
        
    
    if c >= a and c <= a + 15 and d >= b and d <= b + 50:
        speedx = speedx * -1
        
    textSize(35)
    text ("Score", 345, 40)
    text (scoreleft, 300, 40)
    text (scoreright, 460, 40)
    
    if scoreright == 6 or scoreleft == 6:
        textSize (35)
        text ("You win!", 340, 375)
        points = 0
    
    
    
    


    
def keyPressed():
    global x,y,a,b
    if key == 'w' or key == 'W':
        y = y - 10
    if key == 's' or key == 'S':
       y = y + 10
    if key == 'o' or key == 'O':
        b = b - 10
    if key == 'l' or key == 'L' :
        b = b + 10
        
        
        
