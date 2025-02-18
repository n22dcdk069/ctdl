from collections import deque

def max_in_sliding_window(nums, k):
    result = []
    dq = deque()  # To store indices of useful elements in the current window

    for i in range(len(nums)):
        # Remove elements from the front of the deque if they are out of the window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove elements smaller than the current element
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        # Add current element index to the deque
        dq.append(i)

        # If we've processed at least k elements, record the max in the window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Taking input from the terminal
num_list_input = input("Enter the list of numbers (e.g. [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]): ")
num_list = eval(num_list_input)  # Convert the string input into a list of integers
k = int(input("Enter the window size k: "))

# Output the result
output = max_in_sliding_window(num_list, k)
print("Output:", output)
