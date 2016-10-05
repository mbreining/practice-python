#!/usr/bin/python
# vim: foldlevel=0

"""
http://interactivepython.org/runestone/static/pythonds/Graphs/TheKnightsTourProblem.html
A good example of DFS.
"""
from graph import Graph, Vertex


def get_cell_key(x, y, dimension):
    return y*dimension + x


def generate_valid_moves_from(x, y, dimension):
    valid_moves = []
    deltas = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (-1, -2), (1, -2), (1, 2))
    for dx, dy in deltas:
        new_x, new_y = x+dx, y+dy
        if 0 <= new_x <= dimension-1 and 0 <= new_y <= dimension-1:
            valid_moves.append((new_x, new_y))
    return [get_cell_key(i, j, dimension) for i, j in valid_moves]


def build_graph(dimension=8):
    """ Build a graph of valid knight moves. """
    graph = Graph()
    # Go through each cell one at a time.
    for i in range(dimension):
        for j in range(dimension):
            cell_key = get_cell_key(i, j, dimension)
            # Add the cell to the graph.
            from_vertex = graph.add_vertex(cell_key)

            # Figure out the valid knight moves from that cell.
            valid_moves = generate_valid_moves_from(i, j, dimension)
            for vm_key in valid_moves:
                # Add each target cells to the graph and create an edge to represent
                # the valid move.
                to_vertex = graph.add_vertex(vm_key)
                from_vertex.add_neighbor(to_vertex)
    return graph


def knight_tour(cur_path_len, path, to_visit, target_path_len):
    done = False
    to_visit.color = Vertex.GRAY
    path.append(to_visit)
    cur_path_len += 1
    print "Current vertex {0}".format(to_visit.key)
    print "Current path length {0}".format(cur_path_len)

    if cur_path_len == target_path_len:
        print "DONE"
        done = True  # we found a solution
    else:
        for neighbor in to_visit.neighbors:
            if neighbor.color == Vertex.WHITE:
                done = knight_tour(cur_path_len, path, neighbor, target_path_len)
            if done:
                break  # we found a solution deeper in the recurrence tree

        if not done:  # we ran into a dead end, backtrack
            print "DEAD END"
            path.pop()
            to_visit.color = Vertex.WHITE

    return done


dimension = 5
g = build_graph(dimension)
solution_path = []
# Start with the first cell (0, 0)
knight_tour(0, solution_path, g.vertices[0], dimension*dimension)

print
print "Solution:"
print len(solution_path)
print " ".join([str(i.key) for i in solution_path])
