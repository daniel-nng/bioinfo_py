#Author: Daniel Nicholson-Gardner #
#Name: minskew.py #
#Created On: 24/09/2019 #
#Modified by: Daniel Nicholson-Gardner #
#Last Modified: 13/12/2019 #
import  os

def skew(genome):
    return (genome.count('C') - genome.count('G'))


def minimumSkew(genome):

    genomeLen = len(genome)
    skews = []
    minimumSkew = 0
    minimizeSkew = []
    for i in range(genomeLen):
        skews.append(skew(genome[i:genomeLen]))


    minimumSkew = min(skews)
    for j in range(len(skews)):
        if skews[j] == minimumSkew:
            minimizeSkew.append(str(j))

    return minimizeSkew



def main():


     INPATH = './datasets/rosalind_ba1f.txt'
     OUTPATH = './datasets/resultsminiskew.txt'

     try:
        with open(INPATH) as data, open(OUTPATH, 'w') as result:
            genome = data.readline().strip()
            result.write(" ".join(minimumSkew(genome)))
     except IOError as err:
        print("An error occured : " + err.strerror)

if __name__ == '__main__':
    main()




