from xml.dom.minidom import parseString

def PutDataToTable(pattern, node):
    print pattern
    print node
    print "\n"
    if pattern.nodeType != node.nodeType:
        return None
    else:
        if node.nodeType == node.TEXT_NODE:
            return [node.data.encode('utf8')]
        else:
            if pattern.tagName != node.tagName:
                return None
            else:
                current = 0
                table = []
                for child in pattern.childNodes:
                    if child.hasAttribute('symbol'):
                        if child.getAttribute('symbol') == '?':
                            data = PutDataToTable(child, node.childNodes[current])
                            if data:
                                table = table + data
                                current = current + 1                              
                            
                        else:
                            data = []
                            for i in range(current, len(node.childNodes)):
                                item = PutDataToTable(child, node.childNodes[i])
                                if item:
                                    data = data + item
                                else:
                                    break                            
                            if child.getAttribute('symbol') == '+' and len(data) == 0:
                                return None
                            current = i
                            table.append(data)
                    else:
                        data = PutDataToTable(child, node.childNodes[current])
                        if data:
                            table = table + data
                            current = current + 1   
                        else:
                            return None
                return table
                            
pattern = parseString('<n1><n2 symbol="+"><t1>Name</t1><n5 symbol="+"><t5>Addr</t5><t6>Phone</t6><t7 symbol="?">Website</t7></n5></n2></n1>')     
dom = parseString('<n1><n2><t1>ABC company</t1><n5><t5>123 LTK Av.</t5><t6>0123456789</t6></n5><n5><t5>101 LD Blv</t5><t6>0908012034</t6><t7>www.abc.com</t7></n5></n2></n1>')         
print PutDataToTable(pattern.documentElement, dom.documentElement)
