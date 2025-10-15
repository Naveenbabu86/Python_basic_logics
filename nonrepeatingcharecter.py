input = "aabbcdeff"
dict = {}
for i in input:
    if i in dict:
        dict[i] = dict[i]+1
    else:
        dict[i] = 1
print(dict)

d = dict

for keys, values in d.items():
    if values == 1:
        print(keys)
        break
    else:
        pass



