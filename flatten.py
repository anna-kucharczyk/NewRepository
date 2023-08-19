def flatten(list_1):
    flattened = []
    for item in list_1:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened

nested_list = [1, 2, [3, 4, [5, [6]], 7], 8, 9, 10]
flattened_list = flatten(nested_list)
print(flattened_list)

