# http://www.yellowpages.vn/ 
#str = "37A Phan Xich Long, P. 3, Q. Phu Nhuan,Tp. Ho Chi Minh"
str = "1147 Bình Quới, Phường 28, Quận Bình Thạnh - Hồ Chí Minh"

#str = str.lower()
str = str.replace(',', '')
str = str.replace("Tp.",'')

#street = ["ly thuong kiet","nguyen dinh chieu","phan xich long","tran quoc thao"]
ward = ["P.","Phường"]
district = ["Q.","Quận"]
city = ["Hồ Chí Minh"]

#1
#iStreet = -1
#nameStreet = ''
#for i in street :
#	iStreet = str.find(i)
#	if iStreet != -1 :
#		nameStreet = i
#		break	

#2
iStreet2 = str.find(' ')

iWard1 = -1
iWard2 = -1
for i in ward :
	iWard1 = str.find(i)
	if iWard1 != -1 :
		iWard2 = iWard1 + len(i)
		break

iDistrict1 = -1
iDistrict2 = -1
for i in district :
	iDistrict1 = str.find(i)
	if iDistrict1 != -1 :
		iDistrict2 = iDistrict1 + len(i)
		break

iCity = -1
nameCity = ''
for i in city :
	iCity = str.find(i)
	if iCity != -1 :
		nameCity = i
		break
sn1 = ''
sn2 = ''
d = ''
p = ''
q = ''
c = ''
if iStreet2 == -1:
	print "Khong tim thay ten duong"
elif(iWard1 != -1 and iDistrict1 != -1 and iCity != -1 ) :
	#sn = str[:iStreet].strip()
	sn = str[:iStreet2].strip()
	#d = nameStreet
	d = str[iStreet2:iWard1].strip()
	p = str[iWard2:iDistrict1].strip()
	q = str[iDistrict2:iCity].replace('-', '').strip()
	c = nameCity
	print "So nha      : " + sn
	print "Duong       : " + d
	print "Phuong      : " + p
	print "Quan        : " + q
	print "Tinh/Thanh  : " + c
else:
	print "error"
	
