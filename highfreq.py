def high_freq(lis):
    freq = {}
    for j in lis:
        if j in freq:
            freq[j] += 1
        else:
            freq[j] = 1
    return max(freq, key=freq.get)
lis = list(map(int,input("Enter numbers: ").split()))
most_frequent = high_freq(lis)
print("Most frequent elements are: ",most_frequent) 
