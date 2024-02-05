# 242. Valid Anagram (Easy)


# SOLUTION USING COUNTER: (This method probably won't be allowed on interviews)
# Counter is a subclass of dict{}, so this solution runs in O(n) time
# from collections import Counter

# s = 'anagram'
# t = 'nagaram'

# s1 = Counter(s)
# t1 = Counter(t)

# if s1 == t1:
#     print('valid')
# else:
#     print('invalid')



# SOLUTION USING DICTIONARIES
s = 'anagram'
t = 'npog'

dict_s = {}
dict_t = {}

for i in range(len(s)):
    if s[i] not in dict_s:
        dict_s[s[i]] = 1
    else:
        dict_s[s[i]] += 1

for i in range(len(t)):
    if t[i] not in dict_t:
        dict_t[t[i]] = 1
    else:
        dict_t[t[i]] += 1

if dict_s == dict_t:
    print('Valid Anagram')
else:
    print('Not valid.')
