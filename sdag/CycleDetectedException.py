'''
Python Simple Directed Acyclic Graph

Created on 07/12/2011

@author: Moises P. Sena "<moisespsena" + "@" + "gmail.com>"
'''
class CycleDetectedException(Exception):
    def __init__(self, value, cycle):
        self.value = value + ": {'" + "' --> '".join(cycle) + "'}"
         
    def __str__(self):
        return repr(self.value)
