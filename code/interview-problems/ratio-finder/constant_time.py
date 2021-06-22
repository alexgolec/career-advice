# A constant-time solution based on preprocessing connected components into a 
# structure representing conversions through a root node.

from collections import deque

def make_conversions(graph):
    '''
    Returns a preprocessed conversion structure. The structure has the following 
    format:
      unit -> (root of unit's connected component,
               conversion rate from the root to this unit)
    '''
    def conversions_bfs(rate_graph, start, conversions):
        to_visit = deque()
        to_visit.appendleft( (start, 1.0) )

        while to_visit:
            node, rate_from_origin = to_visit.pop()
            conversions[node] = (start, rate_from_origin)
            for unit, rate in rate_graph.get_neighbors(node):
                if unit not in conversions:
                    to_visit.append((unit, rate_from_origin * rate))

        return conversions

    conversions = {}
    for node in graph.get_nodes():
        if node not in conversions:
            conversions_bfs(graph, node, conversions)
    return conversions

def convert(conversions, start, end):
    'Given a conversion structure, performs a constant-time conversion'
    try:
        start_root, start_rate = conversions[start]
        end_root, end_rate = conversions[end]
    except KeyError:
        return None

    if start_root != end_root:
        return None

    return end_rate / start_rate


if __name__ == '__main__':
    from rates import RATE_GRAPH
    conversions = make_conversions(RATE_GRAPH)
    print(convert(conversions, 'hand', 'lightyear'))
