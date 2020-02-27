#Author: Daniel Nicholson-Gardner #
#Name: nucleocount.py #
#Part of: ...#
#Created On: 03/09/2019 #
#Modified by: Daniel Nicholson-Gardner #
#Last Modified: 03/09/2019 #

genomeString = input("Gibs me your genome human: ")
genomeStringarr = []

for x in genomeString:
    genomeStringarr.append(x)
a = genomeStringarr.count('A')
t = genomeStringarr.count('T')
c = genomeStringarr.count('C')
g = genomeStringarr.count('G') 

print("%s %s %s %s" %(a, c, g, t))
