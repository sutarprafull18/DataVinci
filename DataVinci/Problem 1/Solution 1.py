import string

def count_distinct_words(input):
    input = input.upper()

    input = input.translate(str.maketrans('', '', string.punctuation))
    words = input.split()

    # Count of each word
    count = {}
    for text in words:
        if text in count:
            count[text] += 1
        else:
            count[text] = 1

    return count

input_text = "Hello world! Hello Python. Hello!1 hellO 2 PyThOn"
output = count_distinct_words(input_text)
print(output)
