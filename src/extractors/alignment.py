from matching import SimpleTreeMatching

def PartialTreeAlignment(S):
    Ts = S[0]
    S.remove(Ts)
    R = []
    while (S != []):
        Ti = S[0]
        S.remove(Ti)
        w = SimpleTreeMatching(Ts,Ti)
        if w[0] > 0:
            if len(w[1]) > 0:
                seed = InsertIntoSeed(w[1],Ts,Ti)
            else:
                seed = Ts
        else:
            seed = None
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
        if lastMatch != -1:
            if (lastMatch+1) == numCol:
                for x in range(match[lastMatch]+1, numRow):
                    seed.appendChild(node1.childNodes[x].cloneNode(True)) 
            elif (match[lastMatch]+1) == numRow:
                for x in range(lastMatch+1, numCol):
                    seed.appendChild(node2.childNodes[x].cloneNode(True))
            else:
                return None 
        else:
            for x in range(numRow):
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
        if lastMatch != -1:
            if (lastMatch+1) == numRow:
                for x in range(match[lastMatch]+1, numCol):
                    seed.appendChild(node2.childNodes[x].cloneNode(True)) 
            elif (match[lastMatch]+1) == numCol:
                for x in range(lastMatch+1, numRow):
                    seed.appendChild(node1.childNodes[x].cloneNode(True))
            else:
                return None
        else:
            for x in range(numCol):
                seed.appendChild(node2.childNodes[x].cloneNode(True))
    return seed