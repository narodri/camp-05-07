S = list(input())
H = {"d":0, "r":1,"m":2,"f":3,"s":4,"l":5,"c":6}

recent = "m"
count = 0

for i in range(len(S)):
    count += 1
    count += abs(H[S[i]]-H[recent])
    recent = S[i]
print(count)
