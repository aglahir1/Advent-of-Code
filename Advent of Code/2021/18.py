
# Started
# Finished

import math
import ast
import copy

f = open('2021/18.txt', 'r')
inputString = f.read()

def depth(sn):
    if isinstance(sn, list):
        return 1 + max([depth(x) for x in sn])
    else:
        return 0

def any10s(sn):
    for ia, a in enumerate(sn):
        if isinstance(a, list):
            for ib, b in enumerate(a):
                if isinstance(b, list):
                    for ic, c in enumerate(b):
                        if isinstance(c, list):
                            for lid, d in enumerate(c):
                                if isinstance(d, list):
                                    for x in d:
                                        if isinstance(x, int):
                                            if x > 9: return True
                                elif d > 9: return True
                        elif c > 9: return True
                elif b > 9: return True
        elif a > 9: return True
    return False

def reduce(sn):
    while depth(sn) > 4 or any10s(sn):
        if depth(sn) > 4:
            exploded = False
            for ia, a in enumerate(sn):
                if exploded: break
                if isinstance(a, list):
                    for ib, b in enumerate(a):
                        if exploded: break
                        if isinstance(b, list):
                            for ic, c in enumerate(b):
                                if exploded: break
                                if isinstance(c, list):
                                    for lid, d in enumerate(c):
                                        if exploded: break
                                        if isinstance(d, list):
                                            exploded = True
                                            if ia or ib or ic or lid:
                                                if lid:
                                                    sn[ia][ib][ic][0] += d[0]
                                                elif ic:
                                                    if isinstance(b[0], list): sn[ia][ib][0][1] += d[0]
                                                    else: sn[ia][ib][0] += d[0]
                                                elif ib:
                                                    if isinstance(a[0], list):
                                                        if isinstance(a[0][1], list): sn[ia][0][1][1] += d[0]
                                                        else: sn[ia][0][1] += d[0]
                                                    else: sn[ia][0] += d[0]
                                                elif ia:
                                                    if isinstance(sn[0], list):
                                                        if isinstance(sn[0][1], list):
                                                            if isinstance(sn[0][1][1], list): sn[0][1][1][1] += d[0]
                                                            else: sn[0][1][1] += d[0]
                                                        else: sn[0][1] += d[0]
                                                    else: sn[0] += d[0]
                                            if not (ia and ib and ic and lid):
                                                if not lid:
                                                    if isinstance(c[1], list): sn[ia][ib][ic][1][0] += d[1]
                                                    else: sn[ia][ib][ic][1] += d[1]
                                                elif not ic:
                                                    if isinstance(b[1], list): 
                                                        if isinstance(b[1][0], list): sn[ia][ib][1][0][0] += d[1]
                                                        else: sn[ia][ib][1][0] += d[1]
                                                    else: sn[ia][ib][1] += d[1]
                                                elif not ib:
                                                    if isinstance(a[1], list):
                                                        if isinstance(a[1][0], list): 
                                                            if isinstance(a[1][0][0], list): sn[ia][1][0][0][0] += d[1]
                                                            else:  sn[ia][1][0][0] += d[1]
                                                        else: sn[ia][1][0] += d[1]
                                                    else: sn[ia][1] += d[1]
                                                elif not ia:
                                                    if isinstance(sn[1], list):
                                                        if isinstance(sn[1][0], list):
                                                            if isinstance(sn[1][0][0], list): 
                                                                if isinstance(sn[1][0][0][0], list): sn[1][0][0][0][0] += d[1]
                                                                else: sn[1][0][0][0] += d[1]
                                                            else: sn[1][0][0] += d[1]
                                                        else: sn[1][0] += d[1]
                                                    else: sn[1] += d[1]
                                            sn[ia][ib][ic][lid] = 0
        else: 
            splitted = False
            for ia, a in enumerate(sn):
                if splitted: break
                if isinstance(a, list):
                    for ib, b in enumerate(a):
                        if splitted: break
                        if isinstance(b, list):
                            for ic, c in enumerate(b):
                                if splitted: break
                                if isinstance(c, list):
                                    for lid, d in enumerate(c):
                                        if splitted: break
                                        if d > 9:
                                            splitted = True
                                            sn[ia][ib][ic][lid] = [math.floor(d / 2), math.ceil(d / 2)]
                                elif c > 9:
                                    splitted = True
                                    sn[ia][ib][ic] = [math.floor(c / 2), math.ceil(c / 2)]
                        elif b > 9:
                            splitted = True
                            sn[ia][ib] = [math.floor(b / 2), math.ceil(b / 2)]
                elif a > 9:
                    splitted = True
                    sn[ia] = [math.floor(a / 2), math.ceil(a / 2)]
    return sn

def calcMagnitude(sn):
    if isinstance(sn[0], list): rs = calcMagnitude(sn[0])
    else: rs = sn[0]
    if isinstance(sn[1], list): ls = calcMagnitude(sn[1])
    else: ls = sn[1]
    return 3*rs + 2*ls

def partOne(i):
    sn = copy.deepcopy(i).pop(0)
    for add in i[1:]:
        sn = [sn, copy.deepcopy(add)]
        sn = reduce(sn)
    return calcMagnitude(sn)

def partTwo(i):
    topMagnitude = [[],[],0]
    for sn in i:
        for sn2 in i:
            if sn == sn2: continue
            tester = [copy.deepcopy(sn), copy.deepcopy(sn2)]
            tester = reduce(tester)
            test = calcMagnitude(tester)
            if test > topMagnitude[2]: topMagnitude = [sn, sn2, test]
    return topMagnitude

#inputString = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
#inputString = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
#inputString = [[6,[5,[4,[3,2]]]],1]
#inputString = [7,[6,[5,[4,[3,2]]]]]
#inputString = [[[[[9,8],1],2],3],4]
#inputString = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
#[[[5,[2,8]],4],[5,[[9,9],0]]]
#[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
#[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
#[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
#[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
#[[[[5,4],[7,7]],8],[[8,3],8]]
#[[9,3],[[9,9],[6,[4,9]]]]
#[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
#[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

inputArray = inputString.splitlines()

inputs = [list(ast.literal_eval(i)) for i in inputArray]

print(partOne(inputs))

print(partTwo(inputs))
