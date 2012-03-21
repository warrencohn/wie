from xml.dom.minidom import parseString
from lxml import etree

from new import *
# @hungvjnh
def cleanString(html):
	print type(html)
	# html = unicode(html, "UTF-8")
	#html = html.replace(u"\u00A0", " ")
	# other way: 
	html = html.replace("\xc2\xa0", "")
	
	html = html.replace('\n', '')
	html = html.replace('\n\r', '')
	html = html.replace('\t', '')

	cleaner = Cleaner(page_structure=False, style=True, javascript=True,scripts=True)
	#cleaner.kill_tags = ['p', 'img']
	#cleaner.remove_tags = ['p']

	result = cleaner.clean_html(html)

	test = open('test.html', 'w')
	test.write(result)
	
	return result

f1 = open('data/657534', 'r')
f2 = open('data/657642', 'r')

parser = etree.HTMLParser(recover=True, remove_blank_text=True, remove_comments=True,encoding="utf-8") # !important !! utf-8

s1 = f1.read()
s2 = f2.read()

# @hungvjnh
s11 = cleanString(s1)
s22 = cleanString(s2)

html1 = etree.HTML(s11, parser)
html2 = etree.HTML(s22, parser)


result1 = etree.tostring(html1, pretty_print=False, method="xml")
result2 = etree.tostring(html2, pretty_print=False,method="xml")

dom1 = parseString(result1)
dom2 = parseString(result2)

body1 = dom1.getElementsByTagName('body')[0]
body2 = dom2.getElementsByTagName('body')[0]

t, w = SimpleTreeMatching(dom1.documentElement, dom2.documentElement)

tbl = AlignAndLink(w, dom1.documentElement, dom2.documentElement)
printTable('out.html', tbl)
