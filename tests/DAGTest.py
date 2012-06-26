'''
Python Simple Directed Acyclic Graph

Created on 07/12/2011

@author: Moises P. Sena "<moisespsena" + "@" + "gmail.com>"
'''
import unittest
from sdag.DAG import DAG
from sdag.TopologicalSorter import sort as tsort

class DAGTest(unittest.TestCase):
    
    def testSimple(self):
        '''
        Tests the verticles order in:
        
        c --> a --> b --> d
        '''
        
        dag = DAG()
        a = dag.addVertex("a")
        b = dag.addVertex("b")
        c = dag.addVertex("c")
        d = dag.addVertex("d")
        
        dag.addEdge(c, a)
        dag.addEdge(a, b)
        dag.addEdge(b, d)
        dag.addEdge(c, d)
        
        rs = tsort(dag)
        
        self.assertTrue(rs.index("c") < rs.index("a"))
        self.assertTrue(rs.index("a") < rs.index("b"))
        self.assertTrue(rs.index("b") < rs.index("d"))
        self.assertTrue(rs.index("c") < rs.index("d"))
        

if __name__ == "__main__":
    unittest.main()
