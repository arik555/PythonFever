import itertools

for _ in range(int(input())):
    temp = []
    size = int(input())
    arr = [int(i) for i in input().strip().split()]
    if size == len(arr):
        i = 1
        while size > 0:
            x = list(itertools.combinations(arr, i))
            temp.append(x)
            i += 1
            size -= 1
    temp = [j for i in temp for j in i if j is not None ]
    max_sum = -100 # as per constraint
    for i in temp:
        x = sum(i)
        if x > max_sum:
            max_sum = x
    print(max_sum)
    
