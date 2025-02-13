import re

def count_distinct_words(input):
    # Convert to lowercase/Uppercase

    #input = input.lower()
    input = input.upper()

    # Remove punctuation using regular expressions
    input = re.sub(r'[^\w\s]', '', input)
    words = input.split()

    # dictionary comprehension
    word_count = {word: words.count(word) for word in set(words)}

    return word_count

input = "Hello world! Hello Python. Hello!1 hellO 2 PyThOn"
output = count_distinct_words(input)
print(output)
