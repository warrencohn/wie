from xml.dom.minidom import parseString
from lxml import etree
import new
from new import *

def cleanString(html):
	#print type(html)
	# html = unicode(html, "UTF-8")
	#html = html.replace(u"\u00A0", " ")
	# other way: 
	html = html.replace("\xc2\xa0", "")
	html = html.replace('&nbsp;','')
	html = html.replace('\n', '')
	html = html.replace('\n\r', '')
	html = html.replace('\t', '')

	cleaner = Cleaner(page_structure=False, style=True, javascript=True,scripts=True)
	#cleaner.kill_tags = ['p', 'img']
	#cleaner.remove_tags = ['p']

	result = cleaner.clean_html(html)

	#test = open('test.html', 'w')
	#test.write(result)
	
	return result
    
def exportToFile(table):
    for i in range(len(table[0])):
        file = open('out1/' + str(i) + '.out', 'w')
        for j in range(len(table)):
            if table[j][i].nodeType == table[j][i].TEXT_NODE and (not table[j][i].data.isspace() ):
                file.write(table[j][i].data.encode('utf8').strip() + '\n')            
        

f1 = open('data/657534', 'r')
f2 = open('data/657642', 'r')
parser = etree.HTMLParser(recover=True, remove_blank_text=True, remove_comments=True,encoding="utf-8") # !important !! utf-8

html1 = etree.HTML(cleanString(f1.read()), parser)
html2 = etree.HTML(cleanString(f2.read()), parser)
result1 = etree.tostring(html1, pretty_print=True, method="xml")
result2 = etree.tostring(html2, pretty_print=True,method="xml")

dom1 = parseString(result1)
dom2 = parseString(result2)
t, w = SimpleTreeMatching(dom1.documentElement, dom2.documentElement)

tbl = AlignAndLink(w, dom1.documentElement, dom2.documentElement)
#exportToFile(tbl)
print tbl
#printTable("o.html", tbl)