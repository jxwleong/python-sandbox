# Ref: https://stackoverflow.com/a/69803827
def get_data_value(data, data_name):
    d = data['test']
    return [*item_generator(d, data_name)]


def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        if lookup_key in json_input:
            yield {lookup_key: json_input[lookup_key]}
        else:
            for v in json_input.values():
                yield from item_generator(v, lookup_key)

    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)


json_data = {"test": [{"Tier1": [{"Tier1-Main-Title-1": [{"title": "main", "example": 400}]}]}, {"Tier2": []},
                      {"Tier3": [{"Example1-Sub1": 44, "title": "TEST2"}]}]}

print(get_data_value(json_data, 'title'))


def dictionary_check(input):
    """
    First prints the final entry in the dictionary (most nested) and its key
    Then prints the keys leading into this
    * could be reversed to be more useful, I guess

    src: https://gist.github.com/grandadmiral-thrawn/4a5531a1363863e74ded
    """
    for key,value in input.items():
        if isinstance(value, dict):
            dictionary_check(value)
            print (key)
        else:
            print (key, value)