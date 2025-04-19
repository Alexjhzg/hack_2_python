"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    if len(s) > 3:
        return s[1:-1]
    else:
        return s  
    
fn_hack_4('fooziman')
fn_hack_4('barziman')
fn_hack_4('qux')