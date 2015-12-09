#!/usr/bin/python


from  check import Check



class test_check(Check):
    

    def run(self):
        return "test run"

    def report(self):
        return "test report"

