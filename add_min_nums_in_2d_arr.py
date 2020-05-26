"""
Add up and print the sum of the all of the minimum elements of each inner array:

[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

The expected output is given by:

4 + -1 + 9 + -56 + 201 + 18 = 175

You may use whatever programming language you'd like.

Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
"""


def find_min_in_arr(a):
    min_num = a[0]
    for num in a[1:]:
        if min_num > num:
            min_num = num
    return min_num


def sum_of_arrays(arr):
    min_arr = [find_min_in_arr(a) for a in arr]
    total = 0
    for num in min_arr:
        total += num
    return total


test_arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

print(sum_of_arrays(test_arr))