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
			
def GetPreMatch(matchList, current):
    prematch = -1
    for x in reversed(range(0, current)):
        if matchList[x] != -1:
            prematch = x
            break
    return prematch

def InsertIntoSeed(w, node1, node2):
    m = [[x for x, y in row] for row in w]   
    
    seed = node1.cloneNode(False)
    numRow = len(m)
    numCol = len(m[0])
    
    if numCol < numRow:
        match = [-1 for i in range(0, numCol)]
        for i in range(0, numCol):
            m_max = max([m[j][i] for j in range(numRow)])
            if m_max == 0 :
                break
            for j in range(0, numRow):
                if m[j][i] == m_max:
                    if j in match:
                        continue
                    else:
                        match[i] = j                    
                    p = GetPreMatch(match, i)
                    if p != -1 and match[p] >= j:
                        return None
                    else:
                        if p == -1:
                            matchRow = -1
                        else:
                            matchRow = match[p]
                        if i == (p+1):
                            for x in range(matchRow+1, j):
                                seed.appendChild(node1.childNodes[x].cloneNode(True))                                
                        elif j == (matchRow+1):
                            for x in range(p+1, i):
                                seed.appendChild(node2.childNodes[x].cloneNode(True))
                        else:
                            return None
                    if len(w[j][i][1]) == 0:   
                        seed.appendChild(node1.childNodes[j].cloneNode(False))
                    else:                        
                        child = InsertIntoSeed(w[j][i][1], node1.childNodes[j], node2.childNodes[i])
                        if child:
                            seed.appendChild(child)
                        else:
                            return None
                    break
        lastMatch = GetPreMatch(match, numCol)
        if (lastMatch+1) == numCol:
            for x in range(match[lastMatch]+1, numRow):
                seed.appendChild(node1.childNodes[x].cloneNode(True)) 
        elif (match[lastMatch]+1) == numRow:
            for x in range(lastMatch+1, numCol):
                seed.appendChild(node2.childNodes[x].cloneNode(True))
        else:
            return None
    else:
        match = [-1 for i in range(0, numRow)]
        for i in range(0, numRow):
            m_max = max(m[i])
            if m_max == 0:
                break
            for j in range(0, numCol):
                if m[i][j] == m_max:
                    if j in match:
                        continue
                    else:
                        match[i] = j   
                    p = GetPreMatch(match, i)                        
                    if p != -1 and match[p] >= j:
                        return None
                    else:
                        if p == -1:
                            matchCol = -1
                        else:
                            matchCol = match[p]
                        if i == (p+1):
                            for x in range(matchCol+1, j):
                                seed.appendChild(node2.childNodes[x].cloneNode(True))                                
                        elif j == (matchCol+1):
                            for x in range(p+1, i):
                                seed.appendChild(node1.childNodes[x].cloneNode(True))
                        else:
                            return None
                    if len(w[i][j][1]) == 0:
                        seed.appendChild(node1.childNodes[i].cloneNode(False))
                    else:
                        child = InsertIntoSeed(w[i][j][1], node1.childNodes[i], node2.childNodes[j])
                        if child:
                            seed.appendChild(child)
                        else:
                            return None
                    break        
        lastMatch = GetPreMatch(match, numRow)
        if (lastMatch+1) == numRow:
            for x in range(match[lastMatch]+1, numCol):
                seed.appendChild(node2.childNodes[x].cloneNode(True)) 
        elif (match[lastMatch]+1) == numCol:
            for x in range(lastMatch+1, numRow):
                seed.appendChild(node1.childNodes[x].cloneNode(True))
        else:
            return None
    return seed   
    
dom1 = parseString('<a name="abc">sas<b>dsfsf</b><c>sffsf</c>fgd</a>')
m, w = SimpleTreeMatching(dom1.documentElement, dom1.documentElement)

seed = InsertIntoSeed(w, dom1.documentElement, dom1.documentElement)
print seed.toprettyxml()