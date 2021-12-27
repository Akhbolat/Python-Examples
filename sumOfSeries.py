def sumOfSeries(n):
    Sum = 0
    for i in range(1, n + 1):
        Sum += i * i * i
        print(i)
    return Sum

number = int(input("Enter the number: "))
Result = sumOfSeries(number)
print("Sum of the series: ", Result)
