quation = '3x^3-4x^2+2x-3=0' #(2) 1, -7, 12, 0

coef = []
degrees = ['x^3', 'x^2', 'x', '=']

def findDist(quation):
    try:
        indexes = [quation.find('-'), quation.find('+')]
        index = min([i for i in indexes if i>0])
        if index != 0:
            return index
        
        indexes = [quation[1:].find('-'), quation[1:].find('+')]
        index = min([i for i in indexes if i>0]) + 1
        return index
    except ValueError: return -1

for degree in degrees:
    coef.append(quation[:quation.find(degree)])
    quation = quation[findDist(quation):]

param = [i-20 for i in range(41)]

coef = [int(i) for i in coef]

def calcGorner(coef, num):
    value_list = [coef[0]]
    for i in range(3):
        value_list.append(num * value_list[i] + coef[i+1])
    return value_list

root_list = []

for number in param:
    if 0 == calcGorner(coef, number)[-1]:
        root_list.append(number)
    #print( number, ':', calcGorner(coef, number) )

print(root_list)