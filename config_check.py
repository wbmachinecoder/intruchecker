#!/usr/bin/python

import hashlib
from check import Check

class config_check(Check):


	#Object constructor
	def __init__(self, filename):
		self.filename = filename

	#run the intrusion check and get important information
	def run(self):
		
		with open("/Users/Mitchell/scripts/python/intruchecker/hashfile", 'r') as fd:
			for line in fd:
				file_info = line.split('\t')
				if file_info[0] == self.filename:
					self.good_hash =  file_info[1]
					print self.good_hash
					
		file_contents = open(self.filename, 'r')
		curhash = hashlib.sha256(file_contents.read()).hexdigest()
		if self.good_hash.strip('\n') == curhash.strip('\n'):
			print curhash
			print good_hash
			print "no changes"
		else:
			print curhash
			print "config change"


