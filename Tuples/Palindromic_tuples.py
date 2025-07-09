def is_palindromic_tuple(tup):
    # Your code goes here
    revrs_tup = ()
    for i in tup:
        revrs_tup = (i,) + revrs_tup
        
    if tup == revrs_tup:
        return True
    else:
        return False
