#Will List dirs in path
import os

path = "/home/ubuntu/myapps"

print(os.listdir(path))


#for roots, dirs, files in os.walk(path)):
#	for dir in dirs:
#		print("Dir = %s" % dir)
#	for file in files:
#		print("File = %s" %file)

roots = next(os.walk(path))[0]
print("Roots = %s" % roots)

dirs = next(os.walk(path))[1]
print("Dirs = %s" % dirs)

files = next(os.walk(path))[2]
print("Files = %s" % files).upper()

