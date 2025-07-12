def merge_dicts_with_overlapping_keys(dicts):
    # Your code goes here
    merged = {}
    for d in dicts:
        for key,value in d.items():
            if key in merged :
                merged[key] += value
            else:
                merged[key] = value
                
    return merged
