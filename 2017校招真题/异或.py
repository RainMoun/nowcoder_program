n, m = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
result = 0
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] > A[j] > m:
            result += 1
print(result)