numbers = [12,7,19,20,33,42,8,15,26,31]
count = 0
a=0
for k in numbers:
    if numbers[a] % 2 == 0:
        print("짝수:",numbers[a])
        count = count + 1

    a=a+1
print("총 짝수 개수: ", count)
