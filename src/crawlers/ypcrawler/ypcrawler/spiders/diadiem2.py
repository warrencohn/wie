# coding=latin-1
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from urlparse import urlparse
import os
import re
import json
import urllib2
import urllib
import pymongo
import math
from datetime import datetime
from time import gmtime, strftime
import sys


_spec_chars = [u'\xb4', u'\xc1',u'\xe1',u'\xc0',u'\xc2',u'\xe0',u'\xc2',u'\xe2',u'\xc4',u'\xe4',u'\xc3',u'\xe3',u'\xc5',u'\xe5',u'\xc6',u'\xe6',u'\xc7',u'\xe7',u'\xd0',u'\xf0',u'\xc9',u'\xe9',u'\xc8',u'\xe8',u'\xca',u'\xea',u'\xcb',u'\xeb',u'\xcd',u'\xed',u'\xcc',u'\xec',u'\xce',u'\xee',u'\xcf',u'\xef',u'\xd1',u'\xf1',u'\xd3',u'\xf3',u'\xd2',u'\xf2',u'\xd4',u'\xf4',u'\xd6',u'\xf6',u'\xd5',u'\xf5',u'\xd8',u'\xf8',u'\xdf',u'\xde',u'\xfe',u'\xda',u'\xfa',u'\xd9',u'\xf9',u'\xdb',u'\xfb',u'\xdc',u'\xfc',u'\xdd',u'\xfd',u'\xff',u'\xa9',u'\xae',u'\u2122',u'\u20ac',u'\xa2',u'\xa3',u'\u2018',u'\u2019',u'\u201c',u'\u201d',u'\xab',u'\xbb',u'\u2014',u'\u2013',u'\xb0',u'\xb1',u'\xbc',u'\xbd',u'\xbe',u'\xd7',u'\xf7',u'\u03b1',u'\u03b2',u'\u221e', u'\u1ef9']

def cleanspec(s, cleaned=_spec_chars):
    return ''.join([(c in cleaned and ' ' or c) for c in s])



class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("log.dat", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

sys.stdout = Logger()

class diadiemSpider2(CrawlSpider):
    totalResults = 0
    catResult = []
    
    diadiem_clt = None
    diadiem_stt = None
    diadiem_log = None
    diadiem_ltw = None
    
    latestWork = None
    
    
    name = 'diadiem2'
    allowed_domains = ['diadiem.com']
    # start_urls = ['http://www.diadiem.com/directory.aspx?st=SaiGon&l=0']

    rules = (
        #Rule(SgmlLinkExtractor(allow=('diadiem.com/directory.aspx?.*$', ))),
        
        Rule(SgmlLinkExtractor(allow=('diadiem.com/directory.aspx.*$', )), callback='parse_cate'),
    )
    
    'run if this is the firt time you run the program'
    def firstimerun(self):
        self.init()
        
        self.initLatestWork(1, 1, 0, 0)


    dest = []
    src = []
    dist = []
    def checkResult(self):
        conn = pymongo.Connection()
        db = conn.diadiem
        
        clt = db.data
        
        src = db.stat
        
        src = []
        dist = []
        
        dest = src.find_one()['catCounter']
        
        print ""
        
        for i in range(1, 28):
            regex = r"^%s_" % i
            b = clt.find({"NnDv":{"$regex":regex}})
            # print b.count()
            src.append(b.count())
            dist.append(dest[i-1] - b.count())
        t1 = 0
        t2 = 0
        dd = 0
        for i in range(0, 27):
            print "%s \t   %s \t   %s" % (dest[i], src[i], dist[i])
            t1 += dest[i]
            t2 += src[i]
            dd += dist[i]
            
        print "%s \t   %s \t   %s" % (t1, t2, dd)

    def rerun(self):
        for i in range(1, 28): # per category

            npage = int(math.ceil(self.catResult[i-1] / nRow))

            for j in range(1, npage + 1): # per page
                
                data = self.requestd(i, j, nRow)
                dlen = len(data['dsCompany'])

                for k in range(self.latestWork["a"], dlen): # per address
                    dd = data['dsCompany'][k]                    

                    self.insert(dd)


    'main function '
    def start_requests(self):
        self.connectDB()
        
        # case 1
        #self.firstimerun()

        # case 2
        # self.getLatestWork()
        # print "self.latestWork: c = %s, p = %s, a = %s, total=%s" %(self.latestWork['c'], self.latestWork['p'], self.latestWork['a'], self.latestWork['counter'])
        
        # self.run()
        
        # case 3
        self.checkResult()
        
        
    
    'read and run'
    def run(self):
        self.readInitVar()
        self.downloadAll()
    
    'read init var'
    def readInitVar(self):
        print "readInitVar;"
        init = self.diadiem_stt.find_one()
        self.catResult =  init['catCounter']
        self.totalResults = init['glbCounter']
        
        print "self.catResult", self.catResult
        print "self.totalResults ", self.totalResults 
        
    
    'get number record per category, and total records'
    def init(self):
        
        for i in range(1, 28):
            tr = int(self.get_total_row(i))
            self.totalResults += tr 
            self.catResult.append(tr)
        print self.catResult
        print "totalResults %s" % self.totalResults
        
        self.diadiem_stt.update({'key': 'logCounter'}, {'$set': {'key': 'logCounter', 'catCounter': self.catResult, 'glbCounter': self.totalResults}}, True)
        
        self.diadiem_stt.find_one()
    
    
    'save latest work information of current session'
    def saveLatestWork(self, c, p, a, counter):
        self.diadiem_ltw.update({"key":"latest_work"}, {"$set": {'c':c, 'p':p, 'a':a, 'counter':counter}}, True)
    
    'init latest work log'
    def initLatestWork(self, c, p, a, counter):
        self.diadiem_ltw.remove()
        self.diadiem_ltw.update({"key":"latest_work"}, {"$set": {'c':c, 'p':p, 'a':a, 'counter':counter}}, True)
    
    'get latest work from previous session'
    def getLatestWork(self):
        data = self.diadiem_ltw.find({"key":"latest_work"}).limit(1)
        # print "data.count()",data.count()
        if data.count() == 1:
            self.latestWork = data[0]
        else:
            self.latestWork = {"c":1, "p":1, "a":0, "counter":0}
        
    
    'get all data from diadiem.com'
    def downloadAll(self):
        nRow = 20
        
        counter = self.latestWork["counter"]
        ccounter = 0
        
        dlen = 0
        
        fname = strftime("%Y-%m-%d %H-%M-%S", gmtime())
 
        
        for i in range(self.latestWork["c"], 28): # per category
            ccounter = 0
            self.logTo(fname, "cID = %s, total record = %s" % (i, self.catResult[i-1]))
            npage = int(math.ceil(self.catResult[i-1] / nRow))
            print type(npage)
            
            for j in range(self.latestWork["p"], npage + 1): # per page
                
                data = self.requestd(i, j, nRow)
                dlen = len(data['dsCompany'])

                for k in range(self.latestWork["a"], dlen): # per address
                    dd = data['dsCompany'][k]                    
                   
                    counter += 1
                    ccounter += 1
                    self.logTo(fname, "[%s] inserted c=%s p=%s a=%s > %s" % (counter, i, j, k, dd['TCtyKD']))
                    
                    # save latest work
                    self.saveCatLog(i, j, k)
                    self.saveLatestWork(i, j, k, counter)
                    
                    counter -= 1
                    
                    self.insert(dd)
                
                    counter += 1
                
                self.latestWork["a"] = 0  
                
                # break
            self.logTo(fname, "total cat %s > %s" % (i, ccounter))
            
            self.latestWork["p"] = 1
            
            # break
                
        self.logTo(fname, "total: %s objects" % counter)
        
    
    'save to database the current work of a category, p-th page, a-th record'
    def saveCatLog(self, i , p, a):
        self.diadiem_log.update({"cat": i}, {"$set":{"p":p, "a":a}}, True)

    'log to file a log string'
    def logTo(self, file, str):
        #print cleanspec(str)
        date = datetime.now()
        str = "%s %s %s" % (date, str, "\n")
        print cleanspec(str)
        #open(file, "ab").write(cleanspec(str))
                
    'make a request to diadiem ajax server'
    def requestd(self, cid, npage, nrow):
        formdata={'stpe':'28',
                  'st':'SaiGon',
                  'F':'',
                  'C':'',
                  'K':'',
                  'A':'',
                  'S':'T',
                  'P':npage,
                  'R':nrow,
                  'fD':'1',
                  'uID':'0',
                  'cID':cid,
                  'dID':'0',
                  '_':''
                  }
        print "Query: P = %s cID = %s, R = %s" % (npage, cid, nrow)
        res = urllib2.urlopen("http://www.diadiem.com/Comp.aspx", urllib.urlencode(formdata))
        res_data = res.read()
        # res_data = res_data.replace("\\\'","'")
        # res_data = res_data.replace("\\:",":")
        
        # replace all with single command 
        res_data = re.sub(r'\\([^"])', r'\1', res_data)
        
        open("test.html", "wb").write(res_data)
        data = json.loads(res_data)
        res.close()
        return data
    
    'get the number of records per category'
    def get_total_row(self, cate):
        data = self.requestd(cate, '1', '1')
        print "total row %s" % data['tr']
        return data['tr']
    

 
    'connect to mongo database, and get 4 collections'
    def connectDB(self):
        conn = pymongo.Connection()
        db = conn.diadiem
        
        self.diadiem_clt = db.data
        self.diadiem_stt = db.stat
        self.diadiem_log = db.log
        self.diadiem_ltw = db.latestwork
        
    
    'insert a address record to database'
    def insert(self, dd):  
        #dd = {"name": "hungvjnh"}
        self.diadiem_clt.update({'MCty':dd['MCty']},{"$set":dd}, True)

            
    
    
    
