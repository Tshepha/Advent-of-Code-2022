# This is a sample Python script.


bag_input = open('baginput.txt')
bag_list = bag_input.read().split('\n')
print(bag_list)


def list_splitter(index):
    b_string = bag_list[index]
    b_length = int(len(b_string)/2)
    f_half = b_string[:b_length]
    s_half = b_string[b_length:]
    '''
    i = 0
    while i < b_length:
        if i < b_length/2:
            f_half.append(b_string[i])
        else:
            s_half.append(b_string[i])
        i = i + 1
    '''

    return f_half, s_half


def point_conversion(letter):
    letter_code = ord(letter)
    points = 0
    if letter_code > 96:
        points = letter_code - 96
    else:
        points = letter_code - 38
    return points


def string_compare(index):
    f_half, s_half = list_splitter(index)
    temp_points = 0
    for x in f_half:
        for y in s_half:
            if x == y:
                temp_points = point_conversion(x)
                break
        else:
            continue
        break
    return temp_points


def string_comparev2(index):
    f_bag = bag_list[index]
    s_bag = bag_list[index+1]
    t_bag = bag_list[index+2]
    temp_points = 0
    for x in f_bag:
        for y in s_bag:
            if x == y:
                for z in t_bag:
                    if y == z:
                        temp_points = point_conversion(y)
                        break
    return temp_points


total_points = 0
i = 0
while i < len(bag_list):
    total_points = total_points + string_compare(i)
    i = i + 1
print(total_points)


total_pointsv2 = 0
i = 0
while i < len(bag_list):
    if i+2 > len(bag_list):
        break
    else:
        total_pointsv2 = total_pointsv2 + string_comparev2(i)
        print(total_pointsv2)
        i = i + 3
