import lxml.html
from lxml import etree

def func(tree, node1, node2):
	#print node1.tag + ' vs ' + node2.tag
	if node1.tag != node2.tag:
		return 0
	else:
		
		k = len(node1)
		n = len(node2)
		#print '%d vs %d' % (k, n)
		m = [[0]*(n+1)]*(k+1)
		for i in range (1, k+1):
			#print 'i = %d'%i
			for j in range (1, n+1):
				#print '\t j = %d'%j
				w = func(tree, node1[i-1], node2[j-1])
				if w == 1 and node1[i-1].text is not None and node2[j-1].text is not None:
					node1[i-1].attrib['link'] = tree.getpath(node2[j-1])
				m[i][j] = max( m[i][j-1], m[i-1][j], m[i-1][j-1]+w )
		print m
		return m[k][n] + 1
		

tree1 = lxml.html.parse('abc.html')
root1 = tree1.getroot()
tree2 = lxml.html.parse('xyz.html')
root2 = tree2.getroot()
root = etree.Element('root')
root.append(root1)
root.append(root2)
tree = etree.ElementTree(root)
print func(tree2, root2, root2)
#for node in root.iter():
#	if node.attrib.has_key('link'):
#		print tree.getpath(node) + ' link to ' + node.attrib['link']
