#Creates a request on the url and prints out the status code, heads and content of the url.
import requests

r = requests.get('https://udemy.com')

print r.status_code
print r.headers
print r.content
