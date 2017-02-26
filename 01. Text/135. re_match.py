import re
text = 'this is some text -- with punctiuation.'
pattern = 'is'
print 'Text :', text
print 'Patern:', pattern

m = re.match(pattern, text)
print 'Match :', m
s = re.search(pattern, text)
print 'Search :', s