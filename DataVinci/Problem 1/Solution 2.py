import string

def count_distinct_words(input):
    #lowercase
    input = input.lower()

    input = input.translate(str.maketrans('', '', string.punctuation))
    words = input.split()

    # dictionary comprehension
    word_count = {word: words.count(word) for word in set(words)}

    return word_count


input_text = "Hello world! Hello Python. Hello!1 hellO 2 PyThOn"
output = count_distinct_words(input_text)
print(output)
