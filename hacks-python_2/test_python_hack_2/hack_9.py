"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(input_dict):
    output_dict = {}
    if "foo" in input_dict:
        original_value = input_dict["foo"]
        processed_value = original_value.capitalize().replace("kz", "z")
        output_dict["Foo"] = processed_value
    return output_dict

input_dict = {"foo": "fookziman", "bar": "barziman"}
fn_hack_9(input_dict)