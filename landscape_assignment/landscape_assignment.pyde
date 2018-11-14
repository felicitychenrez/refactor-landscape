# while loop
# increase a variable
# use draw() for animation 
import time
x = 0
sun_x = 0
sun_y = 0
def draw_sun(x,y):
    print("Drawing sun at ({x}, {y}).")
draw_sun(0, 0)
def setup():
    size(640, 480)

def draw():
    global x, sun_x, sun_y 
    if x >= 640:
        x = 0
    x += 3
    background(136, 206, 250)
    noStroke()
    fill (255)
    ellipse(x, height/4, 50, 50)
    ellipse(x+30, height/4, 50, 50)
    ellipse(x+10 , height/4-20, 50, 50)
    time.sleep(0.01)
    ellipse(x-100, height/4, 50, 50)
    ellipse(x-70, height/4, 50, 50)
    ellipse(x-80 , height/4-20, 50, 50)
    fill (0, 128, 0)
    rect(0, height - 50, width, 50)
    fill (200)
    triangle(640, 430, 480, 300, 320, 430)
    fill (255)
    triangle(516, 330, 480, 300, 444, 330)
    fill (200)
    triangle(400, 430, 240, 300, 80, 430)
    fill (255)
    triangle(276, 330, 240, 300, 204, 330)
    fill (200, 200 , 0)
    ellipse(sun_x, sun_y , 100, 100)
    while sun_x < 20 and sun_y < 20:
        sun_x += 1
        sun_y += 1
    

    
