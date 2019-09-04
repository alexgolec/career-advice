# A linear-time BFS-based solution.

from collections import deque

def bfs(rate_graph, start, end):
    to_visit = deque()
    to_visit.appendleft( (start, 1.0) )
    visited = set()

    while to_visit:
        node, rate_from_origin = to_visit.pop()
        if node == end:
            return rate_from_origin
        visited.add(node)
        for unit, rate in rate_graph.get_neighbors(node):
            if unit not in visited:
                to_visit.appendleft((unit, rate_from_origin * rate))

    return None

if __name__ == '__main__':
    from rates import RATE_GRAPH
    print(bfs(RATE_GRAPH, 'hand', 'lightyear'))
