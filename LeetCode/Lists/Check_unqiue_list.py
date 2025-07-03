def check_unique(lst):
    # Your code goes here
    seen = set(lst)
    
    if len(lst) == len(seen):
        return True
        
    else:
        return False


#or could have been done other way
def are_elements_unique(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False  # Duplicate found
    return True 
