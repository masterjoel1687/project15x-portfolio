n = input("Enter a Sentence: ")

def word_frequency_counter(n):
    words = n.split()
    frequency = {}

    for word in words:
        word = word.upper()  
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

result = word_frequency_counter(n)
print("Word Frequency Count:")
print(result)