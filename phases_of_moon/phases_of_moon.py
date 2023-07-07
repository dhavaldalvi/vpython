from vpython import *
import numpy as np


canvas_1 = canvas(width=600 ,height=400)
canvas_1.lights = []
canvas_1.autoscale = False
canvas_1.range = 6
canvas_1.title = '<b>Phases of Moon</b>'
canvas_1.align = 'left'

earth = sphere(canvas = canvas_1, pos = vector(0,0,0), radius = 1, texture = textures.earth)
earth.rotate(axis = vector(1,0,0), angle = pi/2)
moon = sphere(canvas = canvas_1, pos = vector(5,0,0), radius = 0.6, texture = 'moon.jpg')
moon.rotate(axis = vector(1,0,0), angle=pi/2)
background = sphere(canvas=canvas_1, pos=vector(0,0,0), texture = 'galaxy.jpg', radius = 50, shininess = 0)
background.rotate(axis = vector(1,0,0), angle = pi)
source = distant_light(canvas = canvas_1, direction = vector(-100,0,0), color = color.white)


canvas_2 = canvas(width = 600, height = 400)
canvas_2.ambient = color.black
canvas_2.lights = []
canvas_2.title='As viewed from the Earth'
canvas_2.align='right'

moon1 = sphere(canvas = canvas_2, radius = 1, texture = 'moon.jpg',shininess=0)
lamp = local_light(canvas = canvas_2, pos = vector(0,0,0), color = color.white)

i = 0.0
while True:
    rate(10)
    moon.pos.x = 5*np.sin(i)
    moon.pos.y = 5*np.cos(i)
    lamp.pos.z = 500*np.cos(i-np.pi/2)
    lamp.pos.x = 500*np.sin(i-np.pi/2)
    i = i + 0.01
