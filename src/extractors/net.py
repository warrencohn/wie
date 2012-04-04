from matching import TreeMatch
from alignment import PartialTreeAlignment

def BreakRecord(list):
    if len(list) == 0:
        return [list]
    else:
        indices = [i for i, x in enumerate(list) if x[0] == list[0][0]]
        if len(indices) > 1:
            result = []
            for i, x in enumerate(indices):
                if i == len(indices) - 1:
                    result.append(list[indices[i]:])
                else:
                    result.append(list[indices[i]:indices[i+1]])
            return result
        else:
            return [list]
        
def GenRecord(data):
    result = []
    rs = BreakRecord(data)
    if len(rs) > 1:
        for r in rs:
            items = GenRecord(r[1:])
            result.append(r[0:1] + items[0])
            if len(items) > 1:
                for i in items[1:]:
                    result.append(i)        
        return result
    else:
        return [data]
        
def GenRecords(list):
    records = []
    for i in range(0, len(list)):        
        if list[i] > -1:
            if i == 0  or list[i-1] == -1:
                records.append([])
            records[-1].append((list[i], i))
    return records
            
def PutDataToTable(records):
    records.sort(key=lambda x: x[0])   
    records.reverse()
    i = 0
    while True:    
        pivot = 0
        item = records[pivot][i][0]
        for j in range(0, len(records)): 
            if len(records[j]) <= i:
                records[j].insert(i, (-1, -1))
            elif records[j][i] > -1:
                if item == -1:
                    pivot = j
                    item = records[j][i][0]            
                else:
                    if records[j][i][0] != item:
                        if item in records[j]:
                            for x in range(pivot, j):
                                if records[x][i][0] != records[j][i][0]:
                                    records[x].insert(i, (-1, -1))
                            pivot = j   
                        elif j == len(records)-1:
                            for x in range(pivot, j+1):
                                records[x].insert(i, (-1, -1))
            if j == len(records)-1:
                for x in range(0, j):
                    if records[x][i][0] != -1 and records[x][i][0] != records[pivot][i][0]:
                        records[x].insert(i, (-1, -1)) 
        records.sort(key=lambda x: -len(x)) 
        i = i + 1
        if i == len(records[0]):
            break
    return records   

def GetTextNodeValue(node):
    if node.nodeType == node.TEXT_NODE:
        return [node.data]
    else:
        texts = []
        for child in node.childNodes:
            texts = texts + GetTextNodeValue(child)
        return texts
        
def CheckEqual(lst):
       return lst[1:] == lst[:-1]
       
def GetDataRecord(pattern, node):
    if pattern.nodeType != node.nodeType:
        return ['' for i in GetTextNodeValue(pattern)]
    else:
        if node.nodeType == node.TEXT_NODE:
            return [node.data]
        else:
            if pattern.tagName == node.tagName:            
                record = []
                j = 0
                for i in range(0, len(pattern.childNodes)):
                    if j >= len(node.childNodes):
                        r = ['' for i in GetTextNodeValue(pattern.childNodes[i])]
                    else:
                        if pattern.childNodes[i].nodeType != node.childNodes[j].nodeType:
                            r = ['' for i in GetTextNodeValue(pattern.childNodes[i])]
                        elif node.childNodes[j].nodeType == node.childNodes[j].ELEMENT_NODE and pattern.childNodes[i].tagName != node.childNodes[j].tagName:
                            r = ['' for i in GetTextNodeValue(pattern.childNodes[i])]
                        else:
                            r = GetDataRecord(pattern.childNodes[i], node.childNodes[j])
                            j = j + 1
                    record = record + r
                return record
            else:
                return ['' for i in GetTextNodeValue(pattern)]    
        
def Match1(node, nodeData, t):
    children = []
    patterns = []
    patternList = []
    for i in range(len(node.childNodes)):
        children.append(node.childNodes[i])
        patternList.append(-1)
    
    while (children != []) :
        ChildFirst = children[0]
        S = []
        S.append(ChildFirst)
        children.remove(ChildFirst)
        for ChildR in children:
            if TreeMatch(ChildFirst,ChildR) > t:
                S.append(ChildR)
                children.remove(ChildR)
        patterns.append(PartialTreeAlignment(S[:]))
        for n in S:     
            patternList[node.childNodes.index(n)] = len(patterns) - 1 
    recordList = GenRecord(patternList)
    index = 0
    for i, x in enumerate(recordList):
        for j, y in enumerate(x):
            recordList[i][j] = (recordList[i][j], index)
            index = index + 1
    recordTable = PutDataToTable(recordList)
    patternChildren = []
    for i in range(0, len(recordTable[0])):
        for j in range(0, len(recordTable)):
            if recordTable[j][i][0] != -1:
                patternChildren.append(recordTable[j][i][0])
                break
    dataTable = []
    for i in range(0, len(recordTable[0])):
        patternData = GetTextNodeValue(patterns[patternChildren[i]])
        if len(patternData) == 0 or (CheckEqual(patternData) and patternData[0] == ''):
            continue        
        for j in range(0, len(recordTable)):
            dataRecord = []
            if recordTable[j][i][0] == -1:
                dataRecord = dataRecord + patternData
            else:
                row = GetDataRecord(patterns[patternChildren[i]], node.childNodes[recordTable[j][i][1]])  
                if len(nodeData[recordTable[j][i][1]]) > 1:
                    x = 0
                    for i, item in enumerate(row):
                        if item == '':
                            for d in nodeData[recordTable[j][i][1]]:
                                d.insert(i, item)
                    for d in nodeData:
                        dataRecord = dataRecord + d
                            
                else:
                    dataRecord = dataRecord + row         
            dataTable.append(dataRecord)
    if len(patterns) != len(node.childNodes):
        for i in range(0, len(node.childNodes)):
            n = node.childNodes[0]
            node.removeChild(n)
            n.unlink()
        for p in patterns:
            node.appendChild(p)
    return dataTable

def Match(node, nodeData, t):
    print node
    children = []
    patterns = []
    patternList = []
    for i in range(len(node.childNodes)):
        children.append(node.childNodes[i])
        patternList.append(-1)
    
    while (children != []) :
        ChildFirst = children[0]
        S = []
        S.append(ChildFirst)
        children.remove(ChildFirst)
        for ChildR in children:
            if TreeMatch(ChildFirst,ChildR) > t:
                S.append(ChildR)
                children.remove(ChildR)
        s = PartialTreeAlignment(S[:])
        patterns.append(s)
        print s.toxml()
        if len(S) > 1:            
            for n in S:     
                patternList[node.childNodes.index(n)] = len(patterns) - 1 
    recordList = GenRecords(patternList)
    print recordList
    tblList = []
    for r in recordList:
        if len(r) > 1:
            rl = GenRecord(r)
            print rl
            recordTable = PutDataToTable(rl)
            print recordTable
            patternChildren = []
            for i in range(0, len(recordTable[0])):
                for j in range(0, len(recordTable)):
                    if recordTable[j][i][0] != -1:
                        patternChildren.append(recordTable[j][i][0])
                        break
            print patternChildren
            dataTable = []
            for i in range(0, len(recordTable)):
                   
                dataRecord = []
                for j in range(0, len(recordTable[0])): 
                    patternData = GetTextNodeValue(patterns[patternChildren[j]])
                    if len(patternData) == 0 or (CheckEqual(patternData) and patternData[0] == ''):
                        continue 
                    if recordTable[i][j][0] == -1:
                        dataRecord = dataRecord + ['' for x in patternData]
                    else:
                        row = GetDataRecord(patterns[patternChildren[j]], node.childNodes[recordTable[i][j][1]])  
                        #print row
                        if len(nodeData[recordTable[i][j][1]]) > 0:
                            dataRecord.append(nodeData[recordTable[i][j][1]])
                                    
                        else:
                            dataRecord = dataRecord + row
                print dataRecord
                dataTable.append(dataRecord)
            tblList.append(dataTable)
    # chua xu ly truong hop cac record lien ke  
    print patterns
    if len(patterns) != len(node.childNodes):
        for i in range(0, len(node.childNodes)):
            n = node.childNodes[0]
            node.removeChild(n)
            n.unlink()
        print "node " + node.toxml()
        for p in patterns:
            node.appendChild(p)
            print node.toxml()
    print str(node) + " - " + node.toxml()
    return tblList

def TraverseAndMatch(node, t):
    nodeData = []
    for i in range(0, len(node.childNodes)):
        nodeData.append(TraverseAndMatch(node.childNodes[i], t))
    return Match(node, nodeData, t)
        