#!/usr/bin/env python3

def return_evens(num_list):
    """Returns a list of even numbers from num_list. If no evens, returns an empty list."""
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    """Appends an exclamation mark to each sentence in sentence_list. Returns the modified list."""
    return [sentence + '!' for sentence in sentence_list]
