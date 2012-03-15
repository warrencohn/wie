from xml.dom.minidom import parse, parseString
import lxml.html
from lxml.html.clean import Cleaner
import tidy
from lxml import etree
from StringIO import StringIO

def SimpleTreeMatching(node1, node2):    
    if node1.nodeType != node2.nodeType:
        return (0, [])
    else:
        if node1.nodeType == node1.ELEMENT_NODE:
            if node1.tagName != node2.tagName:
                return (0, [])
            else:
                k = len(node1.childNodes)
                n = len(node2.childNodes)
                m = [[0 for x in range(n+1)] for y in range(k+1)]
                w = [[(0, []) for x in range(n)] for y in range(k)]
                for i in range (1, k+1):       
                    for j in reversed(range (1, n+1)):  
                        w[i-1][j-1] = SimpleTreeMatching(node1.childNodes[i-1], node2.childNodes[j-1])         
                        m[i][j] = max( m[i][j-1], m[i-1][j], m[i-1][j-1]+w[i-1][j-1][0] )
                return (m[k][n] + 1, w)
        else:
            return (1, [])
            
def AlignAndLink(w, node1, node2):
    m = [[x for x, y in row] for row in w]
    m_max = max([max(row) for row in m])
    if m_max == 0:
        return []
    else :
        table = []
        numRow = len(m)
        numCol = len(m[0])
        if numCol < numRow:
            for i in range(0, numCol):
                for j in range(0, numRow):
                    if m[j][i] == m_max:
                        if m[j][i] == 1:
                            table.append([node1.childNodes[j], node2.childNodes[i]])
                        else:
                            table += AlignAndLink(w[j][i][1], node1.childNodes[j], node2.childNodes[i])
                        break
        else:
            for i in range(0, numRow):
                for j in range(0, numCol):
                    if m[i][j] == m_max:
                        if m[i][j] == 1:
                            table.append([node1.childNodes[i], node2.childNodes[j]])
                        else:
                            table += AlignAndLink(w[i][j][1], node1.childNodes[i], node2.childNodes[j])
                        break
        return table    

def partialTreeAlignment(S,w):
	Ts = S.childNodes[0]
	S.removeChild(Ts)
	Document.createElement(R)
	while (S.hasChildNodes()):
		Ti = S.childNodes[0]
		S.removeChild(Ti)
		temp = []
		if (checkInsert(w)):
			insertIntoSeed(Ts,Ti)
			S = S + R
			R = [[]]
		else :
			R.insert(len(R),Ti)
	return Ts
	
def insertIntoSeed(Ts,Ti):
	
def checkInsert(w):
	m = [[x for x, y in row] for row in w]
    numRow = len(m)
    numCol = len(m[0])
    if numCol < numRow:
		j = 0 
		#for j in range(0, numCol):
		while (j < numCol):
			m_max = max([m[i][j] for i in range(numRow)]):
			if m_max == 0:
				if(j == 0):
					for k in range(j+1,numCol):
						j = k
						m_max2 = max([m[i][k] for i in range(numRow)])
						if m_max2 != 0:
							break
						if j == numCol:
							return False
					#check First Row
					if m[0][j] == max([m[i][j] for i in range(numRow)]) :
						j = j + 1
						continue
					else:
						return False
				else:
					flagHead = j-1
					flagTail = -1
					for k in range(j+1,numCol):
						j = k
						m_max2 = max([m[i][k] for i in range(numRow)])
						if m_max2 != 0:
							flagTail = k
							break
					if flagTail == -1: #Check Final Row
						if m[numRow-1][j] == max([m[i][j] for i in range(numRow)]) :
							#return True
							break;
					else: #Check Head and Tail are consecutive siblings
						m_max3 = max([m[i][flagHead] for i in range(numRow)])
						m_max4 = max([m[i][flagTail] for i in range(numRow)])
						for x in range(0,numRow-1):
							if ((m[x][flagHead] = m_max3) and (m[x+1][flagHead] != m_max4)) or ((m[x][flagHead] != m_max3) and (m[x+1][flagHead] == m_max4)):
								return False
					j = j + 1
					continue
			for i in range(0,numRow):
				if m[i][j] = m_max:
					if m[i][j] == 1:
						return True
					else:
						checkInsert(w[i][j][1])
					break
								
    else:	# numCol > numRow
		i = 0
		while(i<numRow)
			m_max = max(m[i])
			if m_max == 0:
				if i==0:
					for k in range(i+1,numRow):
						i=k
						m_max2 = max(m[k])
						if m_max2 != 0
							break
						if i == numRow:
							return False
					#check First Column
					if m[i][0] = max(m[i]):
						i = i+1
						continue
					else:
						return False
				else:
					flagHead = i-1
					flagTail = -1
					for k in range (i+1,numRow):
						i=k
						m_max2 = max(m[k])
						if m_max2 != 0:
							flagTail = k
							break
					if flagTail == -1:	#Check Final Column
						if m[flagHead][numCol-1] == max(m[flagHead]):
							#return True
							break
					else:  #Check Head and Tail are consecutive siblings
						m_max3 = max(m[flagHead])
						m_max4 = max(m[flagTail])
						for x in range(0,numCol-1)
							if ((m[flagHead][x] = m_max3) and (m[flagHead][x+1] != m_max4)) or ((m[flagHead][x] != m_max3) and (m[flagHead][x+1] == m_max4)):
								return False
						i = i + 1
						continue
			for j in range(0,numCol):
				if m[i][j] = m_max:
					if m[i][j] == 1:
						return True
					else:
						checkInsert(w[i][j][1])
					break
	return True
options = dict(output_xhtml=1,
               clean=1, 
               drop_proprietary_attributes=1, 
               tidy_mark=0)                         
#file1 = str(tidy.parse('657534', **options))
# file2 = tidy.parse('657642', **options)

f = open('657534', 'r')
parser = etree.HTMLParser(remove_comments=True)
html = etree.HTML(f.read(), parser)
result = etree.tostring(html, pretty_print=True, method="xml")
events = "comment"

	#if action == "comment":
	#	elem.clear()
# print result


f = open('xxx', 'w')
f.write(result)
dom1 = parseString(result)

print dom1

#dom1 = parseString(str(file1))
#f = open('out.html', 'wb');
#f.write( cleaner.clean_html(lxml.html.tostring(file1)))
# f = open('657534', 'r')
# print tidy.parseString(f.read())
# a = lxml.html.tostring(lxml.html.parse('657534'))

# print tidy.parse('xxx')

# dom1 = parseString(a)

# print tidy.parseString(lxml.html.tostring(lxml.html.parse('657534')))
# print tidy.parseString(f.read())
# print tidy.parse('a')
# print tidy.parse('657534')

#root = dom.documentElement
#body = root.childNodes[0]
#t, w = SimpleTreeMatching(body.childNodes[0], body.childNodes[1])

#print AlignAndLink(w, body.childNodes[0], body.childNodes[1])