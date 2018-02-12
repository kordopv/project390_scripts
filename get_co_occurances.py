from __future__ import division

#/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  find frequency word-pairs occurances 
#  
#  look: https://stackoverflow.com/questions/21297740/how-to-find-set-of-most-frequently-occurring-word-pairs-in-a-file-using-python
#  
#  Copyright 2018 Vasiliki Kordopati <vasiliki.kordopati@Vasilikis-MacBook-Pro.local>
#  
#  example of input:
#  DOID_4236 DOID_4236 DOID_4195 DOID_4195 DOID_4195 DOID_4195 DOID_4236 CHEBI_16199
#  DOID_0060260 DOID_0060145 UBERON_0001711 GO_0008152 UBERON_0000955
#  DOID_4071 DOID_4029 DOID_4071 DOID_4029 DOID_1724 DOID_4071 DOID_4029 DOID_4029 DOID_4071 DOID_4029 UBERON_0001165 UBERON_0001166
#  DOID_11755 UBERON_0002394 UBERON_0001174 ENVO_01000472 UBERON_0004529 UBERON_0002114 UBERON_0007651
#  DOID_9408 CHEBI_23888 
#  
#  example of output:
#  DOID_0060260#UBERON_0000955:1
#  ENVO_01000472#UBERON_0001174:1
#  DOID_0060145#GO_0008152:1
#  DOID_11755#UBERON_0002394:1
#  UBERON_0001174#UBERON_0007651:1
#  ENVO_01000472#UBERON_0002394:1
#  UBERON_0001174#UBERON_0002394:1
#  ...
#  
#import file input
import re
import sys
import os
import os, os.path
import math
import subprocess
import multiprocessing
from math import log
from itertools import combinations
from collections import Counter

corpus =[]
#load the corpus
with open(sys.argv[1],'r') as infile2:
	corpus_lines = [lin2.rstrip('\n') for lin2 in infile2]
	for line in corpus_lines:
		wordList = re.sub("[^\w]", " ",  line).split()
		corpus.append(wordList)
	#print lines2
	infile2.close()
	print 'i finished: load the corpus'
	#print corpus

def collect_pairs(lines):
	pair_counter = Counter()
	for line in lines:
		unique_tokens = sorted(set(line))  # exclude duplicates in same line and sort to ensure one word is always before other
		combos = combinations(unique_tokens, 2)
		pair_counter += Counter(combos)
	return pair_counter
	
pairs = collect_pairs(corpus)
with open(sys.argv[2], 'w') as f1:
	for key, value in pairs.items():
		f1.write(str(key[0]+'#'+key[1])+':'+str(value)+'\n')
f1.close()
