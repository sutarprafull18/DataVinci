def find_duplicate_numbers(input):
    count = {}

    for num in input:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    duplicates = [num for num, add in count.items() if add > 1]

    return duplicates

input_number_value = [1, 2, 3, 4, 5, 1, 2, 3, 5, 4, 4, 4, 4, 0, 5, 0]
#input_number_value = [1, 2, 3, 4, 5, 1, 2, 3]
output = find_duplicate_numbers(input_number_value)
print(output)
