def count_word_frequency(sentence):
    # Your code goes here
    words = sentence.split()
    freq = {}
    
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word] = 1
    return freq
