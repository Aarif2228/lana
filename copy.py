with open('blue.txt', 'r') as f:
    file = f.read()

with open("that.txt", "w") as f:
    f.write(file)
   