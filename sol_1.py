# If we only have one register, it does not matter what order they go the time taken is constant

# %%
from ast import arg
import sys
args = sys.argv
if len(args) > 2:
    print('Error: Too many arguments entered')
    exit()
else:
    file = args[1]
global t
t = 0


def onlyOneRegister(struct):
    total = 1
    for line in struct:
        total += int(line[2]) * 2
    print(f'Total time for One register: {total}min')


# Returns the position of the first empty register
def where(arr):
    for i in range(len(arr)):
        if not arr[i]:
            return i


# Customer Type A always chooses the register with the shortest
# line(least number of customers in line). If two or more registers
# have the shortest line, Customer Type A will choose the register
# with the lowest register number


def getPosTypeA(arr):
    # Set the 'shortest' line to the first elem
    # If there are no customers in line then return the first pos
    if arr == None:
        return 0
    temp = len(arr[0])
    idx = 0
    # Loop through the arr find the shortest line, return position
    for i in range(len(arr)):
        if len(arr[i]) < temp:
            idx = i
    return idx


# Customer Type B looks at the last customer in each line,
# and always chooses to be behind the customer with the fewest
# number of items left to check out, regardless of how many
# other customers are in the line or how many items they have.
# Customer Type B will always choose an empty line before a line with any customers in it.


def getPosTypeB(arr):
    # Set the temporary to compare against and the position of that item
    # If there is an empty position, return it.
    temp = 0
    idx = 0
    if min(arr) == []:
        return arr.index(min(arr))
    # Else loop through the list, get smallest last customer return that position
    else:
        for i in range(0, len(arr)):
            if arr[i][-1] < temp:
                temp = arr[i][-1]
                idx = i
    return idx


with open(file) as inFile:
    data = inFile.read()
splits = data.splitlines()
registers = [[] for _ in range(int(splits.pop(0)[0]))]
fmtStrut = []
for i in range(0, len(splits)):
    fmtStrut.append(splits[i].split())


def popCustomer(cust):
    if registers == None:
        return 0
    if cust[0] == 'A':
        pos = getPosTypeA(registers)
        registers[pos].append(int(cust[2]))
        fmtStrut.remove(cust)
    else:
        pos = getPosTypeB(registers)
        registers[pos].append(int(cust[2]))
        fmtStrut.remove(cust)


def moveTime(arr):
    global t
    if any(arr):
        for i in range(len(arr)):
            if not arr:
                break
            elif len(arr[i]) >= 1 and arr[i] != []:
                temp = arr[i][0] - 1
                if arr[i] == arr[-1]:
                    if temp != 0:
                        arr[i].pop(0)
                        arr[i].insert(0, temp)
                        t += 2
                    else:
                        arr[i].pop(0)
                elif temp != 0:
                    arr[i].pop(0)
                    arr[i].insert(0, temp)
                    t += 1
                else:
                    arr[i].pop(0)
        return arr


# Simulation starts
t += 1
if len(registers) > 1:
    while registers:
        if len(fmtStrut) == 1:
            popCustomer(fmtStrut[0])
        elif fmtStrut:
            cust1 = fmtStrut[0]
            cust2 = fmtStrut[1]
            # if the customers are not the same type and  at different times
            # then we can just process them as normal
            if cust1[1] != cust2[1]:
                # Add cust1 and cust2 items to the queue
                popCustomer(cust1)
                popCustomer(cust2)
            elif cust1[1] == cust2[1]:
                if cust1[2] < cust2[2]:
                    print(f'Cust1 has less items: {cust1[2]} < {cust2[2]}')
                    popCustomer(cust1)
                    popCustomer(cust2)
                elif cust2[2] < cust1[2]:
                    print(f'Cust2 has less items: {cust2[2]} < {cust1[2]}')
                    popCustomer(cust2)
                    popCustomer(cust1)
                else:
                    print(fmtStrut)

                    if cust1[0] == 'A':
                        popCustomer(cust1)
                        popCustomer(cust2)
                        # Prcess cust 1 as type A, cust2 as type B
                    else:
                        # Process cust1 as typeB and and Cust2 as type A
                        print(f'Process cust1 as typeB and and Cust2 as type A')
                        popCustomer(cust1)
                        popCustomer(cust2)
            else:
                print(f'Uncaught logic branch')
        else:
            registers = moveTime(registers)
    print(f'Time: {t}')
else:
    onlyOneRegister(fmtStrut)

# %%
