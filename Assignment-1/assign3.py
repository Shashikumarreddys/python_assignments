
def is_number(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)

def merge_tuple_lists(A: List[Tuple[Any, Any]], B: List[Tuple[Any, Any]]) -> List[Tuple[Any, Any]]:
    
    seen = set()
    order_from_A = []
    mapA = {}
    for k, v in A:
        if k not in seen:
            seen.add(k)
            order_from_A.append(k)
            mapA[k] = v

    seenB = set()
    order_from_B = []
    mapB = {}
    for k, v in B:
        if k not in seenB:
            seenB.add(k)
            order_from_B.append(k)
            mapB[k] = v

    C = []
    for k in order_from_A:
        if k in mapB:  
            va = mapA[k]
            vb = mapB[k]
            if va == vb:
                C.append((k, va))
            elif is_number(va) and is_number(vb):
                C.append((k, (va + vb) / 2))
            elif isinstance(va, str) and isinstance(vb, str):
                C.append((k, va + vb))
            else:
                C.append((k, (va, vb)))
        else:
            C.append((k, mapA[k]))

    for k in order_from_B:
        if k not in mapA:
            C.append((k, mapB[k]))

    return C
A = [("x", 10), ("y", "hi"), ("z", [1,2])]
B = [("y", "bye"), ("z", [1,2]), ("w", 50)]

print(merge_tuple_lists(A, B))

