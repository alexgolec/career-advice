# A linear-time, recursive DFS-based solution.

from collections import deque

def __dfs_helper(rate_graph, node, end, rate_from_origin, visited):
    if node == end:
        return rate_from_origin

    visited.add(node)

    for unit, rate in rate_graph.get_neighbors(node):
        if unit not in visited:
            rate = __dfs_helper(rate_graph, unit, end, rate_from_origin * rate, visited)
            if rate is not None:
                return rate

    return None

def dfs(rate_graph, node, end):
    return __dfs_helper(rate_graph, node, end, 1.0, set())


if __name__ == '__main__':
    from rates import RATE_GRAPH
    print(dfs(RATE_GRAPH, 'hand', 'lightyear'))
