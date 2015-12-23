#!/usr/bin/python


import hashlib
import sys


hash_file = open("/Users/Mitchell/scripts/python/intruchecker/hashfile", 'w')

for arg in sys.argv:
	filehash  = hashlib.sha256(open(arg, 'r').read()).hexdigest()
	hash_file.write(arg)
	hash_file.write("\t")
	hash_file.write(filehash)
	hash_file.write("\n")
