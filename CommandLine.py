# This program adds up integers using command line input which I wont be doing right now nah.
import sys
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print('sum = ', total)
except ValueError:
    print("Please supply integer")