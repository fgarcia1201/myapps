import requests

outputfile = open('output.txt', 'a')

var = requests.get('https://udemy.com')

var.read()
#outputfile.write(var.status_code)
