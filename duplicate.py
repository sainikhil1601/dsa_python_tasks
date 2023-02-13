def duplicate(lis):
    seen = set()
    duplicates = set()
    for num in lis:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
lis = list(map(int,input("Enter numbers: ").split()))
duplicate_ele = duplicate(lis)
print("Duplicate elements are: ",duplicate_ele) 
