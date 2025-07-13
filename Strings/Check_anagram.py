def is_anagram(s, t):
    
    if len(s) != len(t):
        return False
    
    temp = ''
    for char in s:
        if char in t:
            temp+=char
    
    if len(s) == len(temp):
        return True
    else:
        return False
