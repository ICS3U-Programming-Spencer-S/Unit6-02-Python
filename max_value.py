#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Dec 19, 2022
# A program which uses lists to generate 10 numbers
# with a range of 1/100 and find the average


import random


def find_max_value(list):

    # Finds the largest number out of the list
    sum = -1
    # len is used to set the max number cap
    len_comm = len(list)
    for counter in range(0, len_comm):
        if list[counter] > sum:
            sum = list[counter]
    return sum


def main():
    # intro message
    print(
        "This is a program that generates 10 numbers and finds the largest number out of them"
    )
    print("")

    numb_list = []
    max_num_list = 0

    # for counter in range loop to generate 10 numbers
    for counter in range(10):
        # creates a number from 1-100
        random_num = random.randint(1, 100)
        # displays number was added to list
        print(f"{random_num} was added to the list")
        # appends the number to the list
        numb_list.append(random_num)

    # calls the function and assign a name
    max_num_list = find_max_value(numb_list)

    # output message
    print("")
    print(f"The largest number in {numb_list} is {max_num_list}")


if __name__ == "__main__":
    main()
