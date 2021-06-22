# Level 2: An exponential-time naive recursive implementation which counts
#          sequences without generating them explicitly.

from neighbors import neighbors

def count_sequences(start_position, num_hops):
    if num_hops == 0:
        return 1
    
    num_sequences = 0
    for position in neighbors(start_position):
        num_sequences += count_sequences(position, num_hops - 1)
    return num_sequences


if __name__ == '__main__':
    import args
    a = args.parse_arguments()
    print(count_sequences(a.start_position, a.num_hops))
