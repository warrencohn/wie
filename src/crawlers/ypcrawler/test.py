import json
import re
import pymongo

#s = "\: \' \, \""

#print s

#output = re.sub(r'\\([^"])', r'\1', s)

#print output

#a = open("test.txt", "rb")

#b = a.read()

#b = b.replace("\\'", "'")
#b = b.replace("\\(.)", "\1")
#c = json.loads(b)

import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("compare.dat", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

sys.stdout = Logger()

conn = pymongo.Connection()
db = conn.diadiem

clt = db.data

src = db.stat

a = []

c = []

d = src.find_one()['catCounter']

print ""

for i in range(1, 28):
    regex = r"^%s_" % i
    b = clt.find({"NnDv":{"$regex":regex}})
    # print b.count()
    a.append(b.count())
    c.append(d[i-1] - b.count())
t1 = 0
t2 = 0
dd = 0
for i in range(0, 27):
    print "%s\t%s \t   %s \t   %s" % (i+1, d[i], a[i], c[i])
    t1 += d[i]
    t2 += a[i]
    dd += c[i]
    
print "TT\t%s \t   %s \t   %s" % (t1, t2, dd)


