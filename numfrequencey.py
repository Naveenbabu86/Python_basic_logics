"""
Input: [1, 2, 2, 3, 1, 4]
Output: {1: 2, 2: 2, 3: 1, 4: 1}
"""

n = [1, 2, 2, 3, 1, 4]
dict = {}
for i in n:
    if i in dict:
        dict[i] = dict[i]+1
    else:
        dict[i] = 1
print(dict)
