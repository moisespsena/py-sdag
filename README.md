# PySDAG - Python Simple Directed Acyclic Graph

The Python Simple Directed Graph whith Cicle Detector and TopoloGical sorter utilities.

## Test the verticles order in:  c --> a --> b --> d

	#!/usr/bin/python
	from sdag.DAG import DAG
	from sdag.TopologicalSorter import sort as tsort
	
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
	
	assert(rs.index("c") < rs.index("a"))
	assert(rs.index("a") < rs.index("b"))
	assert(rs.index("b") < rs.index("d"))
	assert(rs.index("c") < rs.index("d"))
