def is_palindrome(s):
   
    cleaned= ""

    for char in s:
        if char.isalnum():
            cleaned += char.lower()
        
    if cleaned == cleaned[::-1]:
        return True
    else:
        return False
