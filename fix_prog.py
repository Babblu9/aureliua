import os
import glob

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, "r") as f:
        c = f.read()
    
    c = c.replace("programme", "program")
    c = c.replace("Programme", "Program")
    
    with open(file, "w") as f:
        f.write(c)

print("Done replacing.")
