import dictionary
from src import export

entries = dictionary.entries("./cedict.txt")

for entry in entries:
    if entry.simp == "打":
        print("line:", entry.line)
        print("defs:", entry.defs)
        break
