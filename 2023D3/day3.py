def parse_input(filepath):
    line_list = []
    file = open(filepath, 'r')
    while True:
        line = file.readline()
        if not line:
            return line_list
        line_list.append(line.strip())


def check_part_num(row_num, start_index, end_index, array):
    if start_index-1 >= 0:
        if array[row_num][start_index-1] != '.':
            return True
    if end_index + 1 < len(array[row_num]):
        if array[row_num][end_index+1] != '.':
            return True
    if row_num-1 >= 0:
        if start_index-1 >= 0:
            if array[row_num-1][start_index-1] != '.' and not array[row_num-1][start_index-1].isnumeric():
                return True
        if end_index + 1 < len(array[row_num]):
            if array[row_num-1][end_index+1] != '.' and not array[row_num-1][end_index+1].isnumeric():
                return True
        for current_index in range(start_index, end_index+1):
            if array[row_num-1][current_index] != '.' and not array[row_num-1][current_index].isnumeric():
                return True
    if row_num+1 < len(array):
        if start_index-1 >= 0:
            if array[row_num+1][start_index-1] != '.' and not array[row_num+1][start_index-1] .isnumeric():
                return True
        if end_index + 1 < len(array[row_num]):
            if array[row_num+1][end_index+1] != '.' and not array[row_num+1][end_index+1].isnumeric():
                return True
        for current_index in range(start_index, end_index+1):
            if array[row_num+1][current_index] != '.' and not array[row_num+1][current_index].isnumeric():
                return True
    return False


# line_list = parse_input('test_input.txt')
line_list = parse_input('input.txt')

part_number_sum = 0
for row_num, line in enumerate(line_list):
    current_num = 0
    num_start_index = 0
    num_end_index = 0
    for col_num, element in enumerate(line):
        if element.isnumeric():
            if (current_num == 0):
                num_start_index = col_num
            current_num = current_num*10+int(element)
            if col_num+1 == len(line_list[row_num]):
                num_end_index = len(line_list[row_num])-1
                # if row_num == 115:
                #     print(
                #         f"current_num={current_num},row_num={row_num},num_start_index={num_start_index},num_end_index={num_end_index}")

                if check_part_num(row_num, num_start_index,
                                  num_end_index, line_list):
                    # if row_num == 115:
                    #     print("true\n")
                    part_number_sum += current_num
                current_num = 0

        else:
            if current_num != 0:
                num_end_index = col_num - 1
                if row_num == 88:
                    print(
                        f"current_num={current_num},row_num={row_num},num_start_index={num_start_index},num_end_index={num_end_index}")

                if check_part_num(row_num, num_start_index,
                                  num_end_index, line_list):
                    if row_num == 88:
                        print("true\n")
                    part_number_sum += current_num
                current_num = 0
print(part_number_sum)
