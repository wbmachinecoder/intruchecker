#!/usr/bin/python

from check import Check

import difflib
import time


class passwd_check(Check):


	def __init__(self,filename):
		self.filename = filename


	def run(self):
		cur_passwd = open("/etc/passwd",'r')
		old_passwd = open("/Users/Mitchell/passwd.old",'r')

		d = difflib.Differ()
		diff = d.compare(cur_passwd.read(),old_passwd.read())
		print '\n'.join(diff)


