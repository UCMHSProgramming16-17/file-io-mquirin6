import csv
file = open("newcsv.csv", "w")

csvwriter = csv.writer(file, delimiter = ',' )

csvwriter.writerow(["Hi", "How", "Are", "You" ])

file.close()