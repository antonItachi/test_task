# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
#complexity for the solution will be O(n)
def twoSumHashing(num_arr, pair_sum):
    hashTable = []

    for i in range(len(num_arr)):
        num1 = pair_sum - num_arr[i]
        if num1 in hashTable:
            #to print all of them
            #print("Pair with sum", pair_sum,"is: (", num_arr[i],",", num1,")")
            return [num1, num_arr[i]]
        hashTable.append(num_arr[i])
    return -1

a = twoSumHashing([1,2,8,9], 10)
b = twoSumHashing([1,2,3,4], 10)
print("Hashing")
print("Digits can be found: ", a)
print("Digits cant be found: ", b)

#complexity for the solution will be O(n^2)
def twoSumNaive(num_arr, pair_sum):
    #first element
    for i in range(len(num_arr) - 1):
        #second element
        for j in range(i + 1, len(num_arr)):
            # check if these two elemets sum, equal to pair_sum
            if num_arr[i] + num_arr[j] == pair_sum:
                #print("Pair with sum", pair_sum,"is: (", num_arr[i],",",num_arr[j],")")
                return [num_arr[i], num_arr[j]]
    return -1

a1 = twoSumNaive([1,2,8,9], 10)
b1 = twoSumNaive([1,2,3,4], 10)
print("All Options")
print("Digits can be found: ", a1)
print("Digits cant be found: ", b1)

#complexity for the solution will be O(n)
def twoNumberSum(num_arr, pair_sum):
    left = 0
    right = len(num_arr) - 1
    while left < right:
        if num_arr[left] + num_arr[right] == pair_sum:
            return [num_arr[left], num_arr[right]]
        elif num_arr[left] + num_arr[right] < pair_sum:
            left +=1
        elif num_arr[left] + num_arr[right] > pair_sum:
            right -=1
    return -1

a2 = twoNumberSum([1,2,8,9], 10)
b2 = twoNumberSum([1,2,3,4], 10)
print("Two pointers")
print("Digits can be found: ", a2)
print("Digits cant be found: ", b2)










