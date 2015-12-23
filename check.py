#!usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


class Check:


    def gather_info(self):
    	raise NotImplementedError("Subclass must implement abstract method")

    def run(self):
    	raise NotImplementedError("Subclass must implement abstract method")

    def report(self):
	raise NotImplementedError("Subclass must implement abstract method")


