### solution 1

def reverseList1(list):
    left = 0
    right = len(list) - 1

    while left < right:
        list[left], list[right] = list[right], list[left]
        left += 1
        right -= 1
    
    return list

list = [1, 2, 3, 4, 5]
print(reverseList1(list)) # [5, 4, 3, 2, 1]

### solution 2

def reverseList2(lst):
    return lst[::-1]
list = [1, 2, 3, 4, 5]
print(reverseList2(list))  # Output: [5, 4, 3, 2, 1]

### solution 3

def reverseList3(list):
    return list.reverse()
list = [1, 2, 3, 4, 5]
print(reverseList3(list))  # Output: [5, 4, 3, 2, 1]