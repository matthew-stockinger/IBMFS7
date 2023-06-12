def mean(numbers):
    """Computes the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def median(numbers):
    """Computes the median of a list of numbers."""
    numbers.sort()

    if len(numbers) % 2 == 0:
        lower_bound = numbers[len(numbers) // 2]
        upper_bound = numbers[len(numbers) // 2 - 1]
        return (lower_bound + upper_bound) / 2
    else:
        return numbers[len(numbers) // 2]