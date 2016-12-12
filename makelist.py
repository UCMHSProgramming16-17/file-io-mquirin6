list = open("mylist.py", 'w')

for x in range(1, 11):
    list.write(str(x) + "." + " " + input("Item: ") + "\n")