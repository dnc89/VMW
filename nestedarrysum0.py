"""
Input array find the sequence making sum to 0
[1,-1,4,6,7,845,7,8,9,1,0,-5,-8,3]

input:
x = [1, -1, 4, 6, 7, 845, 7, 8, 9, 1, 0, -5, -8, 3, 2, 7, 8, 7, 5, 5, 0]
output:
[[-8, -1, 9], [-8, 0, 8], [-8, 1, 7], [-8, 2, 6], [-8, 3, 5], [-5, -1, 6],
 [-5, 0, 5], [-5, 1, 4], [-5, 2, 3], [-1, 0, 1]]
"""


def get_the_list(list1):
    all_lists = []
    sorted_list = sorted(list1)
    print(sorted_list)
    # As we are going to take l and r , to get rid of index out of range we need
    # to loop till -2 position of array
    for i in range(len(sorted_list) - 2):
        if i > 0 and sorted_list[i] == sorted_list[i - 1]:
            continue
        l = i + 1
        r = len(sorted_list) - 1

        while l < r:
            total = sorted_list[i] + sorted_list[l] + sorted_list[r]
            if total < 0:
                l = l + 1
            elif total > 0:
                r = r - 1
            else:
                temp_list = [sorted_list[i], sorted_list[l], sorted_list[r]]
                all_lists.append(temp_list)
                while l < r and sorted_list[l] == sorted_list[l+1]:
                    l = l + 1
                while l < r and sorted_list[r] == sorted_list[r-1]:
                    r = r - 1
                l = l + 1
                r = r - 1

    print("***")
    print(all_lists)

    return True


x = [1, -1, 4, 6, 7, 845, 7, 8, 9, 1, 0, -5, -8, 3, 2, 7, 8, 7, 5, 5, 0]

get_the_list(x)
