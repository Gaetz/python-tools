# Accessing already created nodes

# Knowing the node's name
node = nuke.toNode("Grade2")
print node.Class()
node['whitepoint'].setValue(0.87)
node['blackpoint'].getValue()

# Alrealdy selected nodes
nodes = nuke.selectedNodes()
node = nuke.selectedNodes()[0]
print node.Class()

selection = nuke.selectedNodes()
for n in selection:
    print n.name()
    n['label'].setValue('New label')

# Select a type in selected nodes
selection = nuke.selectedNodes("Grade")
for n in selection:
    print n.name()

# Select everything
all = nuke.allNodes()
print len(all)

# Select all transformsand delete them
allTransforms = nuke.allNodes("Transform")
for n in allTransforms:
    n.setSelected(True)
nukescripts.node_delete(True)

# Modify a lot of nodes
for i in range(40):
    b = nuke.createNode("Blur", inpanel=False)
    b['size'].setValue(i)
    b.setSelected(False)

offset = 1
factor = 0.75

for b in nuke.allNodes("Blur")
    old_size = b['size']
    new_size = (old_size + offset) * factor
    b['size'].setValue(new_size)

for i in range(20):
    b = nuke.createNode("Transform", inpanel=False)
    b.setSelected(False)

label = '[value filter]'
filter = 'Notch'

for t in nuke.allNodes("Transform")
    t['label'].setValue(label)
    t['filter'].setValue(filter)

