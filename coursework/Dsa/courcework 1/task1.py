def longestSubarray(arr, k):
    prefix_sum = 0
    max_length = 0
    first_index = {}

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == k:
            max_length = i + 1

        required = prefix_sum - k

        if required in first_index:
            length = i - first_index[required]
            max_length = max(max_length, length)

        if prefix_sum not in first_index:
            first_index[prefix_sum] = i

    return max_length


arr = list(map(int, input("Enter elements: ").replace(",", " ").split()))
k = int(input("Enter k: "))

print("Longest subarray length:", longestSubarray(arr, k))
