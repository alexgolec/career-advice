# Level 5: A logarithmic-time, constant space solution which relies on repeated 
#          exponentiation of the adjacency matrix.

import neighbors

# Transform the neighbors map into a 10x10 matrix.
NEIGHBORS_MATRIX = [
        [1 if col in neighbors.NEIGHBORS[row] else 0 for col in range(10)]
                for row in range(10)]


def matrix_multiply(A, B):
    A_rows, A_cols = len(A), len(A[0])
    B_rows, B_cols = len(B), len(B[0])
    result = list(map(lambda i: [0] * B_cols, range(A_rows)))

    for row in range(A_rows):
        for col in range(B_cols):
            for i in range(B_rows):
                result[row][col] += A[row][i] * B[i][col]

    return result


def count_sequences(start_position, num_hops):
    # Start off with a 10x10 identity matrix
    accum = [[1 if i == j else 0 for i in range(10)] for j in range(10)]

    # bin(num_hops) starts with "0b", slice it off with [2:]
    for bit_num, bit in enumerate(reversed(bin(num_hops)[2:])):
        if bit_num == 0:
            import copy
            power_of_2 = copy.deepcopy(NEIGHBORS_MATRIX)
        else:
            power_of_2 = matrix_multiply(power_of_2, power_of_2)

        if bit == '1':
            accum = matrix_multiply(accum, power_of_2)

    return matrix_multiply(accum, [[1]]*10)[start_position][0]


if __name__ == '__main__':
    import args
    a = args.parse_arguments()
    print(count_sequences(a.start_position, a.num_hops))
