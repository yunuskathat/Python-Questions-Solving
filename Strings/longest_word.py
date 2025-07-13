def longest_word_length(s):
    
    max_len = 0
    current_len = 0

    for char in s:
        if char != ' ':
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
            current_len = 0  # reset for next word

    # After loop, check last word
    if current_len > max_len:
        max_len = current_len

    return max_len
