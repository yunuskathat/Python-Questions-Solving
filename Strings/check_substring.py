def is_substring(s, t):

    # Your code here
    for i in range(len(s) -len(t)+1):
        if s[i:i+len(t)] == t:
            return True
    return False
