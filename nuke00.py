# Node creation

# Create a node
nuke.createNode("ColorCorrect")
nuke.createNode("Blur")

# Destroy nodes
nukescripts.node_delete(popupOnError=True)
# You can see python commands in the python script upper part

# Create variable, don't display property windows
b = nuke.createNode("Blur", inpanel=False)

# Data about our object
print type(b)
print b.Class()

# Change properties
b['size'].setValue(10)
b['quality'].setValue(10)
b['filter'].setValue('box')

print b['size'].getValue()

# List all knobs with values
for k in b.knobs():
    print k, type(b[k])
    print '----> ', b[k].getValue()

# Multiple nodes
number = 10
for i in range(number):
    nuke.createNode('Blur', inpanel=False)

# Nodes are connected one with each other
# To avoid this, we have to deselect the created node

for i in range(number):
    b = nuke.createNode('Blur', inpanel=False)
    b.setSelected(False)

# Different pipelines, tidy them and merge
nodes = []
blur_list = []

for i in range(number):
    constant = nuke.createNode('Constant', inpanel=False)
    g = nuke.createNode('Grade', inpanel=False)
    b = nuke.createNode('Blur', inpanel=False)
    b.setSelected(False)
    nodes.append(constant)
    nodes.append(b)
    nodes.append(g)
    blur_list.append(b)

for n in nodes:
    n.setSelected(True)

_autoplace()

for n in nodes:
    n.setSelected(False)

for b in blur_list:
    b.setSelected(True)
m = nuke.createNode("Merge2", inpanel=False)

def autoplace(nodeList):
    for n in nodeList:
        n.setSelected(True)
    _autoplace()
    for n in nodeList:
        n.setSelected(False)

# Managing connections
c = nuke.createNode('Constant', inpanel=False)
nodes = [c]
for i in range(number):
    t = nuke.createNode("Transform", inpanel=False)
    t.setInput(0, c)
    t.setSelected(False)
    nodes.append(t)

autoplace(nodes)

# Basic 3d set 
scene = nuke.createNode("Scene", inpanel=False)
scene.setSelected(False)
scan = nuke.createNode("ScanlineRender", inpanel=False)
scan.setSelected(False)
camera = nuke.createNode("Camera2", inpanel=False)
camera.setSelected(False)
constant = nuke.createNode("Constant", inpanel=False)
constant.setSelected(False)

scan.setInput(0, constant)
scan.setInput(1, scene)
scan.setInput(0, camera)

autoplace([scan, scene, camera, constant])
