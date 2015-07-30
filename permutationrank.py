from collections import defaultdict
from math import factorial
from sys import argv

# permutationrank.py by Matthew Lanier
# Program takes a word as a command line argument and calculates its permutation
# rank based on the order of characters in O(n^2) time.

def calculate_factorial(length, collection):
    # Calculate total factorial of current length
    total = factorial(length)
    
    # Divide by the count of each character currently in the list 
    # This is necessary for words with duplicate characters
    for c in collection:
        total /= factorial(collection[c])
    return total


def get_permutation_rank(word):
    # Current rank (1-based) and length for while-loop
    rank = 1
    length = len(word) - 1
    
    # Lists of sorted and unsorted characters from word
    sorted_chars = sorted(word)
    unsorted_chars = list(word)
    
    # Create collection to keep track of duplicates
    collection = defaultdict(int)
    for c in word:
        collection[c] += 1

    # Loop until calculations are complete
    while (length > 0):
        # Main calculation: take the current character (the first character in
        # the unsorted list) and calculate its position in the sorted list, and
        # multiply this value by the correct factorial value, then add to 
        # the current rank value.
        rank += (sorted_chars.index(unsorted_chars[0]) * calculate_factorial(length, collection))

        # Decrement character count (for duplicate tracking)
        collection[unsorted_chars[0]] -= 1

        # Remove current character from both lists
        sorted_chars.pop(sorted_chars.index(unsorted_chars[0]))
        unsorted_chars.pop(0)

        # Decrement counter
        length -= 1

    # Return total rank
    return rank

# Take command line argument
for argument in argv[1:]:
    print(get_permutation_rank(argument))
