# An implementation of the graph illustrated in the blog post.
RATES = (
    ('foot', 'inch', 12),
    ('inch', 'hand', 0.25),
    ('mile', 'foot', 5280),
    ('mile', 'kilometer', 1.6),
    ('lightyear', 'kilometer', 9.461e+12),
    ('inch', 'centimeter', 2.54),
    ('meter', 'centimeter', 100),
    ('kilometer', 'meter', 1000),
)

class RateGraph(object):
    def __init__(self, rates):
        'Initialize the graph from an iterable of (start, end, rate) tuples.'
        self.graph = {}
        for orig, dest, rate in rates:
            self.add_conversion(orig, dest, rate)


    def add_conversion(self, orig, dest, rate):
        'Insert a conversion into the graph. Note we insert its inverse also.'
        if orig not in self.graph:
            self.graph[orig] = {}
        self.graph[orig][dest] = rate

        if dest not in self.graph:
            self.graph[dest] = {}
        self.graph[dest][orig] = 1.0 / rate


    def get_neighbors(self, node):
        'Returns an iterable of the nodes neighboring the given node.'
        if node not in self.graph:
            return None
        return self.graph[node].items()


    def get_nodes(self):
        'Returns an iterable of all the nodes in the graph.'
        return self.graph.keys()


RATE_GRAPH = RateGraph(RATES)
