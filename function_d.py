def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    print("This is Adelle's change")
    largest_number = 0
    for num in numbers:
        if num > largest_number:
            largest_number = num
    
    return largest_number


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
