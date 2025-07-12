def is_subset(lst1, lst2):
    # Your code goes here
    check_lst = []
    
    for i in lst1:
        found = False
        for j in lst2:
            if i == j:
                found = True
                break
        if found:
            check_lst.append(i)

    if len(check_lst) == len(lst1):
        return True
    else:
        return False
