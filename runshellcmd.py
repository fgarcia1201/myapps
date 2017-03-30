import commands

#runs ls shell command and counts the output with letter d

output = commands.getoutput('ls')
print output

num = output.count('d')
print num
