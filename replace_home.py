import re

with open("index.html", "r") as f:
    c = f.read()

# Replace Hero Title
c = c.replace("Preparing Scholars<br/>for the World's <em>Leading Universities</em>", "Preparing Scholars<br/>for a <em>Global future</em>")

# Replace AP Excellence -> AP Exams
c = c.replace("Aurelius AP Excellence", "Aurelius AP Exams")

# Replace Admission Guidance -> Admissions Guidance
c = c.replace("Admission Guidance", "Admissions Guidance")

# Fix meta tags if necessary
c = c.replace("Preparing Scholars for the World's Leading Universities", "Preparing Scholars for a Global future")

with open("index.html", "w") as f:
    f.write(c)
