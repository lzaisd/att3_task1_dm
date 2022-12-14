import math


def read_from_file(file):
    data = []
    with open(file) as f:
        line = f.readline()
        data.extend([int(x) for x in line.split()])

    return data


def write_to_file(data, num1, num2, file):
    f = open(file, 'w')
    for i in range(len(data)):
        f.write(str(data[i]) + " ")
    f.write("\n" + str(num1) + " " + str(num2))


def shell_sort_first(array):
    n = len(array)
    s = int(math.log2(n))
    gap = 1
    c = 0
    while gap > 0:
        for i in range(gap, n):
            cur_elem = array[i]
            j = i
            while j >= gap and array[j - gap] > cur_elem:
                c += 1
                array[j] = array[j - gap]
                j -= gap
            array[j] = cur_elem
        s -= 1
        gap = 2 ** (s + 1) - 1
    return array, c


def shell_sort_second(array):
    n = len(array)
    s = int(math.log2(n))
    gap = 1
    c = 0
    while gap > 0:
        for i in range(gap, n):
            cur_elem = array[i]
            j = i
            while j >= gap and array[j - gap] > cur_elem:
                c += 1
                array[j] = array[j - gap]
                j -= gap
            array[j] = cur_elem
        s -= 1
        gap = (3 ** (s + 1) - 1) // 2
    return array, c


sorted_arr1, count1 = shell_sort_first(read_from_file('input.txt'))
sorted_arr2, count2 = shell_sort_second(read_from_file('input.txt'))
write_to_file(sorted_arr1, count1, count2, 'output.txt')