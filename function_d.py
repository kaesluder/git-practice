def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    print("This is Adelle's change")
    maximum_result = numbers[0]
    for number in numbers:
        if number > maximum_result:
            maximum_result = number
            
    return maximum_result



if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
