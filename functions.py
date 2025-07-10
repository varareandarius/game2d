def reverse_each_word(input_string):
    words = input_string.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

def checkPalindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

def reorder_words(input_string):
    # I have to reverse the order of words in the string
    words = input_string.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

def checkPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def highest_denominator(first_number, second_number):
    if first_number == 0 or second_number == 0:
        return "Denominator is 0, so the division is not possible"
    else:
        # we need to find the highest common denominator usind first and second number
        while second_number:
            first_number, second_number = second_number, first_number % second_number
        if(first_number < 0):
            first_number = -first_number
        return first_number

def bubble_sort(arr):
    arr = arr.copy()

    n = len(arr)
    isSwapped = True
    for i in range(n):
        if not isSwapped:
            break
        isSwapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSwapped = True
    return arr

def merge(left, right):
    result = []
    indexLeft = indexRight = 0
    while indexLeft < len(left) and indexRight < len(right):
        if left[indexLeft] < right[indexRight]:
            result.append(left[indexLeft])
            indexLeft += 1
        else:
            result.append(right[indexRight])
            indexRight += 1
    result.extend(left[indexLeft:])
    result.extend(right[indexRight:])
    return result

def merge_sort(arr):
    arr = arr.copy()

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left = merge_sort(left_half)
        right = merge_sort(right_half)
        
        finalArr = merge(left, right)
        return finalArr
    else:
        return arr