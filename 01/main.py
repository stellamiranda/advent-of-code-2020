
def finf_two_num_sum(array, num):
    array.sort()
    i = 0
    j = len(array) - 1

    results = []
    while i < j:
        if array[i] + array[j] == num:
            print(array[i] * array[j])
            break
        elif array[i] < array[j] == num:
            i += 1
        else:
            j -= 1


def file_read(fname):
    content_array = []
    with open(fname) as f:
        for line in f:
                content_array.append(int(line))

    return content_array

data = file_read('input.txt')

finf_two_num_sum(data, 2020)