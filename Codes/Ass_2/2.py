

n = int(input())
l1 = input().split()

m = int(input())
l2 = input().split()

i, j = 0, 0
result = []


while i < n and j < m:
    if int(l1[i]) < int(l2[j]):
        result.append(l1[i])
        i += 1
    else:
        result.append(l2[j])
        j += 1


result.extend(l1[i:])
result.extend(l2[j:])
print(" ".join(result))
