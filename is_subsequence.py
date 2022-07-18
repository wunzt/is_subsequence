# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/16/2022
# Description: Returns True if string_a is a subsequence of string_b, via recursion. Otherwise, returns False.

def is_subsequence(string_a, string_b):
    """Returns True if string_a is a subsequence of string_b, via recursion. Otherwise, returns False."""

    if len(string_a) == 0:
        return True

    if string_a[0] in string_b:
        return is_subsequence(string_a[1:], string_b.replace(string_a[0], "", 1))
    else:
        return False
