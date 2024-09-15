from collections import deque

def find_maximum_in_sliding_window(arr, n, m):
    result = []
    max_in_window = deque()

    # Process the first 'm' elements
    for i in range(m):
        while max_in_window and arr[i] >= arr[max_in_window[-1]]:
            max_in_window.pop()
        max_in_window.append(i)

    # Process the remaining elements
    for i in range(m, n):
        result.append(arr[max_in_window[0]])

        # Remove elements that are out of the current window
        while max_in_window and max_in_window[0] <= i - m:
            max_in_window.popleft()

        # Remove elements smaller than the current element
        while max_in_window and arr[i] >= arr[max_in_window[-1]]:
            max_in_window.pop()

        max_in_window.append(i)

    # Add the maximum of the last window
    result.append(arr[max_in_window[0]])

    return result

# Input
n = int(input())
arr = list(map(int, input().split()))
m = int(input())

# Find and print the maximums in sliding windows
result = find_maximum_in_sliding_window(arr, n, m)
for max_val in result:
    print(max_val, end=" ")
