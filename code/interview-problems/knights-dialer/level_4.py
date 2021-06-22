# Level 4: A linear-time, constant space solution based on dynamic programming.

from neighbors import neighbors

def count_sequences(start_position, num_hops):
    prior_case = [1] * 10
    current_case = [0] * 10
    current_num_hops = 1

    while current_num_hops <= num_hops:
        current_case = [0] * 10
        current_num_hops += 1

        for position in range(0, 10):
            for neighbor in neighbors(position):
                current_case[position] += prior_case[neighbor]
        prior_case = current_case

    return current_case[start_position]


if __name__ == '__main__':
    import args
    a = args.parse_arguments()
    print(count_sequences(a.start_position, a.num_hops))
