#Author: Daniel Nicholson-Gardner #
#Name: dbgkmer.py #
#Created On: 14/11/2019 #
#Modified by: Daniel Nicholson-Gardner #
#Last Modified: 13/12/2019 #

fin = open('datasets/rosalind_ba3b.txt', 'r')
fout=open('datasets/results_genomepath.txt', 'w')
reads=[]
for line in fin.readlines():
    reads.append(line.replace('\n',''))
k=len(reads[0])
fout.write(reads[0])
for r in reads[1:]:
    fout.write(r[k-1:])
fin.close()
fout.close()
