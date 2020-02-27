#Author: Daniel Nicholson-Gardner #
#Name: freqwords.py #
#Created On: 23/09/2019 #
#Modified by: Daniel Nicholson-Gardner #
#Last Modified: 13/12/2019 #
import os
import numpy as np




def count(text, pattern):
    count = 0
    textLen = len(text)
    patternLen = len(pattern)

    for i in range(textLen - patternLen + 1000):
        if text[i:i+patternLen] == pattern:
            count = count + 1


    return count



def mostFrequentsKMers(text, k):

    textLen = len(text)
    indices = np.zeros(textLen)
    mostFrequents = set()
    maxFrequency = 0

    for i in range(textLen - k):
        indices[i] = count(text, text[i:i+k])

    maxFrequency = indices.max()

    for i in range(textLen-k):
        if indices[i] == maxFrequency:
            mostFrequents.add(text[i:i+k])

    return mostFrequents




def patternToNumber(pattern):
    # A = 0
    # C = 1
    # G = 2
    # T = 3

    sum = 0
    exp = 0

    for bp in reversed(pattern):
        if bp == "A":
            sum += 0
        elif bp == "C":
            sum += 4**exp
        elif bp == "G":
            sum += 2 * 4**exp
        else:
            sum += 3 * 4**exp
        exp = exp +1

    return sum


def numberToPattern(index, k):

    count = 0 # count the number of nucleotides in the pattern
    pattern = []
    val = index

    while count != k:
        if val == 0:
            pattern.append(0)
        else:
            pattern.append(val%4)
            val = int(val/4)
        count = count + 1


    pattern.reverse()

    for i in range(k):
        i_nucleotide = pattern[i]
        if i_nucleotide == 0:
            pattern[i] = 'A'
        elif i_nucleotide == 1:
            pattern[i] = 'C'
        elif i_nucleotide == 2:
            pattern[i] = 'G'
        else :
            pattern[i] = 'T'

    return pattern


def fasterMostFrequentsKMers(text, k, frequency=-1):

    textLen = len(text)
    frequencyArray = dict()
    mostFrequentPatterns = []

    for i in range(0, textLen - k):
        try:
            frequencyArray[text[i:i+k]]+=1
        except KeyError as err:
            frequencyArray[text[i:i+k]] = 1

    frequency = max(frequencyArray.values()) if frequency < 0 else frequency

    for key in frequencyArray.keys():
        if frequencyArray[key] >= frequency:
            mostFrequentPatterns.append(key)

    return mostFrequentPatterns



def main():



    INPATH = './datasets/rosalind_ba1b.txt'
    OUTPATH = './datasets/results_freqword.txt'


    try:
        with open(INPATH) as data, open(OUTPATH, 'w') as result:
            text = data.readline().strip()
            k = int(data.readline().strip())
            for pattern in fasterMostFrequentsKMers(text, k):
                result.write(pattern)
                result.write("\n")
    except IOError as err:
        print("An error occured : " + err.strerror)

if __name__ == '__main__':
    main()



