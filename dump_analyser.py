import os


path = "/home/nsifniotis/PycharmProjects/dumpfiles/"
filesList = [path + f for f in os.listdir(path) if 'xmlDump' in f]

parents = dict()
children = dict()

for filename in filesList:
    with open(filename) as inputFile:
        lines = inputFile.readlines()

    nodeStack = ['NOTHING']
    for line in lines:
        line = line.strip()
        tag = line[1:-1]

        if '/' not in tag:
            # process an opening tag
            lastTag = nodeStack[-1]
            if lastTag not in children:
                children[lastTag] = set()
            children[lastTag].add(tag)

            if tag not in parents:
                parents[tag] = set()
            parents[tag].add(lastTag)

            nodeStack.append(tag)
        else:
            # process a closing tag.
            nodeStack.pop()

# build the master keys list.
fullSet = set(list(children.keys()) + list(parents.keys()))
orderedKeys = sorted(list(fullSet))
for key in orderedKeys:
    parentsList = []
    childrenList = []
    if key in parents:
        parentsList = list(parents[key])
    if key in children:
        childrenList = list(children[key])

    print(key + ":")
    print("  PARENTS : " + str(sorted(parentsList)))
    print("  CHILDRN : " + str(sorted(childrenList)))
    print()

# Group these suckers
# Hugely interested in things with no or one parent or child.
print("NO PARENTS")
for key in orderedKeys:
    if key in parents:
        if len(parents[key]) is 0:
            print(key)
    else:
        print(key)

print()
print("NO CHILDREN")
for key in orderedKeys:
    if key in children:
        if len(children[key]) is 0:
            print(key)
    else:
        print(key)

print()
print("ONE PARENT")
for key in orderedKeys:
    if key in parents:
        if len(parents[key]) is 1:
            print(key + ": " + str(parents[key]))

print()
print("ONE CHILD")
for key in orderedKeys:
    if key in children:
        if len(children[key]) is 1:
            print(key + ": " + str(children[key]))
