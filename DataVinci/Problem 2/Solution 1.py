def find_duplicates_numbers(input_number):
    noted = set()
    duplicates = set()

    for num in input_number:
        if num in noted:
            duplicates.add(num)
        else:
            noted.add(num)

    return list(duplicates)

input_number_value = [1, 2, 3, 4, 5, 1, 2, 3]
#input_number_value = [1, 2, 3, 4, 5, 1, 2, 3, 5, 4, 4, 4, 4, 0, 5, 0]

output = find_duplicates_numbers(input_number_value)
print(output)

#Note - When I use the Python function, '0' comes first in output,
#        but when I use list comprehension, it comes at the end
#        because of python(the order in which words appear in the list)
#        & comprehension (order is determined by the iteration order of the list).