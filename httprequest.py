import requests
#defining the function
def geturl():
	r = requests.get('https://google.com')

	status = r.status_code

 	print ("This is the status of the request:")
        print status
	if status != 200:
		print ("The status is not 200")
	else:
		print ("The status is 200.")

#run the function geturl
geturl()

#if status==200:
#	print ("The web url is legit")
#else:
#	print ("The web url doesn't exist")

