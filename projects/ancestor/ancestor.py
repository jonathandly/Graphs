
def earliest_ancestor(ancestors, starting_node):
    vertices = {}
    if starting_node not in vertices:
        return -1

    arr = []
    arr.append(starting_node)
    visited = set()
    
    while len(arr) > 0:
        vertex = arr.pop()
        if len(arr) == 1:
            return vertex

        if vertex not in visited:
            visited.add(vertex)

            for vert in vertices[vertex]:
                arr.append(vert)