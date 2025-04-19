"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(lst):
    n = len(lst)
    reversed_lst = lst[::-1]
    result = []
    for i in range(n):
        num = n - i
        if n % 2 == 1:
            result.append(f"{reversed_lst[i]}-{num}")
        else:
            result.append(str(num))
    return result

fn_hack_8(["a","b","c","d","e"])