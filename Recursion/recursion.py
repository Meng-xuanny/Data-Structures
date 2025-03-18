import math


def printStars(n):
    if n == 0:
        print()
    else:
        print("*", end="")
        printStars(n - 1)


# printStars(7)


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


# print(fact(5))


def isPalindrome(s):
    if len(s) < 2:
        return True
    first = s[0]
    last = s[-1]
    if not first == last:
        return False
    middle = s[1:-1] #excluding the first and the last element
    return isPalindrome(middle)


# print(isPalindrome("level"))


def binarySearch(arr, key, lower, upper):
    if lower > upper:
        return -1
    mid = (lower + upper) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binarySearch(arr, key, mid + 1, upper)
    else:
        return binarySearch(arr, key, lower, mid - 1)


# a = [5,7,19,34,55]
# print(binarySearch(a, 55, 0, len(a) - 1))


def recursiveMax(arr):
    if len(arr) == 1:
        return arr[0]
    # Get the maximum from the rest of the list
    max_rest = recursiveMax(arr[1:])

    # Compare the first element with the maximum of the rest
    if arr[0] > max_rest:
        return arr[0]
    else:
        return max_rest


a = [10, 5, 34, 7, 19, 7]


# print(recursiveMax(a))


def recursiveFind(x, nums):
    if not nums:  #returns -1 when the search reaches an empty list (or out-of-bounds index)
        return -1
    if nums[0] == x:
        return 0
    index = recursiveFind(x, nums[1:])  #returns the index where x was found
    if index != -1:
        return index + 1  #add 1 bc the sub-array starts from the second element


# print(recursiveFind(34, a))


def recursiveString(s):
    if len(s) < 2:
        return s
    first = s[0]
    reversed_sub = recursiveString(s[1:])
    return reversed_sub + first


# print(recursiveString("a"))

def isPrime(number, divisor=2):
    if number <= 1:
        return False  # 0 and 1 are not prime
    if number==2:
        return True
    if divisor > math.isqrt(number):  # Stop when division > sqrt(number)
        return True  # No factors found, so it's prime
    if number % divisor == 0:
        return False
    return isPrime(number, divisor + 1)


# print(isPrime(19))

def mergeSort(a):
    if len(a) <= 1:
        return a
    # Split the list into two halves
    mid = len(a) // 2
    leftPart = mergeSort(a[:mid])  # Recursively sort left half
    rightPart = mergeSort(a[mid:])  # Recursively sort right half
    return merge(leftPart, rightPart)


def merge(left, right):
    merged_list = []
    i, j = 0, 0
    # Merge two sorted lists. only runs as long as BOTH lists have elements left.
    while i < len(left) and j < len(right):
        # this loop stops when one list finishes iterating,
        # possibly leaving elements uniterated in the other list
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    #Append remaining elements (if any)
    merged_list += left[i:] + right[j:]

    return merged_list


arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = mergeSort(arr)
print(sorted_arr)


def perms(lst):
    if len(lst) <= 1:
        return [lst]
    first = lst[0]
    ps = perms(lst[1:])
    result=[]
    for p in ps:
        for i in range(len(p) + 1):
            result.append(p[:i] + [first] + p[i:])
            
    return result


# print(perms(["a", "b", "c"]))


def sum_of_digits(num):

    if num < 10:
        return num
    last_digit = num % 10
    return last_digit + sum_of_digits(num // 10)

print(sum_of_digits(1234))