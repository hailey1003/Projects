"""
Name: Hailey Reese
PID: A50227795
"""

import random


def generate_edges(size, connectedness):
    """
    DO NOT EDIT THIS METHOD
    Generates undirected edges between vertices to form a graph
    :return: A generator object that returns a tuple of the form (source ID, destination ID)
    used to construct an edge
    """
    assert connectedness <= 1
    random.seed(10)
    for i in range(size):
        for j in range(i + 1, size):
            if random.randrange(0, 100) <= connectedness * 100:
                w = random.randint(1, 20)
                yield [i, j, w]


class Graph:
    """
    Class representing a Graph
    """

    class Edge:
        """
        Class representing an Edge in the Graph
        """

        __slots__ = ['start', 'destination', 'weight']

        def __init__(self, start, destination, weight):
            """
            DO NOT EDIT THIS METHOD
            :param start: represents the starting vertex of the edge
            :param destination: represents the destination vertex of the edge
            :param weight: represents the weight of the edge
            """
            self.start = start
            self.destination = destination
            self.weight = weight

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: edge to compare
            :return: Bool, True if same, otherwise False
            """
            return self.start == other.start and \
                   self.destination.vertex_id == other.destination.vertex_id \
                   and self.weight == other.weight

        def __repr__(self):
            return f"Start: {self.start} Destination: {self.destination} Weight: {self.weight}"

        __str__ = __repr__

        def get_start(self):
            """
            Gets the edge's starting vertex_id
            :return: vertex id of edge
            """
            return self.start

        def get_destination(self):
            """
            Gets the edge's destination vertex_id
            :return: vertex id of edge destination
            """
            return self.destination.vertex_id

        def get_weight(self):
            """
            Gets the edge's weight
            :return: weight of edge
            """
            return self.weight

    class Vertex:
        """
        Class representing an Edge in the Graph
        """

        __slots__ = ['vertex_id', 'edges', 'visited']

        def __init__(self, vertex_id):
            """
            DO NOT EDIT THIS METHOD
            :param vertex_id: represents the unique identifier of the vertex
            """
            self.vertex_id = vertex_id
            self.edges = {}
            self.visited = False

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: vertex to compare
            :return: Bool, True if the same, False otherwise
            """
            return self.vertex_id == other.vertex_id and \
                   self.edges == other.edges and self.visited == other.visited

        def __repr__(self):
            return f"Vertex: {self.vertex_id}"

        __str__ = __repr__

        def degree(self):
            """
            Finds the degree of vertex
            :return: degree of vertex
            """
            return (len(self.edges) / 2)

        def visit(self):
            """
            Sets a vertex's visit value to True
            """
            self.visited = True

        def insert_edge(self, destination, weight):
            """
            Adds an edge representation into the edge map
            :param destination: end point of the edge from vertex
            :param weight: weight of the edge
            """
            edge = Graph.Edge(self.vertex_id, destination, weight)
            self.edges[edge.get_destination()] = edge

        def get_edge(self, destination):
            """
            Gets edge from vertex to specific destination
            :param destination: end point of the edge from vertex
            """
            return self.edges[destination]

        def get_edges(self):
            """
            Gets all edges coming from vertex
            :return: list of all the vertex's edges
            """
            return list(self.edges.values())

    def __init__(self):
        """
        DO NOT EDIT THIS METHOD
        """
        self.adj_map = {}
        self.size = 0

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are Identical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        return self.adj_map == other.adj_map and self.size == other.size

    def add_to_graph(self, source, dest=None, weight=0):
        """
        Inserts a vertex into graph, creates an edge if destination is given
        :param dest: end point of the edge from vertex
        :param weight: weight of the edge
        """
        v = Graph.Vertex(source)
        d = Graph.Vertex(dest)
        if source not in self.adj_map:
            self.adj_map[source] = v
            self.size += 1
        if dest not in self.adj_map and dest is not None:
            self.adj_map[dest] = d
            self.size += 1
        if dest is not None:
            dest_vertex = self.get_vertex(dest)
            source_vertex = self.get_vertex(source)
            source_vertex.insert_edge(dest_vertex, weight)
            dest_vertex.insert_edge(source_vertex, weight)

    def construct_graph_from_file(self, filename):
        """
        Turns the file into a graph, utilizing every line as a vertex
        :param filename: file to open and turn into graph
        """
        f = open(filename)
        for line in f:
            line = line.split()
            print(line)
            if len(line) == 1:
                source = line[0]
                if source.isnumeric():
                    source = int(source)
                self.add_to_graph(source)
            elif len(line) == 2:
                source = line[0]
                if source.isnumeric():
                    source = int(source)
                destination = line[1]
                if destination.isnumeric():
                    destination = int(destination)
                self.add_to_graph(source, destination)
            else:
                source = line[0]
                if source.isnumeric():
                    source = int(source)
                destination = line[1]
                if destination.isnumeric():
                    destination = int(destination)
                weight = int(line[2])
                self.add_to_graph(source, destination, weight)

    def get_vertex(self, vertex_id):
        """
        Using the given vertex id retrieve the corresponding vertex object
        :param vertex_id: id to use to find corresponding vertex value
        :return: vertex value
        """
        return self.adj_map[vertex_id]

    def get_vertices(self):
        """
        Creates a list of all the vertices in the graph
        :return: list of all vertices
        """
        return list(self.adj_map.values())

    def bfs(self, start, target, path=None):
        """
        Does a Breadth-First search to find a path between the start and the target
        :param start: vertex to start path at
        :param target: vertex to end path at
        :param path: list of vertices
        :return: list of vertices in path
        """
        queue = []
        queue.append([start])
        explored = []
        while queue:
            path = queue.pop(0)
            val = path[-1]
            vertex = self.get_vertex(val)
            if val not in explored:
                neighbors = vertex.edges
                for node in neighbors:
                    new = list(path)
                    new.append(node)
                    queue.append(new)
                    vertex.visit()
                    if node == target:
                        return new
                explored.append(val)

    def dfs(self, start, target, path=None):
        """
        Does a Depth-First search to find a path between the start and the target
        :param start: vertex to start path at
        :param target: vertex to end path at
        :param path: list of vertices
        :return: list of vertices in path
        """
        v = self.get_vertex(start)
        v.visit()
        path.append(start)
        if start == target:
            return path
        else:
            for node in v.edges:
                vertex = self.get_vertex(node)
                if vertex.visited is False:
                    new_path = self.dfs(node, target, path)
                    if new_path:
                        return new_path
        path.pop()
        v.visited = False
        return None


def quickest_route(filename, start, destination):
    """
    Constructs a graph with the given file and find the path with the smallest total weight between the two given points
    :param filename: filename to open and convert to graph
    :param start: vertex to start path at
    :param destination: vertex to end path at
    :return: list of vertices in the quickest path
    """
    graph = Graph()
    graph.construct_graph_from_file(filename)
    dfs_route = graph.dfs(start, destination, [])
    bfs_route = graph.bfs(start, destination, [])
    weight1 = 0
    for i in range(len(dfs_route) - 1):
        v = graph.get_vertex(dfs_route[i])
        edge = v.get_edge(dfs_route[i + 1])
        weight = edge.get_weight()
        weight1 += weight
    weight2 = 0
    for i in range(len(bfs_route) - 1):
        v = graph.get_vertex(bfs_route[i])
        edge = v.get_edge(bfs_route[i + 1])
        weight = edge.get_weight()
        weight2 += weight
    dfs_route.insert(0, weight1)
    bfs_route.insert(0, weight2)
    if dfs_route is None and bfs_route is None:
        return []
    elif dfs_route is None:
        return bfs_route
    elif bfs_route is None:
        return dfs_route
    else:
        if weight1 < weight2:
            return dfs_route
        else:
            return bfs_route