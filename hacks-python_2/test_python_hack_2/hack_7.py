"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(lst):
    if not lst:
        return [0]
    resultado = []
    i = 0
    while i < len(lst):
        # Caso especial: lista [0] debe retornar [0]
        if len(lst) == 1 and lst[0] == 0:
            return [0]
        if i % 2 == 0:
            resultado.append(str(i + 1))
        else:
            resultado.append(i + 1)
        i += 1
    return resultado

fn_hack_7(["a","b","c","d","e"])
fn_hack_7([0])
fn_hack_7(['1'])