def count_vowels(s):
  
    # Your code here
    vowel = "aeiouAEIOU"
    num = 0
    for char in s:
        if char in vowel:
            num+=1
    return num
