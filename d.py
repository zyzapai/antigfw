
import sys,re,base64

def splitList(txt):
	arr = txt.split("\n")
	pattern ='^([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])$'
	l = []
	for line in arr:
		if (not len(line)): #empty line
			continue
		if (line[0] == "!"): #Comment line
			continue
		elif(line[0:2] =="@@"):#Forbidding line
			continue
		elif(line.find("/")!=-1 or line.find("*")!=-1 or line.find("[")!=-1 or line.find("%")!=-1 or line.find(".")==-1 ): #URL is ignored, only domains left
			continue
		elif(re.search(pattern, line)):#IP address
			continue

		#In this case, domain name is irrelevant to protocol(http or https)
		elif(line[0:2] =="||"):
			l.append(line[2:])
		elif(line[0] == "."):
			l.append(line[1:])
		else:
			l.append(line)
	
	return set(l)

f = open('gfwlist.txt', 'r')
r = open('result.txt', 'w')
txt = f.read()
txt = base64.decodestring(txt)
domains = splitList(txt)
for line in domains:
	r.write("server=/%s/127.0.0.1#53535\n" % line)

