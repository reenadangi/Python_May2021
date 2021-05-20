def bubbleSort(lst):
    # sort this list using bubble sort 
    return lst
print(bubbleSort([1,2,-3,16,0]))
# -3,0,1,2,16


	
# baron_vb
# 6:19 PM
unorder = [5,2,1,3,8,4,6,9,0,7] #<--10 items
unorder_two = [4,6,2,8,7,1,3]
unorder_three = [15,-3,20,25,-60,0]

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
        print(lst)
    return lst

print(bubble_sort(unorder))


def bubbleSort(lst):
    # goes through the list up to the last value
    for i in range(len(lst)-1):
        # moves through the list up until the last value. Every iteration through i shortens the list
        for j in range(len(lst)-i-1):
            # if lst[j] > greater than the number in the next index, they swap, moving larger number to the end
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst
print(f"First: {bubbleSort([1,2,-3,16,0])}")
print(f"Second: {bubbleSort([33,21,1,23,2,44,99,12,54])}")
print(f"Third: {bubbleSort([9,8,7,6,5,4,3,2,1])}")

