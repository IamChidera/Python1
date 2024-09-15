def build_heap(arr):
    swaps = []
    n = len(arr)

    for i in range(n // 2, -1, -1):
        sift_down(arr, i, swaps)

    return swaps

def sift_down(arr, i, swaps):
    n = len(arr)
    min_index = i

    left_child = 2 * i + 1
    if left_child < n and arr[left_child] < arr[min_index]:
        min_index = left_child

    right_child = 2 * i + 2
    if right_child < n and arr[right_child] < arr[min_index]:
        min_index = right_child

    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps.append((i, min_index))
        sift_down(arr, min_index, swaps)

if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))

    swaps = build_heap(data)
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])
