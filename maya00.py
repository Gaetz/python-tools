import pymel.core as pm

cube = pm.polyCube()
print(cube)
print type(cube[0])
print type(cube[1])

# Transform change
pm.move(cube[0], [1, 0, 0])
pm.move(cube[0], [0, 0, 0])
pm.scale(cube[0], [2, 0.5, 7])

def reset_transform(obj):
    pm.move(obj, [0, 0, 0])
    pm.scale(obj, [1, 1, 1])
    pm.rotate(obj, [0, 0, 0])

    
reset_transform(cube[0])

# Set attribute way
cube[0].setAttr('translate', [1, 1, 0])
cube[0].setAttr('translateX', 1)
cube[0].setAttr('translateY', 2)
cube[0].setAttr('translateZ', 3)
cube[0].setAttr('rotateY', 20)

reset_transform(cube[0])

print cube[0].getAttr('rotateX')

cube = pm.polyCube(w=3, h=2, d=1)
# you get arguments in the documentation 

sphere = pm.polySphere(sx = 5, sy = 5)

number = 500
for i in range(number):
    cube = pm.polyCube()
    cube[0].setAttr('translate', [i * 1.25, i / 2.0, 0])
    cube[0].setAttr('rotate', [0, 5 * i, 0])
    cube[0].setAttr('scale', [(i+1) * 0.5, (i+1) * 0.1, 1])

# Now let's create more customizable stair

def create_stairs(step_number, step_count_circle):
    step = {"width": 12.0, "height": 1.5, "depth": 3.0 }
    #global_height = 200
    steps = []
    for i in range(step_number):
        cube_name = "stairsCube" + str(i).zfill(4)
        cube = pm.polyCube(w = step["width"], h = step["height"], d = step["depth"], n = cube_name)
        pivot_rotate = [-step["width"] / 2, -step["height"] / 2, step["depth"] / 2]
        pm.rotate(cube[0], 0, 360 / step_count_circle * i, 0, pivot=pivot_rotate)
        pm.move(cube[0], step["width"] / 2, step["height"] / 2 + i * step["height"], -step["depth"] / 2)
        steps.append(cube)
    stairs_group = pm.group(steps, n="stairsGroup")
    pm.select(cl=True)

create_stairs(1000, 30)