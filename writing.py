writing = open(input("Title of File: "), 'w')
writing

lines = int(input("How many lines are you writing: "))

for x in range(lines):
        writing.write(input(">> ") + "\n")