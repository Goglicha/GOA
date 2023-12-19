def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum = sum + (i ** 2)
        i += 1
    return sum

