from xml.dom.minidom import parseString

def BreakRecord(list):
    if len(list) == 0:
        return [list]
    else:
        indices = [i for i, x in enumerate(list) if x == list[0]]
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
    
def PutDataToTable(records):
    records.sort()    
    records.reverse()
    i = 0
    while True:        
        pivot = 0
        item = records[pivot][i]
        for j in range(0, len(records)): 
            if len(records[j]) <= i:
                records[j].insert(i, 0)
            elif records[j][i] > 0:
                if item == 0:
                    pivot = j
                    item = records[j][i]            
                else:
                    if records[j][i] != item:
                        if item in records[j]:
                            for x in range(pivot, j):
                                if records[x][i] != records[j][i]:
                                    records[x].insert(i, 0)
                            pivot = j   
                        elif j == len(records)-1:
                            for x in range(pivot, j+1):
                                records[x].insert(i, 0)
            if j == len(records)-1:
                for x in range(0, j):
                    if records[x][i] != 0 and records[x][i] != records[pivot][i]:
                        records[x].insert(i, 0) 
        records.sort(key=lambda x: -len(x)) 
        i = i + 1
        if i == len(records[0]):
            break
    return records
            
def PutDataToTable2(records):
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
        
def checkEqual(lst):
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
                    record = record + r
                return record
            else:
                return ['' for i in GetTextNodeValue(pattern)]
                
#r = GenRecord([1, 2, 1, 2, 3, 5, 1, 2, 3, 4])
#records = [[(i, 0) for i in record] for record in r]
#print PutDataToTable2(records)
dom1 = parseString('<a><b></b><c><br/><s></s></c></a>')
dom2 = parseString('<a><b></b><c><s></s></c></a>')
#print GetTextNodeValue(dom.documentElement)
print GetDataRecord(dom1.documentElement, dom2.documentElement)