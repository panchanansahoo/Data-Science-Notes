def trap(arr):

    if len(arr) < 3:
        return 0

    left = 0
    right = len(arr) - 1

    left_max = 0
    right_max = 0
    water = 0

    while left < right:

        if arr[left] <= arr[right]:

            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]

            left += 1

        else:

            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water += right_max - arr[right]

            right -= 1

    return water


arr = list(map(int, input("Enter heights: ").replace(",", " ").split()))

print("Trapped water:", trap(arr))