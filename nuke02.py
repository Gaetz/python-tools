# Interaction with user


# Display
nuke.message("Can you hear me Major Tom?")
nuke.message("Can you hear me Major Tom?\nIs that you, Ground Control?")

# Boolean
answer = nuke.ask("Can you hear me Major Tom?")
print answer
if(answer):
    print "Ok, i'm relieved."

# Text input
answer = nuke.getInput("What is your favorite color?")
print type(answer)

# Ask users for nodes to create
node_type = nuke.getInput("Node type (default:Blue)", "Blur")
node_count = int(nuke.getInput("Node number (default:10)", "10"))
limit = 50

if node_count > limit:
    go_on = nuke.ask("Limit is reached, do you want to continue?")
    if go_on:
        for i in range(node_count):
            nuke.createNode(node_type, inpanel=False)
        nuke.message("{} {} nodes were created!".format(node_count, node_type))
    else:
        nuke.message("Operation cancelled")

