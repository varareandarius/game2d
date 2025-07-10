
def reorder_words(input_string):
    # I have to reverse the order of words in the string
    words = input_string.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)