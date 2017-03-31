import csv

def printheaders():
	print ("Year, Model")

def loadcsv():
 	count=0
	with open('file.csv', 'r') as f:
		r = csv.reader(f, delimiter=',')
		for row in r:
			if len(row) == 2:
				count = count+1
				print(row[0] + ', ' + row[1])
	print "Total cars: %s" % count

printheaders()
loadcsv()
