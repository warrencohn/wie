import lxml.html

def func(node1, node2):
	#print node1.tag + ' vs ' + node2.tag
	if node1.tag != node2.tag:
		return 0
	else:
		
		k = len(node1)
		n = len(node2)
		print '%d vs %d' % (k, n)
		m = [[0]*(k+1)]*(n+1)
		for i in range (1, k+1):
			print 'i = %d'%i
			for j in range (1, n+1):
				print '\t j = %d'%j
				w = func(node1[i-1], node2[j-1])
				m[i][j] = max( m[i][j-1], m[i-1][j], m[i-1][j-1]+w )
		return m[k][n] + 1
		

tree1 = lxml.html.parse('abc.html')
root1 = tree1.getroot()
tree2 = lxml.html.parse('xyz.html')
root2 = tree2.getroot()
print func(root1, root2)