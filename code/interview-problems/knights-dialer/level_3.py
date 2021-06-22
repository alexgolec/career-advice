# Level 3: A linear-time, linear space recursive solution which counts and 
#          memoizes results.

from neighbors import neighbors

def count_sequences(start_position, num_hops):
    cache = {}

    def helper(position, num_hops):
        if (position, num_hops) in cache:
            return cache[ (position, num_hops) ]

        if num_hops == 0:
            return 1

        else:
            num_sequences = 0
            for neighbor in neighbors(position):
                num_sequences += helper(neighbor, num_hops - 1)
            cache[ (position, num_hops) ] = num_sequences
            return num_sequences

    res = helper(start_position, num_hops)
    return res

if __name__ == '__main__':
    import args
    a = args.parse_arguments()
    print(count_sequences(a.start_position, a.num_hops))
