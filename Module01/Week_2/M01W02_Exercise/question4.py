def levenshtein_distance(token1 , token2):
    change_part = min(len(token1),len(token2))
    distance = abs(len(token1)-len(token2))
    for i in range(change_part):
        distance+= 1 if token1[i]==token2[i] else 0
    return distance

assert levenshtein_distance("hi", "hello") == 4.0
print(levenshtein_distance("hola", "hello"))