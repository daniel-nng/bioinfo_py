#!/usr/bin/env python3

#Author: Daniel Nicholson-Gardner #
#Name: dbgraphofstrings.py #
#Part of: Lab 5#
#Created On: 03/09/2019 #
#Modified by: Daniel Nicholson-Gardner #
#Last Modified: 03/09/2019 #

class DbG:

    @staticmethod
    def chop(st, k):
        """ Chop a string up into k mers of given length """
        for i in range(0, len(st)-(k-1)):
            yield (st[i:i+k], st[i:i+k-1], st[i+1:i+k])
    class Node:
        """ Node in a de Bruijn graph, representing a k-1 mer.  We keep
            track of # of incoming/outgoing edges so it's easy to check
            for balanced, semi-balanced. """
        def __init__(self, km1mer):
            self.km1mer = km1mer
        def __hash__(self):
            return hash(self.k1mer)
    def __init__(self, strIter, k):
        """ Build de Bruijn multigraph given string iterator and k-mer
            length k """
        self.G = {}    
        self.nodes = {} 
        for st in strIter:
            for kmer  in self.chop(st, k):
                km1L, km1r = kmer[:-1],kmer[1:]
                nodeL, nodeR = None, None
                if km1L in self.nodes:
                    nodeL = self.nodes[km1L]
                else:
                    nodeL = self.nodes[km1L] = self.Node(km1L)
                if km1R in self.nodes:
                    nodeR = self.nodes[km1R]
                else:
                    nodeR = self.nodes[km1R] = self.Node(km1R) 
                    self.G.setdefault(nodeL, []).append(nodeR)
    def eulerPath(self):
        g = self.G
        tour =[]
   
        src = g.iterkeys().next()
        def _visit(n):
            while len(g[n]) > 0:
                dst = g[n].pop()
                _visit(dst)
            tour.append(n)
        _visit(src)
        tour = tour[::-1][:-1]

        return map(str,tour)
import sys

def build_deGruijnGraph(text,k):
	''' first get the unique k-1 mers, which are in fact the nodes of the De Gruijn Graph '''
	k_1mers = []
	for i in range(len(text)-k+2):
		k_1mers.append(text[i:i+k-1])

	k_1mers = sorted(list(set(k_1mers)))
	''' generate nodes'''
	nodes = {}
	for i,v in enumerate(k_1mers):
		nodes[i] = v
	invnodes = {v:i for i,v in nodes.items()}
	''' adding edges based on the overlapping graph of k-1 mers '''
	edges = {}
	for i in range(len(text)-k+1):
		if invnodes[text[i:i+k-1]] in edges:
			edges[invnodes[text[i:i+k-1]]].append(invnodes[text[i+1:i+k]])
		else:
			edges[invnodes[text[i:i+k-1]]] = [invnodes[text[i+1:i+k]]]
	''' print out the result '''
	temp = []
	for key,vals in edges.items():
		print (nodes[key],'->',','.join(sorted([nodes[val] for val in vals])))
		temp.append( nodes[key]+' -> '+','.join(sorted([nodes[val] for val in vals])) )
	return temp

if len(sys.argv) == 2:
	filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()
	k = int(lines[0])
	text = lines[1]
else:
	text = 'AAGATTCTCTAAGA'
	k = 4
	
temp = build_deGruijnGraph(text,k)
