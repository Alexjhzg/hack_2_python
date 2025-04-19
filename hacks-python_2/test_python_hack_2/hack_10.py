"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = []
    counter = 1
    for element in s:
        if isinstance(element, dict):
            new_dict = {}
            for key, value in element.items():
                new_key = str(counter)
                counter += 1
                new_value = str(counter)
                counter += 1
                new_dict[new_key] = new_value
            result.append(new_dict)
        elif isinstance(element, set):
            new_set = set()
            for _ in element:
                new_element = str(counter)
                new_set.add(new_element)
                counter += 1
            result.append(new_set)
    return result

fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}])