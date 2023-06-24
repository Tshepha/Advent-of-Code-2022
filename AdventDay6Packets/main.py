# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#importing string
string_input = open('stringinput.txt').read()
#print(string_input)


def marker_finder(string):
    first_marker = 4
    string_length = len(string)
    i = 4
    while i < string_length:
        a = string[i - 4]
        b = string[i - 3]
        c = string[i - 2]
        d = string[i - 1]
        if a != b and a != c and a != d and b != c and b != d and c != d:
            break
        first_marker = first_marker + 1
        i = i + 1
    return first_marker


def message_finder(string):
    first_message = 14
    string_length = len(string)
    i = 0
    while i < string_length:
        z = i
        bool1 = 0
        while z < i + 13:
            if string.count(string[z], i, i + 14) > 1:
                bool1 = 1
                break
            z = z + 1
        if bool1 == 0:
            return first_message
        first_message = first_message + 1
        i = i + 1

"""
testing various inputs
test_string1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
test_string2 = 'nppdvjthqldpwncqszvftbrmjlhg'
test_string3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
test_string4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
print(marker_finder(test_string1))
print(marker_finder(test_string2))
print(marker_finder(test_string3))
print(marker_finder(test_string4))
test_string5 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
test_string6 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
print(message_finder(test_string5))
print(message_finder(test_string6))
"""
print(marker_finder(string_input))


print(message_finder(string_input))