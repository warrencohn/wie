html = 'vinh\xa0'
f1 = open('xa0.txt', 'r')

s1 = f1.read()

print "1."
ss = s1.decode('windows-1252') # --> unicode
ss.replace(u"\u00A0", "-")
print type(ss), ss

print "2."
print type(s1), s1

# s2 = s1.replace("\xc2\xa0", " ")

#print "3."
#print s2

#uniString = unicode(s1, "UTF-8")
#uniString = uniString.replace(u"\u00A0", " ")

#print "4."
#print uniString
