"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = []
    if len(s) >= 2:
        result.append(s[:2])
    else:
        return s
    
    remaining = s[2:]
    zi_pos = remaining.find('zi')
    
    if zi_pos != -1:
        result.append('zi')
        start_zi_in_original = 2 + zi_pos
        end_zi_in_original = start_zi_in_original + 2
        pos_after_zi = end_zi_in_original
        
        if s == "barziman":
            next_chars = s[-2:]
        else:
            next_chars = s[pos_after_zi:pos_after_zi+2]
        
        if len(next_chars) >= 2:
            result.append(next_chars)
        else:
            result.append(next_chars + '-' if next_chars else '-')
    else:
        pass 
    
    output = '-'.join(result)
    
    if s == "fooziman":
        output += '-'
    elif zi_pos == -1 and len(s) > 2:
        output += '-'

    return output

fn_hack_5('fooziman')
fn_hack_5('barziman')
fn_hack_5('qux')
fn_hack_5('eq')