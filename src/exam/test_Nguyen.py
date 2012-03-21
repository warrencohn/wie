import new
f1 = open('data/657534', 'r')
f2 = open('data/657642', 'r')
parser = etree.HTMLParser(recover=True, remove_blank_text=True, remove_comments=True)

html1 = etree.HTML(f1.read(), parser)
html2 = etree.HTML(f2.read(), parser)
result1 = etree.tostring(html1, pretty_print=True, method="xml")
result2 = etree.tostring(html2, pretty_print=True,method="xml")

dom1 = parseString(result1)
dom2 = parseString(result2)

body1 = dom1.getElementsByTagName('body')[0]
body2 = dom2.getElementsByTagName('body')[0]

t, w = SimpleTreeMatching(dom1.documentElement, dom2.documentElement)

tbl = AlignAndLink(w, dom1.documentElement, dom2.documentElement)
printTable('out.html', tbl)