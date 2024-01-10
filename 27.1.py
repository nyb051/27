f = open('27-B.txt')
n = int(f.readline())
arr = list(map(int, f.readlines()))
arr1 = [0] * 5000
currentSum = 0
maxSum = 0
for i in range (n):
    currentSum += arr[i]
    if currentSum % 5000 == 0:
        maxSum = currentSum
    else:
        if arr1[currentSum % 5000] != 0:
            maxSum = max(maxSum, currentSum - arr1[currentSum % 5000])
            #вписывать новый arr1[currentSum % 5000] не надо, потому что он должен быть минимален
        else:
            arr1[currentSum % 5000] = currentSum
            
print(maxSum)
