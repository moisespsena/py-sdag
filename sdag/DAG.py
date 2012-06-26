'''
Python Simple Directed Acyclic Graph

Created on 07/12/2011

@author: Moises P. Sena "<moisespsena" + "@" + "gmail.com>"
'''
from sdag.Vertex import Vertex
from sdag.CycleDetector import CycleDetector
from sdag.CycleDetectedException import CycleDetectedException

class DAG:
    def __init__(self):
        self.vertexMap = {}
        self.vertexList = []
        
    def getVerticies(self):
        return self.vertexList
    
    def getLabels(self):
        return self.vertexMap.keys()
 
    def addVertex(self, label):
        retValue = None
        
        if label in self.vertexMap:
            retValue = self.vertexMap[label]
        else:
            retValue = Vertex(label)
            self.vertexMap[label] = retValue
            self.vertexList.append(retValue)

        return retValue
    
    def removeVertex(self, label):
        vertex = self.addVertex(label)
        
        for c in vertex.getChildren():
            c.getParents().remove(vertex)
    
    def getVertex(self, label):
        retValue = None
        
        if label in self.vertexMap:
            retValue = self.vertexMap[label]
            
        return retValue
    
    def addEdge(self, fromVertex, toVertex):
        fromVertex.addEdgeTo(toVertex)

        toVertex.addEdgeFrom(fromVertex)

        detector = CycleDetector(self)
        cycle = detector.introducesCycle(toVertex)

        if cycle != None:
            self.removeEdge(fromVertex, toVertex)

            msg = "Edge between '" + str(fromVertex) + "' and '" + str(toVertex) + "' introduces to cycle in the graph"

            raise CycleDetectedException(msg, cycle)

    def removeEdge(self, fromVertex, toVertex):
        fromVertex.removeEdgeTo(toVertex)
        toVertex.removeEdgeFrom(fromVertex)
        
    def __str__(self):
        verticies = []
        
        if len(self.vertexList) == 0:
            return "DAG{}"
        
        for v in self.vertexList:
            verticies.append(v.getLabel())
        
        return "DAG{'" + "', '".join(verticies) + "'}"
