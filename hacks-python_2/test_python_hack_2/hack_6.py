"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""

def fn_hack_6(s):
    if not s:
        return ["0"]
    result = []
    for i in range(len(s)):
        pos = i + 1
        result.append(str(pos) if pos % 2 else "-")
    return result

fn_hack_6(["a","b","c","d","e"])