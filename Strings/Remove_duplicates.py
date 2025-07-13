def remove_duplicates(s):
   
    # Your code here
    
    result = ""
    
    seen = ""
    
    for char in s:
        if char not in seen:
            seen += char
            
            result += char
            
    return result
