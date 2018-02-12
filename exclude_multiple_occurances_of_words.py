from __future__ import division

#/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exclude duplicates in same line and sort to ensure one word is always before other
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
#  ['CHEBI_16199', 'DOID_4195', 'DOID_4236']
#  ['DOID_0060145', 'DOID_0060260', 'GO_0008152', 'UBERON_0000955', 'UBERON_0001711']
#  ['DOID_1724', 'DOID_4029', 'DOID_4071', 'UBERON_0001165', 'UBERON_0001166']
#  ['DOID_11755', 'ENVO_01000472', 'UBERON_0001174', 'UBERON_0002114', 'UBERON_0002394', 'UBERON_0004529', 'UBERON_0007651']
#  ['CHEBI_23888', 'DOID_9408']
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

for line in corpus:
	unique_tokens = sorted(set(line))  # exclude duplicates in same line and sort to ensure one word is always before other
	print unique_tokens
	with open(sys.argv[2], 'a') as f1:
		f1.write(str(unique_tokens)+'\n')
	f1.close()
