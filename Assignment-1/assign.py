def merge_dicts(A: Dict[Any, Any], B: Dict[Any, Any]) -> Dict[Any, Any]:
   
    C: Dict[Any, Any] = {}

    for key in A:                  
        if key in B:
            va = A[key]
            vb = B[key]

            if va == vb:
                C[key] = va

            elif (isinstance(va, (int, float)) and not isinstance(va, bool)
                  and isinstance(vb, (int, float)) and not isinstance(vb, bool)):
                C[key] = (va + vb) / 2

            elif isinstance(va, list) and isinstance(vb, list):
                C[key] = va + vb

            else:
                C[key] = (va, vb)
        else:
            C[key] = A[key]

    
    for key in B:
        if key not in C:
            C[key] = B[key]

    return C

A = {
    "x": 10,
    "y": [1, 2,5],
    "z": "hello"
}
B = {
    "y": [3, 4],
    "z": "hello",
    "w": 99
}

C = merge_dicts(A, B)
print(C)
