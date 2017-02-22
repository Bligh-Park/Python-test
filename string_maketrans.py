import string

leet = string.maketrans('abegiloprstz', '463611092572')
s = "The quick brown fox jumped ver the lazy dog."

print s
print s.translate(leet)