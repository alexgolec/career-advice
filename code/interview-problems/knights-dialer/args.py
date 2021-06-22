import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(
            description='Compute knight\'s dialler sequence counts')
    parser.add_argument('start_position', type=int, help='Starting position')
    parser.add_argument('num_hops', type=int, help='Number of hops')
    args = parser.parse_args()

    if args.start_position < 0 or args.start_position > 9:
        print('Starting position must be in [0, 9]')
        sys.exit(1)
    if args.num_hops < 0:
        print('Number of hops must be nonnegative')
        sys.exit(1)

    return args
