# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.cost_graph_search(ab).path()) #Nuevo orden por path_cost
print(search.heuristica_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
