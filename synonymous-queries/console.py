import copy
import re


def normalize(s):
    return re.sub('\s+', ' ', s.strip())


DEMO_SYNONYMS = [
    ('rate', 'ratings'),
    ('rating', 'ratings'),
    ('approval', 'popularity'),
]


def console(synonym_queries):
    synonym_list = copy.copy(DEMO_SYNONYMS)

    print('Using default synonyms:')
    for s1, s2 in synonym_list:
        print('  {} <-> {}'.format(s1, s2))
    print()

    try:
        print('Input additional synonym pairs, e.g. \'rate ratings\'')
        while True:
            raw_synonyms = normalize(input('(Ctrl-D to finish synonyms): '))
            synonyms = raw_synonyms.split()
            if len(synonyms) != 2:
                print('Two words, please')
                continue
            w1, w2 = synonyms
            print('Added synonyms {} <-> {}'.format(w1, w2))
            synonym_list.append( (w1, w2) )
    except EOFError:
        pass

    try:
        print('Input queries':)
        while True:
            q1 = normalize(input('Query 1: ').strip())
            q2 = normalize(input('Query 2: ').strip())
            synonymous = synonym_queries(synonym_list, [(q1, q2)])[0]
            print('\'{}\' and \'{}\' {} synonymous'.format(q1, q2,
                'ARE' if synonymous else 'ARE NOT'))
    except EOFError:
        pass
    print()
