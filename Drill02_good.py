import math

from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render_all(x,y):
     clear_canvas_now()
     grass.draw_now(400,30)
     character.draw_now(x,y)
     delay(0.01)

def run_circle():
    print('CIRCLE')

    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        render_all(x,y)


def run_rectangle():
    print('CURCLE')

    for x in range(50, 750+1, 10):
       render_all(x,90)
    pass

while True:
    run_circle()
    run_rectangle()
    #break;

close_canvas()
