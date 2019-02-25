import pymel.core as pm

# All objects list
print(pm.ls())

# Select only selected objects
selection = pm.ls(sl=True)
for s in selection:
    print(s)
    
# ls is only one flag, there are other flags in the ls documentation
cam = pm.ls(ca=True)
print(cam)

# Call object by name
obj = pm.ls("group1")
print(obj)

# Select objetcs with wildcard
wildcard = pm.ls("pC*", showType=True)
print(wildcard)

# if we only want the transform
wildcard = pm.ls("pC*", typ="transform")
print(wildcard)


# Create a selection
pm.select("pC*")

# Selection what is inside a group
grp = pm.ls("group1")
print(grp)
pm.select(grp, hi=True)

# unselect
pm.select(cl=True)
pm.select([], r=True) # replace the current selection

# I deplicate group, i can add selections
grp = pm.ls("group1")
pm.select(grp, hi=True)
grp2 = pm.ls("group2")
pm.select(grp2, hi=True, add=True)

# It works for subgroups

# Delete empty groups
selection = pm.ls(sl=True, typ="transform")
for p in selection:
    print(p)
    print(p.getChildren())
    
for p in selection:
    if p.getChildren() == []:
        print(p, " will be deleted")
        pm.delete(p) 
    



