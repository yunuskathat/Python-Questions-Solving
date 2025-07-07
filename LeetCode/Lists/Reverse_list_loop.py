def reverse_list(lst):
    # Your code goes here
    lst1 = []
    
    for i in range(len(lst)-1, -1, -1):
        lst1.append(lst[i])
    return lst1
