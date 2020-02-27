#Author: Daniel Nicholson-Gardner #
#Name: nucleocount.py #
#Part of: ...#
#Created On: 03/09/2019 #
#Modified by: Daniel Nicholson-Gardner #
#Last Modified: 05/09/2019 #

from collections import Counter as cnt
   #This first part of the program intializes the input variables and
   # the arrays to be used in searching for the most frequent kmer
usrinput = input("Gibs me your genome human and that integer: ")
genomeStringarr = []
freqPat =[]
freqWrd =[]

kstr = usrinput[(len(usrinput)-2):len(usrinput)]
k = int(kstr)
for x in usrinput:
    genomeStringarr.append(x)

def freqPattern(kval,genlist):
    for x in genlist:
        if kval > 3:
            print("I'm sorry. I'm afraid I can't take a value lower than 3")

        else:
            for x in kval

print()
