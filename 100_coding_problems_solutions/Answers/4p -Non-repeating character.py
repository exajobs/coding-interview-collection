# Implement your function below.
def non_repeating(given_string):
    char_count = {}
    for c in given_string:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    for c in given_string:
        if char_count[c] == 1:
            return c
    return None

# NOTE: The following input values will be used for testing your solution.
non_repeating("abcab") # should return 'c'
non_repeating("abab") # should return None
non_repeating("aabbbc") # should return 'c'
non_repeating("aabbdbc") # should return 'd'