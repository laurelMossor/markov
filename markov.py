"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_source = open(file_path)
    file_as_string = text_source.read()
    file_as_string = file_as_string.replace("\n", " ")

    return file_as_string

#test = open_and_read_file("green-eggs.txt")


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    # key = (word1, word2); value = dict[key] - > word 3
    # split string into list of words with split
    # loop through string by index, using the range(len(list of words))
        # loop through i and i-1, skipping the first index
    words = text_string.split()
    chains = {}

    for i in range(len(words)):
        if i == 0:
            continue
        
        word1 = words[i-1]
        word2 = words[i]
        if i == len(words) - 1:
            following = None
        else:
            following = words[i+1]

        chains[(word1, word2)] = chains.get((word1, word2), []) + [following]
    

    return chains

# chains = make_chains(test)


def make_text(chains):
    """Return text from chains."""
    
    words = []
    keys_list = list(chains.keys())

    current_key = choice(keys_list)

    # initial key = ('Would', 'you')
    # words = ['would', 'you']
    # next_word = choice(chains[key])
    # new_key = (word2 of previous key, next_word)
    
    # while True:
        #append current key to words CHECK
        # -> values to pick from 
        # -> word2 of current key + random picked value 
            #-> values to pick from
        #if key == (I, am) or value == None
            #break

    while True:
        words.append(current_key[0])
        next_word = choice(chains[current_key])
        if next_word == None:
            words.append(current_key[1])
            break

        new_key = (current_key[1], next_word)

        current_key = new_key 


    return ' '.join(words)

# the_thing = make_text(chains)

# input_path = 'green-eggs.txt'
input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
