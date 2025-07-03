def find_largest(numbers):
    # Your code goes here
    if not numbers:
        return None
        
    largest = numbers[0]
    
    for num in numbers[1:]:
        if num > largest:
            largest = num
            
    return largest
