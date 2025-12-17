def merge_lists_preserve_order(A, B):
  
    C = []
    for x in A:
        if x not in C:
            C.append(x)
    for x in B:
        if x not in C:
            C.append(x)
    return C

A = [1, 2, [3,4], 5, 2]
B = [2, [3,4], 6, 7, 1]
C = merge_lists_preserve_order(A, B)
print(C)  
