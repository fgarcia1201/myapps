import commands

#runs ls shell command and counts the output with letter d

output = commands.getoutput('ls -l')
print output

num = output.count('d')
print num

#runs another command that checks the iostat.

netstat = commands.getoutput('netstat -an |grep LISTEN')

print netstat


