def main(): 
        # Test the function with your example
    nums = [2, 11, 7, 15]
    target = 9
    num_indices = {}  # Dictionary to store the numbers and their indices

    #breakpoint()
    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_indices:
            print(num_indices[complement], i)
            return [num_indices[complement], i]

        num_indices[num] = i

    return []  # No valid solution found


main()