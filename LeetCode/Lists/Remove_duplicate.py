def remove_duplicates(lst):
    # Your code goes here
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
