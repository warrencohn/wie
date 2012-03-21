from xml.dom.minidom import parse, parseString
import lxml.html
from lxml.html.clean import Cleaner
from lxml import etree
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
    
    table = []
    numRow = len(m)
    numCol = len(m[0])
    if numCol < numRow:
        for i in range(0, numCol):
            m_max = max([m[j][i] for j in range(numRow)])
            if m_max == 0 :
                break
            for j in range(0, numRow):
                if m[j][i] == m_max:
                    if m[j][i] == 1:
                        table.append([node1.childNodes[j], node2.childNodes[i]])
                    else:
                        table += AlignAndLink(w[j][i][1], node1.childNodes[j], node2.childNodes[i])
                    break
    else:
        for i in range(0, numRow):
            m_max = max(m[i])
            if m_max == 0:
                break
            for j in range(0, numCol):
                if m[i][j] == m_max:
                    if m[i][j] == 1:
                        table.append([node1.childNodes[i], node2.childNodes[j]])
                    else:
                        table += AlignAndLink(w[i][j][1], node1.childNodes[i], node2.childNodes[j])
                    break
    return table    
                         
def printTable(filename, table):
    file = open(filename, 'w')
    file.write('<html><head><meta charset="utf-8"></head><body><table style="border: 1px solid;">')
    x = [False for i in range(len(table))]
    for i in range(len(table[0])):
        file.write('<tr style="border: 1px solid;">')
        for j in range(len(table)):
            if table[j][i].nodeType == table[j][i].TEXT_NODE and (not table[j][i].data.isspace() ):
                if table[j][i].parentNode.tagName != 'style' and table[j][i].parentNode.tagName != 'script':
                    file.write('<td style="border: 1px solid;">')
                    file.write(table[j][i].data.encode('utf8'))
                    file.write('</td>')
                    x[j] = True
            else:
                if i > 0 and x[j]:
                    file.write('<td style="border: 1px solid;">')
                    file.write('</td>')
                
        file.write('</tr>')
    file.write('</table></body></html>')
    
def cleanHTML(dom):    
    clean_recursive(dom.documentElement)
    
def clean_recursive(node):
    #child = node.lastChild
    for i in range(len(node.childNodes)):
        
        child = node.childNodes[i]
        print child
        if child.nodeType == child.ELEMENT_NODE:
            #print child.tagName
            if child.tagName.lower() == 'script' or child.tagName.lower() == 'style':
                
                node.removeChild(child)
                node.unlink()
            else:
                clean_recursive(child)
        elif child.nodeType == child.TEXT_NODE:
            #print "node data"
            if child.data.isspace() or (len(child.data) == 0):
                
                node.removeChild(child)
                node.unlink()
        
        
        

def partialTreeAlignment(S,w):
	Ts = S.childNodes[0]
	S.removeChild(Ts)
	Document.createElement(R)
	while (S.hasChildNodes()):
		Ti = S.childNodes[0]
		S.removeChild(Ti)
		temp = []
		if (checkInsert(w)):
			insertIntoSeed(Ts,Ti,w)
			S = S + R
			R = [[]]
		else :
			R.insert(len(R),Ti)
	return Ts
def insertIntoSeed(Ts,Ti,w):
	m = [[x for x, y in row] for row in w]
	numRow = len(m)
	numCol = len(m[0])
	if numCol <= numRow:
		flag1 = -1
		flag2 = -1
		j = 0
		while (j < numCol):
			m_max = max([m[i][j] for i in range(numRow)])
			if m_max == 0:
				flag1 = j
				if j == 0: #=> insert before first row
					for k in range(j+1,numCol):
						j = k
						m_max2 = max([m[i][k] for i in range(numRow)])
						if m_max2 != 0:
							flag2 = k
							for x in range(flag1,flag2):
								Ts.insertBefore(Ti.childNodes[x],Ts.firstChild)
							return insertIntoSeed(Ts,Ti,SimpleTreeMatching(Ts, Ti)[1])
					j = j + 1
					continue
				else:
					for k in range(j+1,numCol):
						j = k
						m_max2 = max([m[i][k] for i in range(numRow)])
						if m_max2 != 0:
							flag2 = k
							for i in range(0,numRow):
								if m[i][j] == m_max2:
									for x in range(flag1,flag2):
										Ts.insertBefore(Ti.childNodes[x],Ts.childNodes[i])
									return insertIntoSeed(Ts,Ti,SimpleTreeMatching(Ts, Ti)[1])
					j = j + 1
					continue
			for i in range(0,numRow):
				if m[i][j] == m_max:
					if m[i][j] == 1:
						#return True
						break
					else:
						insertIntroSeed(Ts,Ti,w[i][j][1])
					break
			j = j + 1
					
	else:
		i = 0
		flagHead = -1
		flagTail = -1
		while(i<numRow):
			m_max = max(m[i])
			if m_max != 0:
				for j in range(0,numCol):
					if m[i][j] == m_max:
						flagHead = j
						if m[i][j] == 1:
							#return True
							break 
						elif i == 0:
							break
						else:
							for k in range(i+1,numRow):
								m_max2 = max(m[k])
								if m_max2 != 0:
									for x  in range(0,numCol):
										if m[i][x] == m_max2:
											flagTail = x
											for x in range(flagHead,flagTail):
												Ts.insertBefore(Ti.childNodes[x],Ts.childNodes[i])
											return insertIntoSeed(Ts,Ti,SimpleTreeMatching(Ts, Ti)[1])
						insertIntroSeed(Ts,Ti,w[i][j][1])
			i = i + 1
	return Ts	

def checkInsert(w):
	m = [[x for x, y in row] for row in w]
	numRow = len(m)
	#print m
	numCol = len(m[0])
	#print numCol
	if numCol <= numRow:
		j = 0 
		#for j in range(0, numCol):
		while (j < numCol):
			m_max1 = max([m[i][j] for i in range(numRow)])
			#print "m_max1 = ",m_max1
			if m_max1 == 0:
				if(j == 0):
					for k in range(j+1,numCol):
						#print k
						j = k
						m_max2 = max([m[i][k] for i in range(numRow)])
						if m_max2 != 0:	
							break
					if j == (numCol-1):
						return False
					#check First Row
					if m[0][j] == max([m[i][j] for i in range(numRow)]) :
						#return False
						j = j + 1
						continue
					else:
						return False
				else:
					flagHead = j-1
					#print "flagHead = ",flagHead
					flagTail = -1
					for k in range(j+1,numCol):
						j = k
						print "j = ",j
						m_max2 = max([m[i][k] for i in range(numRow)])
						if m_max2 != 0:
							flagTail = k
							#print "flagTail = ",flagTail
							break
					if flagTail == -1: #Check Final Row
						#print "here"
						if m[numRow-1][flagHead] == max([m[i][flagHead] for i in range(numRow)]) :
							#return True
							break;
					else: #Check Head and Tail are consecutive siblings
						m_max3 = max([m[i][flagHead] for i in range(numRow)])
						m_max4 = max([m[i][flagTail] for i in range(numRow)])
						#print "m_max3 = ",m_max3
						#print "m_max4 = ",m_max4
						for x in range(0,numRow):
							#print "m[%d][flagHead] =%d"%(x,m[x][flagHead])
							#print "m[%d][flagTail] =%d"%(x+1,m[x+1][flagTail])
							if ((m[x][flagHead] == m_max3) & (m[x+1][flagTail] != m_max4)) | ((m[x][flagHead] != m_max3) and (m[x+1][flagTail] == m_max4)):
								#print "here"
								return False
							elif ((m[x][flagHead] == m_max3) & (m[x+1][flagTail] == m_max4)):
								break
					j = j + 1
					continue
			for i in range(0,numRow):
				if m[i][j] == m_max1:
					if m[i][j] == 1:
						#return True
						break
					else:
						checkInsert(w[i][j][1])
					break
			j = j + 1
								
	else:	# numCol > numRow
		i = 0
		flagHead = -1
		flagTail = -1
		while(i<numRow):
			m_max = max(m[i])
			if m_max != 0:
				for j in range(0,numCol):
					if m[i][j] == m_max:
						flagHead = j
						if m[i][j] == 1:
							#return True
							break 
						elif i == 0:
							break
						else:
							for k in range(i+1,numRow):
								m_max2 = max(m[k])
								if m_max2 != 0:
									for x  in range(0,numCol):
										if m[i][x] == m_max2:
											flagTail = x
											if flagTail > flagHead:
												return False
						checkInsert(w[i][j][1])
			i = i + 1
	return True		
        
f1 = open('data/657534', 'r')
f2 = open('data/657642', 'r')
parser = etree.HTMLParser(recover=True, remove_blank_text=True, remove_comments=True)

html1 = etree.HTML(f1.read(), parser)
html2 = etree.HTML(f2.read(), parser)
result1 = etree.tostring(html1, pretty_print=True, method="xml")
result2 = etree.tostring(html2, pretty_print=True,method="xml")

dom1 = parseString(result1)
dom2 = parseString(result2)

body1 = dom1.getElementsByTagName('body')[0]
body2 = dom2.getElementsByTagName('body')[0]

t, w = SimpleTreeMatching(dom1.documentElement, dom2.documentElement)

tbl = AlignAndLink(w, dom1.documentElement, dom2.documentElement)
printTable('out.html', tbl)
if checkInsert(w) == True:
	print "Function checkInsert returns True"
else:
	print "Function checkInsert returns False"

print insertIntoSeed(dom1.documentElement,dom2.documentElement,w).childNodes
	
for m in w: 
	print m