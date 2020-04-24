# class Graph:
#     def __init__(self):
#         self.vertices = {
#             "A": {"B"},
#             "B": {"C","D"},
#             "C": {"E"},
#             "D": {"F","G"},
#             "E": {"C"},
#             "F": {"C"},
#             "G": {"A","F"},
#         }

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        """
        {
            A:{},
            B:{},
            C:{},
            D:{}
        }
        """

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

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
        # create a plan_to_visit queue and add starting_vertex to it
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)

        # create a Set for visited_vertices
        visited_vertices = set()

        # while the plan_to_visit queue is not Empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.dequeue()

            # if it's not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all neighbors to the queue
                # self.get_neighbors(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit queue and add starting_vertex to it
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)

        # create a Set for visited_vertices
        visited_vertices = set()

        # while the plan_to_visit queue is not Empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.pop()

            # if it's not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all neighbors to the stack
                # self.get_neighbors(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        visited.add(starting_vertex)

        for vertex in self.get_neighbors(starting_vertex):
            if vertex not in visited:
               return self.dft_recursive(vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        # create a empty queue, and enqueue a PATH to the starting vertex
        # q = Queue()
        # # queue.enqueue([starting_vertex])
        # q.enqueue(starting_vertex)

        # # create a set for visited_vertices
        # visited_vertices = set()
        # current_path = []
        # new_path = []
        # # while the queue is not empty:
        # while q.size() > 0:
        #     # dequeue the first PATH
        #     # grab the last vertex in the path
        #     current_vertex = q.dequeue()
        #     current_path.append(current_vertex)
        #     # last_vertex = q.dequeue()
        #     # if it hasn't been visited
        #     if current_vertex not in visited_vertices:
        #         # check if its the target
        #         if current_vertex == destination_vertex:
        #             # Return the path
        #             return visited_vertices[current_path]
        #         # mark it as visited
        #         visited_vertices.add(current_vertex)
        #         # make new versions of the current path, with each neighbor added to them
        #             # duplicate the path
        #             # add the neighbor
        #             # add the new path to the queue
        #         for neighbor in self.get_neighbors(current_vertex):
        #             # print(current_vertex, neighbor)
        #             if neighbor not in visited_vertices:
        #                 q.enqueue(neighbor)
        #                 new_path.append(neighbor)
        #         q.enqueue(new_path)

        # create a empty queue, and enqueue a PATH to the starting vertex
        neighbors_to_visit = Queue()
        neighbors_to_visit.enqueue([starting_vertex])

        # create a set for visited vertices
        visited_vertices = set()

        # while the queue is not empty
        while neighbors_to_visit.size() > 0:
            # dequeue the first PATH
            current_path = neighbors_to_visit.dequeue()
            # grab the last vertex in the path
            current_vertex = current_path[-1]
            # if it hasn't been visited
            if current_vertex not in visited_vertices:
                # check if it's the target
                if current_vertex == destination_vertex:
                    return current_path
                    # Return the path
                # mark it as visited
                visited_vertices.add(current_vertex)
                # make new versions of the current path, with each neighbor added to them
                for next_vertex in self.get_neighbors(current_vertex):
                    # duplicate the path
                    new_path = list(current_path)
                    # add the neighbor
                    new_path.append(next_vertex)
                    # add the new path to the queue
                    neighbors_to_visit.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        neighbors_to_visit = Stack()
        visited_vertices = set()
        neighbors_to_visit.push((starting_vertex, []))

        while neighbors_to_visit.size() > 0:
            current_vertex_plus_path = neighbors_to_visit.pop()
            current_vertex = current_vertex_plus_path[0]

            if current_vertex not in visited_vertices:
                if current_vertex == destination_vertex:
                    updated_path = current_vertex_plus_path[1] + [current_vertex]
                    return updated_path
                # mark it as visited
                visited_vertices.add(current_vertex)
                # add neighbors to stack
                for neighbor in self.get_neighbors(current_vertex):
                    updated_path = current_vertex_plus_path[1] + [current_vertex]
                    neighbors_to_visit.push((neighbor, updated_path))

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        if path == None:
            path = []
        
        visited.add(starting_vertex)

        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)

                if new_path is not None:
                    return new_path

        return None
        

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
    print("DFT")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    # graph.dft_recursive(1)

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
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
