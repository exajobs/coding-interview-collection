# Implement your function below.
def is_one_away(s1, s2):
    if len(s1) - len(s2) >= 2 or len(s2) - len(s1) >= 2:
        return False
    elif len(s1) == len(s2):
        return is_one_away_same_length(s1, s2)
    elif len(s1) > len(s2):
        return is_one_away_diff_lengths(s1, s2)
    else:
        return is_one_away_diff_lengths(s2, s1)


def is_one_away_same_length(s1, s2):
    count_diff = 0
    for i in range(len(s1)):
        if not s1[i] == s2[i]:
            count_diff += 1
            if count_diff > 1:
                return False
    return True


# Assumption: len(s1) == len(s2) + 1
def is_one_away_diff_lengths(s1, s2):
    i = 0
    count_diff = 0
    while i < len(s2):
        if s1[i + count_diff] == s2[i]:
            i += 1
        else:
            count_diff += 1
            if count_diff > 1:
                return False
    return True

# NOTE: The following input values will be used for testing your solution.
is_one_away("abcde", "abcd")  # should return True
is_one_away("abde", "abcde")  # should return True
is_one_away("a", "a")  # should return True
is_one_away("abcdef", "abqdef")  # should return True
is_one_away("abcdef", "abccef")  # should return True
is_one_away("abcdef", "abcde")  # should return True
is_one_away("aaa", "abc")  # should return False
is_one_away("abcde", "abc")  # should return False
is_one_away("abc", "abcde")  # should return False
is_one_away("abc", "bcc")  # should return False
