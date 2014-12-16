#! /usr/bin/python

pickled = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
test = pickle.loads(pickled.read())
for i in test:
  print(''.join(el[0] * el[1] for el in i))

