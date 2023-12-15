#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Dec. 12, 2023
# This program generates 10 random numbers then finds the max number and uses lists.

import constants
import random


def find_max_value(list):
    # declare variable
    largest_num = 0

    # Look for largest number
    for counter in range(0, constants.SIZE):
        if list[counter] > largest_num:
            largest_num = list[counter]

    # return value
    return largest_num


def main():
    # introduce program to user
    print("Hello, this program generates 10 random numbers then finds the max.")

    # declare list
    num_list = []

    # populate list with loop
    for counter in range(0, constants.SIZE):
        # generate random numbers 0-100
        random_number = random.randint(constants.MIN, constants.MAX)

        # populate list
        num_list.append(random_number)

    # call function
    max = find_max_value(num_list)

    # loop to display all numbers in list
    for counter_two in range(0, constants.SIZE):
        print("The random numbers are: {} ".format(num_list[counter_two]))

    # display max number
    print("The max is {}.".format(max))


if __name__ == "__main__":
    main()
