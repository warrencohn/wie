from xml.dom.minidom import parse, parseString
import lxml.html
from lxml.html.clean import Cleaner
from lxml import etree
#import tidy
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
    file.write('<html><head><meta charset="utf-8"></head><body><table style="border: 1px solid;border-collapse: collapse;">')
    x = [False for i in range(len(table))]
    for i in range(len(table[0])):
        file.write('<tr style="border: 1px solid;">')
        for j in range(len(table)):
            if table[j][i].nodeType == table[j][i].TEXT_NODE: # and (not table[j][i].data.isspace() )
                #if table[j][i].parentNode.tagName != 'style' and table[j][i].parentNode.tagName != 'script':
				file.write('<td style="border: 1px solid;">')
				file.write(table[j][i].data.encode('utf8'))
				file.write('</td>')
				x[j] = True
            # else:
                # if i > 0 and x[j]:
                #   file.write('<td style="border: 1px solid;">')
                #    file.write('</td>')
                
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
			m_max1 = max([m[i][j] for i in range(numRow)])
			if m_max1 == 0:
				flag1 = j
				if j == 0: #=> insert before first row
					for k in range(j+1,numCol):
						j = k
						m_max2 = max([m[i][k] for i in range(numRow)])
						if m_max2 != 0:
							if m[0][j] == m_max2:
								m_max1 = m_max2
								flag2 = k
								for x in range(flag1,flag2):
									#print Ti.childNodes
									#print Ts.childNodes
									tree = Ti.childNodes[x].cloneNode(True)
									Ts.insertBefore(tree,Ts.firstChild)
								return insertIntoSeed(Ts,Ti,SimpleTreeMatching(Ts, Ti)[1])
				else:
					m_max2 = max([m[i][flag1-1] for i in range(numRow)])
					m_max3 = -1
					if m[numRow-1][flag1-1] == m_max2 :
						for x in range(flag1,numCol):
							print Ts.childNodes
							tree = Ti.childNodes[x].cloneNode(True)
							Ts.appendChild(tree)
						return insertIntoSeed(Ts,Ti,SimpleTreeMatching(Ts, Ti)[1])
					else:
						flag2 = -1
						for k in range(j+1,numCol):
							j = k
							m_max3 = max([m[i][k] for i in range(numRow)])
							if m_max3 != 0:
								flag2 = k
								break
						if flag2 != -1:
							for i in range(0,numRow):
								if m[i][j] == m_max2:#Lay vi tri i 
									for x in range(flag1,flag2):
										#print Ti.childNodes
										#print Ts.childNodes
										tree = Ti.childNodes[x].cloneNode(True)
										Ts.insertBefore(tree,Ts.childNodes[i])
									return insertIntoSeed(Ts,Ti,SimpleTreeMatching(Ts, Ti)[1])
									m_max1 = m_max3
			for i in range(numRow):
				if m[i][j] == m_max1:
					if m[i][j] == 1:
						#return True
						break
					else:
						insertIntoSeed(Ts,Ti,w[i][j][1])
					break
			j = j + 1
					
	else:
		i = 0
		flagHead = -1
		flagTail = -1
		while(i<numRow):
			m_max = max(m[i])
			if m_max != 0:
				#print m_max
				for j in range(0,numCol):
					if m[i][j] == m_max:
						if (i == 0) & (j != 0):
							
							print "i = ",i
							print "j = ",j
							print "\n"
							for x in range(0,j):
								#print Ti.childNodes
								print Ts.childNodes
								tree = Ti.childNodes[x].cloneNode(True)
								Ts.insertBefore(tree,Ts.childNodes[i+x])
								
								
								print "spt = ",SimpleTreeMatching(Ts, Ti)[1]
								print "\n"
							return insertIntoSeed(Ts,Ti,SimpleTreeMatching(Ts, Ti)[1])
						else:							
							flagHead = j
							f = 0
							for k in range(i+1,numRow):
								i = k
								#print "k = ",k
								f = 1 #con row tiep theo
								m_max2 = max(m[k])
								if m_max2 != 0:
									#print "m_max2 = ",m_max2
									for x  in range(0,numCol):
										#print "i = ",i
										#print "x = ",x
										if m[i][x] == m_max2:
											#print x
											flagTail = x
											if flagHead != flagTail-1:
												for x in range(flagHead,flagTail):
													#print Ti.childNodes
													print Ts.childNodes
													tree = Ti.childNodes[x].cloneNode(True)
													Ts.insertBefore(tree,Ts.childNodes[i])
												return insertIntoSeed(Ts,Ti,SimpleTreeMatching(Ts, Ti)[1])
							if f != 1 :
								print "here"
								for x in range(flagHead+1,numCol):
									#print "flagHead = ",flagHead
									#print "x = ",x
									#print "here"
									#print Ti.childNodes
									print Ts.childNodes
									tree = Ti.childNodes[x].cloneNode(True)
									Ts.appendChild(tree)
								return insertIntoSeed(Ts,Ti,SimpleTreeMatching(Ts, Ti)[1])
							#print "here"
							#return insertIntoSeed(Ts,Ti,w[i][j][1])
			for j in range(0,numCol):
				if m[i][j] == m_max:
					if m[i][j] == 1:
						#return True
						break
					else:
						#print "here"
						insertIntoSeed(Ts,Ti,w[i][j][1])
					break
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
		while (j < numCol):
			
			m_max1 = max([m[i][j] for i in range(numRow)])
			#print "m_max1 = ",m_max1
			if (m_max1 != 0) & (j != 0):
				#kiem tra max truoc do co theo thu tu hay khong
				m_max0 = max([m[i][j-1] for i in range(numRow)])
				if m_max0 != 0:
					for x in range(numRow):
						if m[x][j-1] == m_max0:
							rowHead = x
						if m[x][j] == m_max1:
							rowTail = x
					if rowHead > rowTail:
						return False
			if m_max1 == 0:				
				if(j == 0):
					for k in range(j+1,numCol):
						#print k
						j = k
						m_max2 = max([m[i][k] for i in range(numRow)])
						if m_max2 != 0:	
							if m[0][j] == m_max2:
								m_max1 = m_max2
								break
							else:
								return False
						if k == (numCol-1):
							return False
				else:
					flagHead = j-1
					m_max2 = max([m[i][flagHead] for i in range(numRow)])
					m_max3 = -1
					if m[numRow-1][flagHead] == m_max2 :
						break #khong can de quy check tai vi tri nay ( vi da chay truoc do)
					else:
						flagTail = -1
						for k in range(j+1,numCol):
							j = k
							m_max3 = max([m[i][k] for i in range(numRow)])
							if m_max3 != 0:
								flagTail = k
								break
						if flagTail == -1: #Check Final Row
							return False	
						else: #Check Head and Tail are consecutive siblings
							for x in range(numRow):
								if ((m[x][flagHead] == m_max2) & (m[x+1][flagTail] != m_max3)) | ((m[x][flagHead] != m_max2) and (m[x+1][flagTail] == m_max3)):
									return False
								elif ((m[x][flagHead] == m_max2) & (m[x+1][flagTail] == m_max3)):
									break
							m_max1 = m_max3
			for i in range(numRow):
				if m[i][j] == m_max1:
					if m[i][j] == 1:
						break
					else:
						checkInsert(w[i][j][1])
					break
			j = j + 1
								
	else:	# numCol > numRow
		i = 0
		while (i < numRow):
			m_max1 = max(m[i])
			#print "m_max1 = ",m_max1
			if (m_max1 != 0) & (i != 0) :
				#kiem tra max truoc do co theo thu tu hay khong
				m_max0 = max(m[i-1])
				if m_max0 != 0:
					for x in range(numCol):
						if m[i-1][x] == m_max0:
							rowHead = x
						if m[i][x] == m_max1:
							rowTail = x
					if rowHead > rowTail:
						return False
			if m_max1 == 0:
				if(i == 0):
					for k in range(i+1,numRow):
						#print k
						i = k
						m_max2 = max(m[i])
						if m_max2 != 0:	
							if m[i][0] == m_max2:
								m_max1 = m_max2
								break
							else:
								return False
						if k == (numRow-1):
							return False
				else:
					flagHead = i-1
					m_max2 = max(m[flagHead])
					m_max3 = -1
					if m[flagHead][numCol-1] == m_max2 :
						break #khong can de quy check tai vi tri nay ( vi da chay truoc do)
					else:
						flagTail = -1
						for k in range(i+1,numRow):
							i = k
							m_max3 = max(m[i])
							if m_max3 != 0:
								flagTail = k
								break
						if flagTail == -1: #Check Final Row
							return False	
						else: #Check Head and Tail are consecutive siblings
							for x in range(numCol):
								if ((m[flagHead][x] == m_max2) & (m[flagTail][x+1] != m_max3)) | ((m[flagHead][x] != m_max2) and (m[flagTail][x+1] == m_max3)):
									return False
								elif ((m[flagHead][x] == m_max2) & (m[flagTail][x+1] == m_max3)):
									break
							m_max1 = m_max3
			for j in range(numCol):
				if m[i][j] == m_max1:
					if m[i][j] == 1:
						break
					else:
						checkInsert(w[i][j][1])
					break
			i = i + 1
	return True