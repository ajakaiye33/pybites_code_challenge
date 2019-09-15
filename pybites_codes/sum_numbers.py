def sum_numbers(numbers=list(range(1, 101))):
    if numbers is None:
        return 5050
    elif numbers is not None:
        return sum(numbers)


print(sum_numbers([1, 2, 3, 4, 5]))
print(sum_numbers((1, 2, 4, 6)))
print(sum_numbers([]))
print(sum_numbers())
print(sum_numbers(None))
