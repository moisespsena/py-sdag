'''
Python Simple Directed Acyclic Graph

Created on 07/12/2011

@author: Moises P. Sena "<moisespsena" + "@" + "gmail.com>"
'''
class Vertex:
    def __init__(self, label):
        self.label = label
        self.children = []
        self.parents = []
        
    def getLabel(self):
        return self.label
    
    def getChildren(self):
        return self.children
    
    def getParents(self):
        return self.parents
    
    def addEdgeTo(self, vertex):
        self.children.append(vertex)
        
    def removeEdgeTo(self, vertex):
        self.children.remove(vertex)
    
    def addEdgeFrom(self, vertex):
        self.parents.append(vertex)
        
    def removeEdgeFrom(self, vertex):
        self.parents.remove(vertex)
        
    def getChildLabels(self):
        labels = []
        
        for lbl in self.children:
            labels.append(lbl)
            
        return labels
        
    def getParentLabels(self):
        labels = []
        
        for lbl in self.parents:
            labels.append(lbl)
            
        return labels
    
    def isLeaf(self):
        return len(self.children) == 0
    
    def isRoot(self):
        return len(self.parents) == 0
    
    def isConnected(self):
        if self.isLeaf() or self.isRoot():
            return True
        return False
    
    def __str__(self):
        return "Vertex{label='" + self.label + "'}"
    
    def __eq__(self, other):
        if isinstance(other, Vertex):
            if(self.label == other.label):
                return True;
        return False
    
    def __nq__(self, other):
        if isinstance(other, Vertex):
            if(self.label == other.label):
                return False;
        return True
    
    def __hash__(self):
        return self.label.__hash__()
