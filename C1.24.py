def vowel_count(data):
    count  = 0
    for x in data:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            count+=1
    return count
