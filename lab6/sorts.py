# CPE 202 lab 6
# Name: Ashley Sutter
# Student ID: 011278952
# Date (last modified): 2/17/2019
#
# Lab 6
# Section 5
# Purpose: Selection and insertion sorting
# additional comments: Ask if you need to have 100% test coverage with the main function. Also ask if the test file is named correctly (the handin command is different)


import random
import time
import sys

def selection_sort(list):
    compare = 0
    for i in range(len(list)):
        minimum = i
        for j in range(i+1, len(list)):
            compare += 1
            if list[j] < list[minimum]:
                minimum = j
        temp = list[i]
        list[i] = list[minimum]
        list[minimum] = temp
    return compare

def insertion_sort(list):
    compare = 0
    for i in range(1,len(list)):
        j = i
        compare += 1
        while j > 0 and list[j] < list[j-1]:
            compare += 1
            temp = list[j]
            list[j] = list[j-1]
            list[j-1] = temp
            j -= 1
    return compare
   

def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), int(sys.argv[1]))
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

