"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    dictionary = {
        'o': '0',
        'i': '¡',
        'a': '@',
        'u': 'v'
    }
    
    palabra_editada = "".join(dictionary.get(letter, letter) for letter in s)
    
    if palabra_editada:
        # Manejar la última letra: si era 'u' original, mantener 'v' en minúscula
        original_last_char = s[-1] if s else ''
        last_char = palabra_editada[-1].lower() if original_last_char == 'u' else palabra_editada[-1].upper()
        
        palabra_editada = (
            palabra_editada[0].upper() + 
            palabra_editada[1:-1] + 
            last_char
        )
    
    return palabra_editada

fn_hack_3('fooziman')
fn_hack_3('barziman')
fn_hack_3('3q')
fn_hack_3('qu')
fn_hack_3('qux')
