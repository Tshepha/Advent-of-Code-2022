# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


schedule_input = open('input.txt').read().replace('\n', ',')
schedule_inputv2 = schedule_input.split(',')

print(schedule_inputv2)


def schedule_compare(index):
    f_sched = schedule_inputv2[index].split('-')
    other_index = index + 1
    s_sched = schedule_inputv2[other_index].split('-')
    pairs = 0
    if int(f_sched[0]) <= int(s_sched[0]) and int(f_sched[1]) >= int(s_sched[1]):
        pairs = 1
    elif int(s_sched[0]) <= int(f_sched[0]) and int(s_sched[1]) >= int(f_sched[1]):
        pairs = 1
    return pairs


total_pairs = 0
i = 0
while i < len(schedule_inputv2):
    if i + 1 >= len(schedule_inputv2):
        break
    total_pairs = total_pairs + schedule_compare(i)
    #print(total_pairs)
    i += 2

print(total_pairs)


def schedule_comparev2(index):
    f_sched = schedule_inputv2[index].split('-')
    other_index = index + 1
    s_sched = schedule_inputv2[other_index].split('-')
    overlap = 0
    if int(f_sched[0]) <= int(s_sched[0]) and int(f_sched[1]) >= int(s_sched[0]):
        overlap = 1
    elif int(s_sched[0]) <= int(f_sched[0]) and int(s_sched[1]) >= int(f_sched[0]):
        overlap = 1
    return overlap


total_overlap = 0
i = 0
while i < len(schedule_inputv2):
    if i + 1 >= len(schedule_inputv2):
        break
    total_overlap = total_overlap + schedule_comparev2(i)
    #print(total_overlap)
    i += 2
print(total_overlap)
