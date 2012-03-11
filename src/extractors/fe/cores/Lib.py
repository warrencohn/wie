'''
Created on Mar 11, 2012

@author: LeHung
'''
import lxml.html
from lxml import etree

debugMode = False

# index matching table
mtcMatrix = None

# the number of right childrens
nRow = 0

# hash key table for first children(compared children)
mtcKey = {}

def echo(str):
    if(debugMode == False):
        print str,

def AlignAndLink():
    echo('@mtcMatrix: \n')
    if(mtcMatrix == None):
        echo('None')
        return
    for i in range(0, len(mtcMatrix)):
        for j in range(0, len(mtcMatrix[i])):
            if mtcMatrix[i][j] != '':
                #echo('1')
                echo(mtcMatrix[i][j])
            else: 
                echo('0')
        echo('\n')
    echo('--\n')




def GenNodePattern(child):
    pass

def Match(Node, t):
    num = len(Node)
    for i in range(1, num + 1):
        # ChildFirst := select and remove the first child from  Children; 
        for j in range (i, num + 1):#for each  ChildR  in  Children  do 
            # initDict(root, tree)
            if Node[j].has_key('isTraveled') and Node[j].attrib['isTraveled'] == 1:
                continue
            
            if TreeMatch(Node, Node[i], Node[j]) > t:
                AlignAndLink()
                Node[j].attrib['isTraveled'] = 1
                
        # if some alignments (or links) have been made with  ChildFirst then  
        if(Node[i].has_key['isLinked']):
            GenNodePattern(Node[i])

# generate a hash key table, and matching matrix
def initDict(root, tree):
    global mtcMatrix
    #echo('@Indexing..\n')
    i = 0
    for node in root.iter():
        mtcKey[tree.getpath(node)] = i
        #echo(tree.getpath(node) + ' > %d\n' % i)
        i = i + 1
    #echo('Total indexed elements: %d\n' % len(mtcKey))
    mtcMatrix = [[''] * len(mtcKey)] * (len (tree.getroot()) - 1)
    #echo('init mtcMatrix: ')
    #echo(mtcMatrix)
    #echo('\n')
    #return mtcMatrix

def TreeMatch(tree, node1, node2):
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
                w = TreeMatch(tree, node1[i-1], node2[j-1])
                if w == 1 and node1[i-1].text is not None and node2[j-1].text is not None:
                    node1[i-1].attrib['link'] = tree.getpath(node2[j-1])
                    
                    index = mtcKey[tree.getpath(node1[i-1])]

                    mtcMatrix[nRow][index] = tree.getpath(node2[j-1])
                    
                m[i][j] = max( m[i][j-1], m[i-1][j], m[i-1][j-1]+w )

        # print m
        return m[k][n] + 1
        

tree1 = lxml.html.parse('abc.html')
root1 = tree1.getroot()
tree2 = lxml.html.parse('xyz.html')
root2 = tree2.getroot()
root = etree.Element('root')
root.append(root1)
root.append(root2)
tree = etree.ElementTree(root)


initDict(root1, tree)


TreeMatch(tree, root1, root2)

#AlignAndLink()

print mtcMatrix
#for node in root.iter():
 #   if node.attrib.has_key('link'):
  #      print tree.getpath(node) + ' link to ' + node.attrib['link']
                