# help_example.py
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-a',  # flag to use on CLI, also default name if dest is not used
                       action='store',  # what to do with it in the Namespace object
                       choices=['head', 'tail'],  # choice of values
                       help='set the user choice to head or tail',
                       dest='coin_side',  # name handle to reference in the Namespace object
                       )

args = my_parser.parse_args()

#print(vars(args))  # print all stored arguments
print(args.coin_side)
