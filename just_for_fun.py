def count_words(sentence_str):
    alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
    letters_dict = {letter: 0 for letter in alphabet_str}
    
    words_list = sentence_str.lower().split()
    for word in words_list:
        letters_dict[word[0]] += 1
    return letters_dict
sentence_str = "Fibonacci numbers are strongly related to the golden ratio: Binet's formula expresses the nth Fibonacci number in terms of n and the golden ratio, and implies that the ratio of two consecutive Fibonacci numbers tends to the golden ratio as n increases."
print(count_words(sentence_str))
