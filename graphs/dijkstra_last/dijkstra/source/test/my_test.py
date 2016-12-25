import unittest
import sys
sys.path.append("..")
from Graph import Graph
from Dijkstra import *

class Graph_Test(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_add_nodes(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_node('C')
        self.graph.add_node('D')
        self.graph.add_node('E')
        self.graph.add_node('F')
        self.graph.add_node('G')
        self.assertEqual(self.graph.nodes, set(['A', 'B', 'C', 'D', 'E', 'E', 'F', 'G']))

    def test_shortest_path(self, ):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_node('C')
        self.graph.add_node('D')
        self.graph.add_node('E')
        self.graph.add_node('F')
        self.graph.add_node('G')
        self.graph.add_edge('A', 'B', 10)
        self.graph.add_edge('A', 'C', 20)
        self.graph.add_edge('B', 'D', 15)
        self.graph.add_edge('C', 'D', 30)
        self.graph.add_edge('B', 'E', 50)
        self.graph.add_edge('D', 'E', 30)
        self.graph.add_edge('E', 'F', 5)
        self.graph.add_edge('F', 'G', 2)
        dijkstra_output = dijkstra(self.graph, 'A')
        self.assertEqual(shortest_path(self.graph, dijkstra_output,'A', 'E'), (55, ['A', 'B', 'D', 'E']))
        self.assertEqual(shortest_path(self.graph, dijkstra_output,'A', 'G'), (62, ['A', 'B', 'D', 'E', 'F', 'G']))

    def test_for_one(self, ):
        self.graph.add_node('A')
        dijkstra_output = dijkstra(self.graph, 'A')
        self.assertEqual(shortest_path(self.graph, dijkstra_output,'A', 'G'), "There is no sense in your request!")

    def test_for_dijkstra_heap(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_node('C')
        self.graph.add_node('D')
        self.graph.add_node('E')
        self.graph.add_node('F')
        self.graph.add_node('G')
        self.graph.add_edge('A', 'B', 10)
        self.graph.add_edge('A', 'C', 20)
        self.graph.add_edge('B', 'D', 15)
        self.graph.add_edge('C', 'D', 30)
        self.graph.add_edge('B', 'E', 50)
        self.graph.add_edge('D', 'E', 30)
        self.graph.add_edge('E', 'F', 5)
        self.graph.add_edge('F', 'G', 2)
        self.assertEqual(dijkstra_with_heap(self.graph, 'A', 'E'), (55, ['A', 'B', 'D', 'E']))
        self.assertEqual(dijkstra_with_heap(self.graph, 'A', 'G'), (62, ['A', 'B', 'D', 'E', 'F', 'G']))


suite = unittest.TestLoader().loadTestsFromTestCase(Graph_Test)
unittest.TextTestRunner(verbosity=2).run(suite)
