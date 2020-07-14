"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import collections
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        traversed = set()

        while queue.size() > 0:
            t = queue.dequeue()
            if t not in traversed:
                print(t)
                traversed.add(t)
                for nextup in self.get_neighbors(t):
                    queue.enqueue(nextup)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        traversed = set()
        while stack.size() > 0:
            current = stack.pop()
            if current not in traversed:
                print(current)
                traversed.add(current)
                for nextup in self.get_neighbors(current):
                    stack.push(nextup)

    def dft_recursive(self, starting_vertex, traversed=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if traversed is None:
            traversed = set()
        traversed.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex) - traversed:
            self.dft_recursive(neighbor, traversed)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        queue = Queue()
        # make a set to track nodes we've visited
        visited = set()

        path = [starting_vertex]
        queue.enqueue(path)

        while queue.size() > 0:
            current_path = queue.dequeue()
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    path_copy = current_path[:]
                    path_copy.append(neighbor)
                    queue.enqueue(current_path + [neighbor])


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push(starting_vertex)
        traversed = set()
        path = []
        while stack.size()>0:
            current = stack.pop()
            path.append(current)
            for neighbor in self.get_neighbors(current):
                if neighbor not in traversed:
                    traversed.add(neighbor)
                    stack.push(neighbor)
                    if neighbor == destination_vertex:
                        path.append(neighbor)
                        return path

    def dfs_recursive(self, starting_vertex, destination_vertex, traversed = None, path = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if traversed is None:
            traversed = set()
            path = collections.deque([])
            path.append([starting_vertex])

        traversed.add(starting_vertex)
        current = path.pop()
        last = current[-1]
        
        for last in self.get_neighbors(last):
            if last not in traversed:
                route = list(current)
                route.append(last)
                path.append(route)
                if last is destination_vertex:
                    return route

        return self.dfs_recursive(last, destination_vertex, traversed, path)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
