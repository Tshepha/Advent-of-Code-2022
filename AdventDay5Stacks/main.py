# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
test_string = 'abcde'
test_list = list(test_string)
print(test_list)
test_list.pop()
print(test_list.append('e'))
nested_list = [0, 1, [2, 3], 4]
print(nested_list)
nested_list[2].pop(1)
print(nested_list)
"""
stack_input = open('stackinput.txt').read()
order_input = open('orderinput.txt').read()

line_input = open('stackinput.txt').readline()
line_length = len(line_input)
stack_length = len(stack_input)

print(stack_input)
print(line_input)
print(line_length)
print(stack_length)

temp_stack = []

i = 0

while i < line_length:
    temp_stack.append([])
    i = i + 1

#initilize temp
i = 0
y = 0
while i < stack_length:
    temp_stack[y].append(stack_input[i])
#    z = len(stack_input[y])
#    print(temp_stack[y][z-1])

    if y == 35:
        y = 0
    else:
        y = y + 1
    i = i + 1


#clean temp
temp_stack2 = []
i = 1
while i < line_length:
    temp_stack2.append(temp_stack[i])
    i = i + 4
print(temp_stack2)

#used to find total length of a nested list
def nested_list_count(the_list):
    length1 = len(the_list)
    total_length = 0
    i = 0
    while i < length1:
        total_length = total_length + len(the_list[i])
        i = i + 1
    return total_length


#make real list
real_stack = []
i = 0
while i < len(temp_stack2):
    real_stack.append([])
    i = i + 1
#append real list
y = 0
i = 0
j = nested_list_count(temp_stack2)
while i < j:
    z = temp_stack2[y][-1]
    #print(z)
    #if z == ' ':
    #    temp_stack2[y].pop()
    #    z = temp_stack2[y][-1]
    if z != ' ':
        real_stack[y].append(z)
        temp_stack2[y].pop()
    else:
        temp_stack2[y].pop()
    if y == len(temp_stack2)-1:
        y = 0
    else:
        y = y + 1
    i = i + 1


print(real_stack)

#---------------------------------------------------------------------------
order_input_2 = order_input.replace('move', '')
order_input_2 = order_input_2.replace(' ', '')
order_parse_1 = order_input_2.split('\n')
print(order_parse_1)
temp_order_length = len(order_parse_1)
print(temp_order_length)
real_order = []

#tempthing = order_parse_1[0].split('from')
#tempthing2 = tempthing[1].split('to')
#print(tempthing)
#print(tempthing2)

for x in order_parse_1:
    if x == '':
        break
    temp_strthing = x.split('from')
    temp_strthing_2 = temp_strthing[1].split('to')
    a = temp_strthing[0]
    b = temp_strthing_2[0]
    c = temp_strthing_2[1]
    real_order.append([a, b, c])
print(real_order)


#---------------------------------------------------------------------------

def stack_reorg(stack, order):
    for x in order:
        first = int(x[0])
        second = int(x[1])
        third = int(x[2])
        i = 0
        while i < first:
            stack[third-1].append(stack[second-1].pop())
            i = i + 1
    return stack


def stack_reorg2(stack, order):
    for x in order:
        first = int(x[0])
        second = int(x[1])
        third = int(x[2])
        i = 0
        while i < first:
            z = -(first - i)
            stack[third-1].append(stack[second-1].pop(z))
            i = i + 1
    return stack

from copy import deepcopy


print(real_stack)
real_stack2 = deepcopy(real_stack)
print(real_stack2)
finished_stack = stack_reorg(real_stack, real_order)
print(finished_stack)
for x in finished_stack:
    print(x[-1])
print("stuff")
print(real_stack2)
finished_stack2 = stack_reorg2(real_stack2, real_order)
print(finished_stack2)
for x in finished_stack2:
    print(x[-1])
