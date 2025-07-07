def count_even_odd(lst):
    # Your code goes here
    even = 0
    odd = 0
    for i in lst:
        if i%2 != 0:
            odd+=1
        else:
            even+=1
    return (even,odd)
