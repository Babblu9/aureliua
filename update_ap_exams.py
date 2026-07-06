with open("index.html", "r") as f:
    c = f.read()

c = c.replace("Aurelius AP Exams", "AP Exams")

with open("index.html", "w") as f:
    f.write(c)

