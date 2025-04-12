
#//* Accepting Arguments

""" import sys

name = sys.argv[1]

print(f"Hello, {name}") """


import argparse

parser = argparse.ArgumentParser(
    description='This program prints the names of my cats'
)

parser.add_argument('-c', '--color', metavar='color', required=True, choices={'blue', 'yellow'}, help='the color to search for')

args = parser.parse_args()

print(args.color)