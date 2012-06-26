'''
Python Simple Directed Acyclic Graph

Created on 07/12/2011

@author: Moises P. Sena "<moisespsena" + "@" + "gmail.com>"
'''
class CycleDetector:
    NOT_VISITED = 0
    VISITING = 1
    VISITED = 2
    
    def __init__(self, dag):
        self.dag = dag
        
    def hasCicle(self):
        vertexList = self.dag.vertexList
        vertexStateMap = {}
        retValue = []
        
        for vertex in vertexList:
            if self.notVisited(vertex, vertexStateMap):
                retValue = self.introducesCycle(vertex, vertexStateMap)
                
                if retValue == None:
                    break
         
    def isNotVisited(self, vertex, vertexStateMap):
        if not vertex.getLabel() in vertexStateMap:
            return True
        
        state = vertexStateMap[vertex.getLabel()]
        
        if state == CycleDetector.NOT_VISITED:
            return True
        
        return False
    
    def isVisiting(self, vertex, vertexStateMap):
        if not vertex.getLabel() in vertexStateMap:
            return False
        
        state = vertexStateMap[vertex.getLabel()]
        
        if state == CycleDetector.VISITING:
            return True
        
        return False
    
    
    def introducesCycle(self, vertex, vertexStateMap=None):
        if vertexStateMap == None:
            vertexStateMap = {}
            
        cycleStack = []
        hasCycle = self.dfsVisit(vertex, cycleStack, vertexStateMap)
        
        if hasCycle:
            firstLabel = cycleStack[0]
            cycle = [firstLabel]
            
            for i in xrange(1, len(cycleStack)):
                label = cycleStack[i]
                
                if firstLabel != label:
                    cycle.append(label)
                else:
                    cycle.append(label)
                    break
            
            return cycle
        return None
    
    def dfsVisit(self, vertex, cycle, vertexStateMap):
        cycle.insert(0, vertex.getLabel())

        vertexStateMap[ vertex.getLabel() ] = CycleDetector.VISITING

        verticies = vertex.getChildren()

        for v in verticies:
            if self.isNotVisited(v, vertexStateMap):
                hasCycle = self.dfsVisit(v, cycle, vertexStateMap)

                if hasCycle:
                    return True
                
            elif self.isVisiting(v, vertexStateMap):
                cycle.insert(0, v.getLabel())
                
                return True
            
        vertexStateMap[vertex.getLabel()] = CycleDetector.VISITED

        del cycle[0];

        return False;
