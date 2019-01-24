class DisjointSet(object):
    def __init__(self):
        self.parents = {}

    def get_root(self, w):
        words_traversed = []
        while w in self.parents and self.parents[w] != w:
            words_traversed.append(w)
            w = self.parents[w]
        for word in words_traversed:
            self.parents[word] = w
        return w

    def add_synonyms(self, w1, w2):
        if w1 not in self.parents:
            self.parents[w1] = w1
        if w2 not in self.parents:
            self.parents[w2] = w2

        w1_root = self.get_root(w1)
        w2_root = self.get_root(w2)
        if w1_root < w2_root:
            w1_root, w2_root = w2_root, w1_root
        self.parents[w2_root] = w1_root

    def are_synonymous(self, w1, w2):
        return self.get_root(w1) == self.get_root(w2)


def preprocess_synonyms(synonym_words):
    ds = DisjointSet()
    for w1, w2 in synonym_words:
        ds.add_synonyms(w1, w2)
    return ds


def synonym_queries(synonym_words, queries):
    '''
    synonym_words: iterable of pairs of strings representing synonymous words
    queries: iterable of pairs of strings representing queries to be tested for 
             synonymous-ness
    '''
    synonyms = preprocess_synonyms(synonym_words)

    output = []
    for q1, q2 in queries:
        q1, q2 = q1.split(), q2.split()
        if len(q1) != len(q2):
            output.append(False)
            continue
        result = True
        for i in range(len(q1)):
            w1, w2 = q1[i], q2[i]
            if w1 == w2:
                continue
            elif synonyms.are_synonymous(w1, w2):
                continue
            result = False
            break
        output.append(result)
    return output


if __name__ == '__main__':
    import console
    console.console(synonym_queries)
