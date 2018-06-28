num = int(input())

arr = [0 for i in range(10001)]

for i in range(num):
    j = int(input())
    arr[j] += 1;

for i in range(10001):
    if(arr[i]!=0):
        for j in range(arr[i]):
            print(i)
