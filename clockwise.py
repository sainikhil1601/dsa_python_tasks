def clockwise(lis, inp):
    for i in range(inp):
        lis.insert(0, lis.pop())
    return lis
lis = list(map(int,input("Enter numbers: ").split()))
inp = int(input("Number of steps: "))
rotated_array = clockwise(lis, inp)
print("Rotated array is: ",rotated_array) 
