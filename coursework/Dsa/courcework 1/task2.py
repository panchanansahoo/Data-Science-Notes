def maximumProductTriplet(arr):

    if len(arr) < 3:
        return None

    arr.sort()

    product1 = arr[-1] * arr[-2] * arr[-3]
    product2 = arr[0] * arr[1] * arr[-1]

    if product1 >= product2:
        return arr[-3], arr[-2], arr[-1]
    else:
        return arr[0], arr[1], arr[-1]


arr = list(map(int, input("Enter elements: ").replace(",", " ").split()))

result = maximumProductTriplet(arr)

if result is None:
    print("At least 3 elements are required")
else:
    print("Triplet having maximum product:", result)