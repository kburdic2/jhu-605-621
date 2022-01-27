#!/usr/bin/python3.8

print("insertion sort demo")

# unsorted arr
inputArr = [8,2,4,9,3,6]

print("Input: ", inputArr)

# basic insertion sort algorithm
def insertionSort( arrIn ):


    for j in range(1, len(arrIn)):
        #print('j = ', j)

        key = arrIn[j]
        #print('key = ', key)

        i = j - 1
        #print('i = ', i)

        while i >= 0 and arrIn[i] > key:
            arrIn[i+1] = arrIn[i]
            i = i - 1

        arrIn[i+1] = key   

    return arrIn


# run function
outputArr = insertionSort(inputArr) 

print("Output: ", outputArr)




