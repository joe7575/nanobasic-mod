# Generate a TOC from the given MD File

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

lines = open("manual.md").readlines()

toc = []
for line in lines:
    if line.startswith("##"):
        indentation = line.count("#")
        blanks = " " * ((indentation - 1) * 2)
        line = line[indentation:].strip()
        link = line.replace(" ", "-").replace(".", "-").lower()
        toc.append("%s* [%s](#%s)" % (blanks, line, link))

print("\n".join(toc))

