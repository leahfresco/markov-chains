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

def open_two_files(file_path1, file_path2):
    """ Takes two file paths as a string and return the combined text as a string.
    """
    # Opens entire file and reads to a string
    contents = open(file_path1).read()

    # Opens second file and appends to a string
    contents2 = open(file_path2).read()

    contents += contents2
    
    return contents

def make_chains(text_string, ngrams_size=2):
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
    for i in range(len(words)-ngrams_size):

        # Use List comprehension there
        key_list = []
        key_list = (words[i+grams] for grams in range(ngrams_size))

        key = tuple(key_list)

        # Creates empty list if no value for key
        chains.setdefault(key, [])

        # Append word after key as value in list of keys
        chains[key].append(words[i+ngrams_size])

    return chains


def make_text(chains, ngrams_size=2):
    """Returns text from chains."""

    words = []

    # Find a first random key
    next_key = choice(chains.keys())

    while not next_key[0][0].isupper():
        next_key = choice(chains.keys())

    # Adds first keys n words into words list
    words.extend(list(next_key))

    # Loop through keys and find words to add until the key does not exist
    while next_key in chains.keys():

        random_word = choice(chains[next_key])
        words.append(random_word) 
        
        key_list = []

        key_list = (words[grams] for grams in range(-ngrams_size, 0))

        next_key = tuple(key_list)


    return " ".join(words)



if len(sys.argv) == 3:
    input_text = open_two_files(sys.argv[1], sys.argv[2])
else:
    # Open the file and turn it into one long string
    input_text = open_and_read_file(sys.argv[1])

#Ask user for n-gram size
n_grams = raw_input("How long should n-grams be: ")

# Get a Markov chain
chains = make_chains(input_text, int(n_grams))

# Produce random text
random_text = make_text(chains, int(n_grams))

print random_text
