# Level 1: An exponential-time naive recursive implementation which generates
#          all sequences and counts them.

from neighbors import neighbors

def yield_sequences(starting_position, num_hops, sequence=None):
    if sequence is None:
        sequence = [starting_position]
    
    if num_hops == 0:
        yield sequence
        return

    for neighbor in neighbors(starting_position):
        yield from yield_sequences(
            neighbor, num_hops - 1, sequence + [neighbor])

def count_sequences(starting_position, num_hops):
    num_sequences = 0
    for sequence in yield_sequences(starting_position, num_hops):
        num_sequences += 1
    return num_sequences

if __name__ == '__main__':
    import args
    a = args.parse_arguments()
    print(count_sequences(a.start_position, a.num_hops))
