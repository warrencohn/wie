from xml.dom.minidom import parse, parseString
import lxml.html
from lxml.html.clean import Cleaner
import tidy

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
            if m_max == 0:
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
                         
#options = dict(output_xhtml=1, 
#               clean=1, 
#               drop_proprietary_attributes=1, 
#               tidy_mark=0)                         
#file1 = tidy.parse('657534', **options)
#file2 = tidy.parse('657642', **options)

#dom1 = parseString(str(file1))
#f = open('out.html', 'wb');
#f.write( cleaner.clean_html(lxml.html.tostring(file1)))
#f = open('657534', 'r')
#print tidy.parseString(f.read()).writexml()
dom = parse('xyz.html')
root = dom.documentElement
body = root.childNodes[0]
t, w = SimpleTreeMatching(body.childNodes[0], body.childNodes[1])

print AlignAndLink(w, body.childNodes[0], body.childNodes[1])