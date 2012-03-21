from lxml.html.clean import Cleaner

f1 = open('x.html', 'r')

html = f1.read()

html = html.replace('\n', '')
html = html.replace('\n\r', '')
html = html.replace('\t', '')
html = html.replace('  ', '')

a = '\t adasd \t sdad \n\r asdadas'

print a.strip(' \t\n\r')

cleaner = Cleaner(page_structure=False, style=True, javascript=True,scripts=True)
cleaner.kill_tags = ['p', 'img']

print cleaner.clean_html(html)