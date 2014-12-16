import urllib.request
import re

nothing = '12345'

def nexturl(nothing):
    page = str(urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % (nothing)).read())
    for i in range(400):
         nextpage = re.findall("nothing is ([0-9]+)", page)
         if nextpage:
             page = str(urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % (nextpage[0])).read())
             print(i, nextpage)
             currentpage = nextpage
         if not nextpage:
             print(page)
             print(currentpage)
             break
    return nextpage
