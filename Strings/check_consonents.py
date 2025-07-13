def count_consonants(s):
   
    # Your code here
    
    vowel = 'aeiouAEIOU'
    count = 0
    
    for char in s:
        if char.isalpha() and char not in vowel:
            count+=1
    
    return count
