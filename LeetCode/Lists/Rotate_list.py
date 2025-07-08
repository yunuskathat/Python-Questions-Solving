def rotate_list(lst, k):
    # Your code goes here
    n = len(lst)
    if n==0:
        return []
        
    result = lst[:]
        
    k = k%n
        
    for _ in range(k):
        last_element = result.pop()
                    
        result.insert(0,last_element)
                    
    return result
