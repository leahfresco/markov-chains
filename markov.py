"""Generate markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Opens entire file and reads to a string
    contents = open(file_path).read()

    # Strip any new line characters
    contents = contents.replace('\n', ' ')

    return contents


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """

    chains = {}

    # your code goes here

    #splitting string into words
    words = text_string.split()

    #for loop through words to combine into chain dictionary
    for i in range(len(words)-2):
        key = (words[i], words[i+1])
        
        # Creates empty list if no value for key
        chains.setdefault(key, [])

        # Append word after key as value in list of keys
        chains[key].append(words[i+2])

    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    # Find a first random key
    next_key = choice(chains.keys())

    # Adds first keys two words into words list
    words.extend(list(next_key))

    # Loop through keys and find words to add until the key does not exist
    while True:

        random_word = choice(chains[next_key])
        words.append(random_word) 
        
        next_key = (words[-2], words[-1])
        
        # Key does not match whats in chains, meaning done
        if next_key not in chains.keys():
            break

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# #Ask user for n-gram size
# n_grams = raw_input("How long should n-grams be: ")

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
