import copy
import math
from typing import TypeVar
from ..Data_Structures import PriorityQueueHeap as pq

T = TypeVar('T')
N = TypeVar('N')

WHITE = 0
GRAY = 1
BLACK = 2

class Edge:
    def __init__(self, dest_node, weight=1):
        self.weight = weight
        self.dest_node = dest_node

    def setWeight(self, new_weight):
        self.weight = new_weight

    def getDestNode(self):
        return self.dest_node


class Node:
    def __init__(self, data: T, name: N):
        self.data = data
        self.name = name
        self.adjList: list[Edge] = []
        self.color = WHITE
        self.discovery_time: int
        self.finish_time: int
        self.distance: int
        self.parent: Node

    def addConnection(self, node, connection_weight=1):
        self.adjList.append(Edge(node, weight=connection_weight))

    def getData(self) -> T:
        return self.data


class Graph:
    time = 0

    def __init__(self, start_node: Node = None):
        self.start_node: Node = start_node
        self.node_lookup = {}
        self.nodes = []
        self.topologically_sorted_list: list = None

    def addConnection(self, src_node: Node, dest_node: Node, connection_weight=1):
        if len([x for x in self.nodes if
                (x.name == dest_node.name and x.data == dest_node.data) or x == dest_node]) <= 0:
            self.nodes.append(dest_node)
            self.node_lookup[dest_node.name] = dest_node
        src_node.addConnection(dest_node, connection_weight=connection_weight)

    def addNode(self, node: Node):
        if self.start_node is None:
            self.start_node = node
        self.nodes.append(node)
        self.node_lookup[node.name] = node

    def resetGraph(self):
        for node in self.nodes:
            node.color = WHITE
            node.discovery_time = node.finish_time = 0


    def bfs(self, start_node: Node = None, dest_node: Node = None):
        queue = []
        start_node = self.start_node if start_node is None else start_node
        start_node.distance = 0
        start_node.parent = None
        queue.append(start_node)

        while len(queue) > 0:
            curr_node = queue.pop(0)
            for adj_edge in curr_node.adjList:
                adj_node = adj_edge.getDestNode()
                if adj_node.color is WHITE:
                    adj_node.color = GRAY
                    adj_node.distance = curr_node.distance + 1
                    adj_node.parent = curr_node
                    if dest_node is not None and (dest_node == adj_node or
                                                  (
                                                          dest_node.name == adj_node.name and dest_node.data == adj_node.data)):
                        return adj_node.distance, adj_node.parent
                    queue.append(adj_node)
            curr_node.color = BLACK

    def shortestPath(self, src_node_name: N, dest_node_name: N):
        return self.bfs(self.node_lookup[src_node_name], self.node_lookup[dest_node_name])

    def dfs(self, start_node: Node = None, dest_node: Node = None):
        start_node = self.start_node if start_node is None else start_node
        start_node.time = 0
        self.dfsVisit(start_node, dest_node)

    def dfsVisit(self, cur_node, dest_node=None, topo_sort_list=[], searched_list=[]):
        searched_list.append(cur_node)
        cur_node.color = GRAY
        type(self).time += 1
        cur_node.discovery_time = type(self).time
        for adj_edge in cur_node.adjList:
            adj_node = adj_edge.getDestNode()
            if adj_node.color is WHITE:
                adj_node.parent = cur_node
                if dest_node is not None and (dest_node == adj_node or
                                              (dest_node.name == adj_node.name and dest_node.data == adj_node.data)):
                    adj_node.discovery_time = cur_node.discovery_time + 1
                    searched_list.append(adj_node)
                    topo_sort_list.insert(0, adj_node)
                    return True, searched_list, topo_sort_list
                found_dest_node, returned_search, returned_topo_sort = \
                    self.dfsVisit(adj_node, dest_node, topo_sort_list, searched_list)
                if found_dest_node:
                    return found_dest_node, returned_search, returned_topo_sort

        cur_node.color = BLACK
        type(self).time += 1
        cur_node.finish_time = type(self).time
        topo_sort_list.insert(0, cur_node)
        self.topologically_sorted_list = topo_sort_list

    def djikstra(self, start_node, dest_node):
        self.pq = pq.Heap(pq.minHeapComparator, start_node)
