def sum_dicts(*kdicts) -> dict:
    # write your code here
    result = {}
    for dictionary in kdicts:
        for item in dictionary:
            if not item in result:
                result.update({item: dictionary[item]})
            else:
                 result.update({item: result[item] + dictionary[item]})
    return result

first = {"a": 2, "b": 4};
second = {"a": 2, "b": 10};
third = {"d": -5, "e"};
print(sum_dicts(first, second, third))