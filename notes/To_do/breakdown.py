decrypt string from alpabet
for i in range(-1, -(len(s)+1), -1):
    temp = ''
    if s[i] == '#':
        temp += s[i-2] + s[i-1] + s[i]
        reult = t_map[temp] + result
        p -= 3

    if p == i:
        result = t_map[s[i]] + result
        p -= 1