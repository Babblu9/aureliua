with open("global-pathways.html", "r") as f:
    c = f.read()

c = c.replace("programmes", "programs")
c = c.replace("Programmes", "Programs")

with open("global-pathways.html", "w") as f:
    f.write(c)

