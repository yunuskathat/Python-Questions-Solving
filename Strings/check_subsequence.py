def is_subsequence(s, t):

    # Your code here
    i = 0
    for char in s:
        if i < len(t) and char == t[i]:
            i += 1
    return i == len(t)
