def count_word_frequency(words):
    word_count = {}
    
    for word in words: 
        if word not in word_count: 
            word_count[word] = 0 
        word_count[word] += 1
        
    return word_count

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word_frequency(words))