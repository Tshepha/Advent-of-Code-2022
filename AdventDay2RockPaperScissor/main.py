# This is a sample Python script.


RPSinput = open('rpsInput.txt')
RPSone = RPSinput.read().replace(' ', '\n')
#print(RPSone)
RPStwo = RPSone.split('\n')
print(RPStwo)

rps_opponent = []
rps_yourself = []

i = 0
while i < len(RPStwo):
#    print(RPStwo[i])
    rps_opponent.append(RPStwo[i])
    i = i+2
rps_opponent.pop()
print(rps_opponent)

i = 1
while i < len(RPStwo):
    rps_yourself.append(RPStwo[i])
    i = i+2
print(rps_yourself)

def rps_outcome(index):
    if rps_opponent[index] == 'A':
        return rps_outcomea(index)
    elif rps_opponent[index] == 'B':
        return rps_outcomeb(index)
    elif rps_opponent[index] == 'C':
        return rps_outcomec(index)

def rps_outcomea(index):
    points = 0
    if rps_yourself[index] == 'X':
        points += 1
        points += 3
        return points
    elif rps_yourself[index] == 'Y':
        points += 2
        points += 6
        return points
    elif rps_yourself[index] == 'Z':
        points += 3
        points += 0
        return points

def rps_outcomeb(index):
    points = 0
    if rps_yourself[index] == 'X':
        points += 1
        points += 0
        return points
    elif rps_yourself[index] == 'Y':
        points += 2
        points += 3
        return points
    elif rps_yourself[index] == 'Z':
        points += 3
        points += 6
        return points

def rps_outcomec(index):
    points = 0
    if rps_yourself[index] == 'X':
        points += 1
        points += 6
        return points
    elif rps_yourself[index] == 'Y':
        points += 2
        points += 0
        return points
    elif rps_yourself[index] == 'Z':
        points += 3
        points += 3
        return points

total_points = 0
i = 0
while i < len(rps_opponent):
    total_points = total_points + rps_outcome(i)
    i = i + 1

print(total_points)
# version 2
#
#
#
#
def rps_outcomev2(index):
    if rps_opponent[index] == 'A':
        return rps_outcomeav2(index)
    elif rps_opponent[index] == 'B':
        return rps_outcomebv2(index)
    elif rps_opponent[index] == 'C':
        return rps_outcomecv2(index)

def rps_outcomeav2(index):
    points = 0
    if rps_yourself[index] == 'X':
        points += 3
        points += 0
        return points
    elif rps_yourself[index] == 'Y':
        points += 1
        points += 3
        return points
    elif rps_yourself[index] == 'Z':
        points += 2
        points += 6
        return points

def rps_outcomebv2(index):
    points = 0
    if rps_yourself[index] == 'X':
        points += 1
        points += 0
        return points
    elif rps_yourself[index] == 'Y':
        points += 2
        points += 3
        return points
    elif rps_yourself[index] == 'Z':
        points += 3
        points += 6
        return points

def rps_outcomecv2(index):
    points = 0
    if rps_yourself[index] == 'X':
        points += 2
        points += 0
        return points
    elif rps_yourself[index] == 'Y':
        points += 3
        points += 3
        return points
    elif rps_yourself[index] == 'Z':
        points += 1
        points += 6
        return points

total_points = 0
i = 0
while i < len(rps_opponent):
    total_points = total_points + rps_outcomev2(i)
    i = i + 1
print(total_points)

thingy = 'A'
thinge = ord(thingy)
print(thinge)