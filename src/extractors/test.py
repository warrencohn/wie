from net import Match, GetDataRecord, GenRecords, TraverseAndMatch
from xml.dom.minidom import parseString
def a(node):
    b = node.childNodes[-1].cloneNode(False)
    node.appendChild(b)
dom = parseString('<html><a><h1></h1><p><h2></h2><h3></h3><h4></h4></p><p><h2></h2><h3></h3></p></a><a><h1></h1><p><h2></h2><h3></h3></p></a></html>')
#dom = parseString('<html>a3<b>abc</b>a1<b>xyz</b>a2<c></c><a>1</a><a>2</a></html>')
#print dom.documentElement.toxml()
#print Match(dom.documentElement, 0.5)
#print GetDataRecord(dom.documentElement.childNodes[0], dom.documentElement.childNodes[1])
print TraverseAndMatch(dom.documentElement,  0.5)
#print Match(dom.documentElement,[[],[],[],[],[],[],[],[]],  0.5)

