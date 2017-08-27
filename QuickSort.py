'''
QUICK SORT

1.  pick the first element of array arr[0] as pivot

2.  qsort those elements of array which are less than pivot with List Comprehension
    => qsort([x for x in arr[1:] if x<arr[0]])
    
3.  qsort those elements of array which are larger than pivot with List Comprehension
    => qsort([x for x in arr[1:] if x>=arr[0]])
'''

def qsort(arr): 
     if len(arr) <= 1:
          return arr
     else:
          return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])


print("Enter array elements (e.g, [1 2 3 4 5 6]):\n")
arr = list(map(int, input().split(' ')))
arr = qsort(arr)
print(arr)
