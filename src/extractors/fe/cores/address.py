﻿# http://www.yellowpages.vn/ +
#coding=utf-8
#str = "37A Phan Xich Long, P. 3, Q. Phu Nhuan,Tp. Ho Chi Minh"
#str = "1147 Bình Quới, Phường 28, Quận Bình Thạnh - Hồ Chí Minh"
#str = "Phòng 107, 232 (10) Đường 3 Tháng 2, P. 12, Q. 10,"
#str = u"Phong 107,Đường 3 Thang 2, P.12, Q.10,"
#str = u"Phòng 1205, Tầng12, Tòa Nhà Mê Linh Point, 2 Ngô Đức Kế, Q. 1,"
str = u"11G4 Khu Dân Cư Tân Quy Đông, Đường Nguyễn Thị Thập, Phường Tân Phong, Quận 7"
#str = u"83 Nguyễn Cư Trinh, Quận 1,"
#215 Tổ 59,Khu Phố 4, Phường Tân Chánh Hiệp, Quận 12,Đường

def checkInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False	

def checkStr(str):
	if str[len(str)-1] != ',':
		str = str + ','
	str1 =  str.rsplit(',',4)
	str1.reverse()
	l = []
	for i in range(len(str1)):
		if i == 0:
			if str1[i].strip() == '':
				 l.append(u"Hồ Chí Minh")
			else:
				 l.append(str1[i].strip())
		elif i == 1:
			l.append(str1[i].replace(u"Q.",'').replace(u"Quận",'').strip())
		elif i == 2:
			l.append(str1[i].replace(u"P.",'').replace(u"Phường",'').strip())
		elif i == 3:
			str1[i]=str1[i].replace(u"Số",'')
			if str1[i].find(u"Đường") != -1:
				snd = str1[i].split(u"Đường",1)
				l.append(snd[1].strip())
				l.append(snd[0].strip())
			else:
				snd = str1[i].strip().split(" ",1)
				if (snd[0].find('\\') != -1) or (snd[0].find('/') != -1) or (snd[0].find('-') != -1) :
					l.append(snd[1].strip())
					l.append(snd[0].strip())
				else:
					if checkInt(snd[0][0]):
						l.append(snd[1].strip())
						l.append(snd[0].strip())
					else:
						l.append(str1[i].strip())
						l.append('')
		elif i == 4:
			l.append(str1[i].strip())
	return l
			
print checkStr(unicode(str))
