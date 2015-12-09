#!usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4


class Check:


    def gather_info(self):
     raise NotImplementedError()

    def run(self):
     raise NotImplementedError()

    def report(self):
     raise NotImplementedError()


