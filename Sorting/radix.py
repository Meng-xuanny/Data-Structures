def counting_sort(a, exp):
    n = len(a)
    output = [0] * n  # Output array
    count = [0] * 10   # Count array for digits (0-9)

    # Count occurrences of each digit at exp place
    for i in range(n):
        index = (a[i] // exp) % 10
        count[index] += 1

    # Compute cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the sorted output array
    for i in range(n - 1, -1, -1):  # Iterate in reverse for stability
        index = (a[i] // exp) % 10
        output[count[index] -1] = a[i]
        count[index] -= 1

    # Copy sorted elements back to original array
    for i in range(n):
        a[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)  # Find the max number
    exp = 1  # Start with 1s place
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10  # Move to the next digit place
    return arr


arr=[170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))