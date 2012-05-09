# http://www.yellowpages.vn/ 
#str = "37A Phan Xich Long, P. 3, Q. Phu Nhuan,Tp. Ho Chi Minh"
#str = "1147 Bình Quới, Phường 28, Quận Bình Thạnh - Hồ Chí Minh"
#str = "Phòng 107, 232 (10) Đường 3 Tháng 2, P. 12, Q. 10,"
#str = "Phong 107, 232 (10) Duong 3 Thang 2, P.12, Q.10,"
#str = "Phòng 1205, Tầng12, Tòa Nhà Mê Linh Point, 2 Ngô Đức Kế, P. Bến Nghé, Q. 1,"
str = "Phong 1205, Tang 12, Toa Nha Me Linh Point, 232/2 Duong 3 Thang 2, P.Ben Nghe, Q. 1,"

def checkInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

c1 = ""
q1 = ""
p1 = ""
d1 = ""
sn1 = ""
dt = ""
str1 =  str.rsplit(',',4)
str1.reverse()
for i in range(len(str1)):
	if i == 0:
		if str1[i].strip() == '':
			c1 = "Ho Chi Minh"
		else:
			c1 = str1[i].strip()
	elif i == 1:
		q1 = str1[i].replace("Q.",'').strip()
	elif i == 2:
		p1 = str1[i].replace("P.",'').strip()
	elif i == 3:
		if str1[i].find("Duong") != -1:
			snd = str1[i].split("Duong",1)
			sn1 = snd[0].strip()
			d1 = snd[1].strip()
		else:
			snd = str1[i].strip().split(" ",1)
			if (snd[0].find('\\') != -1) or (snd[0].find('/') != -1):
				sn1 = snd[0].strip()
				d1 = snd[1].strip()
			else:
				if checkInt(snd[0]):
					sn1 = snd[0].strip()
					d1 = snd[1].strip()
				else:
					sn1 = ''
					d1 = str1[i].strip()
	elif i == 4:
		dt = str1[i].strip()
		
print c1
print q1
print p1
print d1
print sn1
print dt
			
	
