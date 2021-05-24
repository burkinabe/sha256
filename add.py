def add (*x):
    totalSum = 0
    for number in x:
        totalSum += number
    return totalSum % 2 ** 32
