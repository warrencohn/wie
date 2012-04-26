import pymssql

conn = pymssql.connect(host='(local)', user='sa', password='sa', database='BanDoSG')
cur = conn.cursor()
cur.execute('SELECT * FROM ConDuong')
street = []
for row in cur:
    #print row[3]
	street.append(row[3].lower())

#print street
conn.close()

str = "615 Nguyen Kiem, P.3, Q.Go Vap, Tp.Ho Chi Minh"
str = str.lower()
str = str.replace(',', '')
str = str.replace("duong",'')
str = str.replace("tp.",'')

#street = ["ly thuong kiet","nguyen dinh chieu"]
ward = ["p.","f.","p","f","phuong"]
district = ["q.","quan"]
city = ["ho chi minh"]

indexStreetHead = 0
strt = ''
for i in street :
	indexStreetHead = str.find(i)
	if indexStreetHead != -1 :
		strt = i
		break	

indexWardTail = 0
for i in ward :
	indexWard = str.find(i)
	if indexWard != -1 :
		indexWardTail = indexWard + len(i)
		break

indexDistrictHead = 0
indexDistrictTail = 0
for i in district :
	indexDistrictHead = str.find(i)
	if indexDistrictHead != -1 :
		indexDistrictTail = indexDistrictHead + len(i)
		break

indexCityHead = 0
indexCityTail = 0
ct = 0
for i in city :
	indexCityHead = str.find(i)
	if indexCityHead != -1 :
		ct = i
		break
sn1 = ''
sn2 = ''
d = ''
p = ''
q = ''
c = ''
if(indexStreetHead != -1 and indexWard != -1 and indexDistrictHead != -1 and indexCityHead != -1 ) :
	sn1 = str[:indexStreetHead].strip()
	sn2 = str[:indexStreetHead].strip()
	d = strt
	p = str[indexWardTail:indexDistrictHead].strip()
	q = str[indexDistrictTail:indexCityHead].strip()
	c = ct
else :
	print "here"
	
#print "So nha1      : " + sn1
#print "So nha2      : " + sn2
#print "Duong       : " + d
#print "Phuong      : " + p
#print "Quan        : " + q
#print "Tinh/Thanh  : " + c

#r'.\SQLEXPRESS
conn = pymssql.connect(host='(local)', user='sa', password='sa', database='Address')
cur = conn.cursor()
#cur.executemany("INSERT INTO diachi VALUES(%s)", [ 'aaa', 'bbb' ])
cur.executemany("INSERT INTO diachi VALUES(%s, %s, %s, %s, %s, %s)",[(sn1,sn2,d,p,q,c)])
conn.commit()
conn.close()