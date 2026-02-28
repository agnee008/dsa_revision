from collections import defaultdict
a = ['apple', 'apple', 'orange', 'banana', 'banana']

count = defaultdict(int)

for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)

    


