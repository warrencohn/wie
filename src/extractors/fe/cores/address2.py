# Tho dia
str = "11 asda, Q1 - Ho Chi Minh"

def checkInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def checkq (q):
	if checkInt(q.replace('Q','')):
		return True
	else: 
		return False
		
def checkp (p):
	if checkInt(p.replace('P','')):
		return True
	else: 
		return False

def checkInt2(s):
	snd = s.strip().split(" ",1)
	if (snd[0].find('\\') != -1) or (snd[0].find('/') != -1):
		return True
	else:
		if checkInt(snd[0]):
			return True
		else:
			return False
			
c = ""
q = ""
p = ""
d = ""
sn = ""
dt = ""
str1 =  str.rsplit(',',4)
str1.reverse()
for i in range(len(str1)):
	if i == 0:
		qc = str1[i].split('-',1)
		c = qc[1].strip()
		if (qc[0].find("Quan") != -1) or (qc[0].find("Q.") != -1):
			q = qc[0].replace("Quan",'').replace("Q.",'').strip()
		elif checkq(qc[0]):
			q = qc[0].replace("Q",'').strip()
		else:
			q = ''
			p = ''
			d = ''
			sn = ''
			dt = qc[0].strip()
	elif i == 1:
		if (str1[i].find("Phuong") != -1) or (str1[i].find("P.") != -1):
			p = str1[i].replace("Phuong",'').replace("P.",'').strip()
		elif checkp(str1[i]):
			p = str1[i].replace("P",'').strip()
		else:
			if checkInt2(str1[i]):
				snd = str1[i].strip().split(" ",1)
				p = ''
				d = snd[1].strip()
				sn = snd[0].strip()
			else:
				p = ''
				d = ''
				sn = ''
				dt = str1[i].strip()
	elif i == 2:
		if str1[i].find("Duong") != -1:
			snd = str1[i].split("Duong",1)
			sn = snd[0].strip()
			d = snd[1].strip()
		else:
			snd = str1[i].strip().split(" ",1)
			if (snd[0].find('\\') != -1) or (snd[0].find('/') != -1):
				sn = snd[0].strip()
				d = snd[1].strip()
			else:
				if checkInt(snd[0]):
					sn = snd[0].strip()
					d = snd[1].strip()
				else:
					sn = ''
					d = str1[i].strip()
	elif i == 4:
		dt = str1[i].strip()

print "c : " + c
print "q : " + q
print "p : " + p
print "d : " + d
print "sn : " + sn
print "dt : " + dt
					
		