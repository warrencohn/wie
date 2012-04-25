# coding=utf-8
from numpy import array
from urlparse import urlsplit
import re

def createInput(filename):
	f = open(filename, 'r')
	input = []
	for line in f.readlines():
		p = line[:-1]
		input.append([numCapitalWords(p), numComma(p), pattern(p), freqWord(p), numDigits(p), numDigitsMax(p)])
	return array(input)

def createTrainInput(filename):
	f = open(filename, 'r')
	input = []
	output = []
	for line in f.readlines():
		p = line[:-1].split('\t')
		print p
		output.append(int(p[0]))
		input.append([numCapitalWords(p[1]), numComma(p[1]), pattern(p[1]), freqWord(p[1]), numDigits(p[1]), numDigitsMax(p[1])])
	return (array(input), array(output))

# return number of capitalized-first-character words 
def numCapitalWords(string):
    words = string.split()
    num = 0.0
    for w in words:
        if len(w) > 0 and w[0].isupper():
            num = num + 1.0
    return num / len(words)

# return number of commas in given string
def numComma(string):
    return len(re.findall(u',', string))
    
# return 2 if url
#        1 if email
#        0 otherwise
def pattern(string):
    if re.search(ur'[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+\.[a-zA-Z]{2,6}', string):
        return 1
    elif re.search(ur'(http://)?www\.[a-z0-9-_]+\.[a-z0-9-_.%+/?]+', string):
        return 2
    else:
        return 0
        
def addSpace(word):
    ws = re.compile("\s").split(word)
    if len(ws) > 0:
        r = r'\b' + ws[0] + r'\b'
        for w in ws[1:]:
            r = r + u'( )+' + r'\b' + w + r'\b'
        return '(' + r + ')'
    return ''
    
def createRegex(keywords):
    if len(keywords) > 0:
        reg = addSpace(keywords[0])
        for keyword in keywords[1:]:
            reg = reg + '|' + addSpace(keyword)
        return reg
    return ''

# match some frequent words
def freqWord(string):
    words = (
        ((ur'ông', ur'bà'), 4),
        ((ur'công ty', ur'cơ sở', ur'nhà hàng', ur'khách sạn', ur'cửa hàng', ur'quán', ur'shop', ur'cafe'), 3),
        ((ur'tel', ur'telephone', ur'phone', ur'đt', ur'điện thoại'), 2),
        ((ur'fax'), 1)
    )
    for w in words:
        p = re.compile(createRegex(w[0]), re.IGNORECASE | re.UNICODE)
        if p.search(string):
            return w[1]
    return 0

# return number of digits     
def numDigits(string):
    digitStrs = re.findall(r'\d+', string)
    result = 0
    for s in digitStrs:
        result = result + len(s)
    return result
    
# return max number of sequential digits
def numDigitsMax(string):
    digitStrs = re.findall(r'\d+', string)
    result = 0
    for s in digitStrs:        
        result = max(result, len(s))
    return result
        
#p = re.compile(u'(công( )+ty)|(nhà hàng)', re.IGNORECASE | re.UNICODE)
#print p.search(u'nhà Hàng')