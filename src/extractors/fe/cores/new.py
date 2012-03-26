from xml.dom.minidom import Document, parse, parseString
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

def Match(Node,t):
    Children = []
    for i in range(Node.childNodes.length):
        Children.append(Node.childNodes[i])
    root = Document()
    while (Children != []) :
        ChildFirst = Children[0]
        S = []
        S.append(ChildFirst)
        Children.remove(ChildFirst)
        for ChildR in Children:
            if TreeMatch(ChildFirst,ChildR) > t:
                S.append(ChildR)
                Children.remove(ChildR)
        root.appendChild(PartialTreeAlignment(S))
        break
    return GenRecordPattern(root)            

def GenRecordPattern(Node):
    for subNode in Node.chilNodes:
        
    
def TreeMatch(Node1,Node2):
    m = SimpleTreeMatching(Node1,Node2)[0]
    return m/((Nodes(Node1)+Nodes(Node2))/2.0 + 1)

def Nodes(Node):
    count = Node.childNodes.length
    for subNode in Node.childNodes:
        count = count + Nodes(subNode)
    return count
 
def PartialTreeAlignment(S):
    Ts = S[0]
    S.remove(Ts)
    R = []
    while (S != []):
        Ti = S[0]
        S.remove(Ti)
        w = SimpleTreeMatching(Ts,Ti)[1]
        seed = InsertIntoSeed(w,Ts,Ti)
        if seed:
            Ts = seed
            S = S + R
            R = []
        else :
            R.append(Ti)
    return Ts

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
                continue
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
                                node1.childNodes[x].setAttribute("key","?")
                                seed.appendChild(node1.childNodes[x].cloneNode(True))                                
                        elif j == (matchRow+1):
                            for x in range(p+1, i):
                                node2.childNodes[x].setAttribute("key","?")
                                seed.appendChild(node2.childNodes[x].cloneNode(True))
                        else:
                            return None
                    if len(w[j][i][1]) == 0:   
                        seed.appendChild(node1.childNodes[j].cloneNode(False))
                    else:                        
                        child = InsertIntoSeed(w[j][i][1], node1.childNodes[j], node2.childNodes[i])
                        if child:
                            child.toprettyxml()
                            seed.appendChild(child)
                        else:
                            return None
                    break
        lastMatch = GetPreMatch(match, numCol)
        if lastMatch != -1:
            if (lastMatch+1) == numCol:
                for x in range(match[lastMatch]+1, numRow):
                    node1.childNodes[x].setAttribute("key","?")
                    seed.appendChild(node1.childNodes[x].cloneNode(True)) 
            elif (match[lastMatch]+1) == numRow:
                for x in range(lastMatch+1, numCol):
                    node2.childNodes[x].setAttribute("key","?")
                    seed.appendChild(node2.childNodes[x].cloneNode(True))
            else:
                return None 
        else:
            for x in range(numRow):
                node1.childNodes[x].setAttribute("key","?")
                seed.appendChild(node1.childNodes[x].cloneNode(True))
    else:
        match = [-1 for i in range(0, numRow)]
        for i in range(0, numRow):
            m_max = max(m[i])
            if m_max == 0:
                continue
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
                                node2.childNodes[x].setAttribute("key","?")
                                seed.appendChild(node2.childNodes[x].cloneNode(True))                                
                        elif j == (matchCol+1):
                            for x in range(p+1, i):
                                node1.childNodes[x].setAttribute("key","?")
                                seed.appendChild(node1.childNodes[x].cloneNode(True))
                        else:
                            return None
                    if len(w[i][j][1]) == 0:
                        seed.appendChild(node1.childNodes[i].cloneNode(False))
                    else:
                        child = InsertIntoSeed(w[i][j][1], node1.childNodes[i], node2.childNodes[j])
                        if child:
                            child.toprettyxml()
                            seed.appendChild(child)
                        else:
                            return None
                    break        
        lastMatch = GetPreMatch(match, numRow)
        if lastMatch != -1:
            if (lastMatch+1) == numRow:
                for x in range(match[lastMatch]+1, numCol):
                    node2.childNodes[x].setAttribute("key","?")
                    seed.appendChild(node2.childNodes[x].cloneNode(True)) 
            elif (match[lastMatch]+1) == numCol:
                for x in range(lastMatch+1, numRow):
                    node1.childNodes[x].setAttribute("key","?")
                    seed.appendChild(node1.childNodes[x].cloneNode(True))
            else:
                return None
        else:
            for x in range(numCol):
                node2.childNodes[x].setAttribute("key","option")
                seed.appendChild(node2.childNodes[x].cloneNode(True))
    return seed