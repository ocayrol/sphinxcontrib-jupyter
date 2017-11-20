
with open("nodesList.txt") as inputFile:
    lines = inputFile.readlines()

for line in lines:
    line = line.strip()
    parts = line.split(",")

    for nodeName in parts:
        print("    def visit_" + nodeName + "(self, node):")
        print("        self.dumpFile.write(\"<" + nodeName + ">\\n\")")
        print()
        print("    def depart_" + nodeName + "(self, node):")
        print("        self.dumpFile.write(\"</" + nodeName + ">\\n\")")
        print()