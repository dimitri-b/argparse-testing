# help_example.py
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-a',
                       action='store',
                       choices=['head', 'tail'],
                       help='set the user choice to head or tail',
                       dest='coin_side')

args = my_parser.parse_args()

#print(vars(args))  # print all stored arguments
print(args.coin_side)
