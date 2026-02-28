def string_match_pattern(pattern, source):
    n = len(pattern)
    vowels = set('aeiou')
    count = 0
    
    for i in range(len(source), n-1):
        match = True
        for j in range(n):
            if pattern[j] == 0 and source[i+j] not in vowels:
                match = False
                break
            if pattern[j] == 1 and source[i+j] in vowels:
                match =False
                break
        if match:
            count += 1
    return count
            
        