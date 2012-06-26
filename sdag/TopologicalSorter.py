'''
Python Simple Directed Acyclic Graph

Created on 13/12/2011

@author: Moises P. Sena "<moisespsena" + "@" + "gmail.com>"
'''
from sdag.Vertex import Vertex
from sdag.DAG import DAG

NOT_VISITED = 0
VISITING = 1
VISITED = 2

class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def addOnHead(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = self.head # link the new node to the 'previous' node.
        self.head = new_node #  set the current node to the new one.

    def reset(self):
        self.current = self.head
    
    def nextNode(self):
        if self.current:
            self.current = self.current.next

    def currentNode(self):
        return self.current

    def currentData(self):
        if self.current:
            return self.current.data
        
        return None
    
    def __str__(self):
        dataList = []
        node = self.head
        
        while node:
            dataList.append(str(node.data))
            node = node.next
        
        return "LinkedList{" + ", ".join(dataList) + "}"
    
    def toList(self):
        dataList = []
        node = self.head
        
        while node:
            dataList.append(node.data)
            node = node.next
        
        return dataList

def sort(source):
    if isinstance(source, Vertex):
        return sortVertex(source)
    elif isinstance(source, DAG):
        return dfs( source );
    return None

def sortVertex( vertex ):
    # we need to use addFirst method so we will use LinkedList explicitly
    retValue = LinkedList()
    vertexStateMap = {}
    dfsVisit( vertex, vertexStateMap, retValue )

    return retValue.toList()


def dfs( graph ):
    verticies = graph.getVerticies()

    # we need to use addFirst method so we will use LinkedList explicitly
    retValue = LinkedList()

    vertexStateMap = {}

    for vertex in verticies:
        if isNotVisited( vertex, vertexStateMap ):
                dfsVisit( vertex, vertexStateMap, retValue )

    return retValue.toList()

def isNotVisited( vertex, vertexStateMap ):    
    if not vertex in vertexStateMap:
        return True
    
    state = vertexStateMap[ vertex ]

    return NOT_VISITED == state

def dfsVisit( vertex, vertexStateMap, vertexList ):
    if vertex.getLabel() == "br.com.orionsistemas.factor:factor-module-view:1.0-SNAPSHOT":
        pass
    
    vertexStateMap[vertex] = VISITING

    verticies = vertex.getChildren();

    for v in verticies:
        if isNotVisited( v, vertexStateMap ):
            dfsVisit( v, vertexStateMap, vertexList )

    vertexStateMap[vertex] = VISITED;
    vertexList.addOnHead(vertex.getLabel());
