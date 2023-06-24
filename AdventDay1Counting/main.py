# This is a sample Python script.


#import csv
#import numpy as np


#test_array = np.array([1, 2, 3, 4])
#print(test_array[0])


elf_input = open("ElfTestInput.txt", "r")
#print(elf_input.readlines())


elf_list = elf_input.read().split('\n')
#print(elf_list)

#final_elf_list = csv.reader(elf_list, delimiter=",")
final_elf_list = []
#print(final_elf_list[0])
#np.append(final_elf_array,[24])


count = 0
for x in elf_list:
    if x == '':
        final_elf_list.append(count)
        count = 0
    else:
        count = count + int(x)
print(final_elf_list)

final_elf_list_sorted = final_elf_list.copy()
final_elf_list_sorted.sort(reverse=True)
print(final_elf_list_sorted)
highest_value = final_elf_list_sorted[0]
print(highest_value)
highest_value_index = final_elf_list.index(highest_value)
print(highest_value_index)
print(final_elf_list[127])

print(highest_value_index+1,' is the elf with the most calories')
