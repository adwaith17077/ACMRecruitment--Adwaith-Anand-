#Program: Find the second largest number in a list

def second_largest(arr):
    largest = second = -9999999
    for num in arr:
        if num >largest:
            second = largest
            largest = num
        elif num > second and num!=largest:# in case the list has 2 same element which is
                                           #the largest then the second variable will also take the largest value
                                           #so to avoid this we write num not equal to largest
            second = num
    return second

arr = list(map(int, input("Enter numbers: ").split()))

print("Second largest:", second_largest(arr))
