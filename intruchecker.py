#!/usr/bin/python


import time
import sys
import config_check
import passwd_check

def get_check_types():
	for arg in sys.argv:
		if arg == "all":
			print "test"
	return 

def run_checks():
	print("Running Checks at %s", time.strftime("%H:%M:%S %d"))
	check_list = []
	
	test_check = config_check.config_check("/Users/Mitchell/scripts/python/intruchecker/testfile")
	check_list.append(test_check)

	test2_check = passwd_check.passwd_check("/etc/passwd")
	check_list.append(test2_check)

	for check in check_list:
		check.run()	

def run():
	get_check_types()
	while True:
		run_checks()	
		time.sleep(60)

run()
