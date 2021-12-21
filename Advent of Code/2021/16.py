
# Started 04:27
# Finished 05:51

import re

f = open('2021/16.txt', 'r')
inputString = f.read()

#inputString = "9C0141080250320F1802104A08"
#inputString = "9C005AC2F8F0"

#inputString = "F600BC2D8F"

#inputString = "D8005AC2A8F0"
#inputString = "CE00C43D881120"
#inputString = "880086C3E88112"
#inputString = "04005AC33890"
#inputString = "C200B40A82"

zeroes = re.compile('0*')

def decipherPackets(bitstream, mode = 1):
    operations = []
    header = int(bitstream[:3], 2)
    pcktype = int(bitstream[3:6], 2)
    packet = bitstream[6:]
    if mode:
        if pcktype == 4: 
            literal = ''
            while int(packet[0]):
                literal += packet[1:5]
                packet = packet[5:]
            literal += packet[1:5]
            packet = packet[5:]
            operations.append([header, pcktype, int(literal, 2)])
            if zeroes.fullmatch(packet):
                return operations
            operations += decipherPackets(packet)
        else:
            if int(packet[0]):
                length = int(packet[1:12], 2)
                packet = packet[12:]
                sps = []
                while length:
                    sp = decipherPackets(packet, 0)
                    packet = sp[1]
                    sps += sp[0]
                    length -= 1
                operations.append([header, pcktype, sps])
                if zeroes.fullmatch(packet):
                    return operations
                operations += decipherPackets(packet)

            else:
                length = int(packet[1:16], 2)
                packet = packet[16:]
                operations.append([header, pcktype, decipherPackets(packet[:length])])
                if zeroes.fullmatch(packet[length:]):
                    return operations
                operations += decipherPackets(packet[length:])
        return operations
    else:
        if pcktype == 4: 
            literal = ''
            while int(packet[0]):
                literal += packet[1:5]
                packet = packet[5:]
            literal += packet[1:5]
            packet = packet[5:]
            operations.append([header, pcktype, int(literal, 2)])
            return (operations,packet)
        else:
            if int(packet[0]):
                length = int(packet[1:12], 2)
                packet = packet[12:]
                sps = []
                while length:
                    sp = decipherPackets(packet, 0)
                    packet = sp[1]
                    sps += sp[0]
                    length -= 1
                operations.append([header, pcktype, sps])
                return (operations,packet)

            else:
                length = int(packet[1:16], 2)
                packet = packet[16:]
                operations.append([header, pcktype, decipherPackets(packet[:length])])
                return (operations,packet[length:])

def countVersions(ops):
    count = 0
    count += ops[0][0]
    if isinstance(ops[0][2], list):
        for x in ops[0][2]:
            count += countVersions([x])
    return count

def evalOp(ops):
    value = 0
    oid = ops[0][1]
    if oid == 4:
        return ops[0][2]
    if oid == 0:
        for op in ops[0][2]:
            value += evalOp([op])
        return value
    if oid == 1:
        value = 1
        for op in ops[0][2]:
            value *= evalOp([op])
        return value
    if oid == 2:
        return min([evalOp([op]) for op in ops[0][2]])
    if oid == 3:
        return max([evalOp([op]) for op in ops[0][2]])
    if oid == 5:
        return evalOp([ops[0][2][0]]) > evalOp([ops[0][2][1]])
    if oid == 6:
        return evalOp([ops[0][2][0]]) < evalOp([ops[0][2][1]])
    if oid == 7:
        return evalOp([ops[0][2][0]]) == evalOp([ops[0][2][1]])


def partOne(i):
    bitstream = str(bin(int('1'+i, 16)))[3:]
    return countVersions(decipherPackets(bitstream))
    


def partTwo(i):
    bitstream = str(bin(int('1'+i, 16)))[3:]
    return evalOp(decipherPackets(bitstream))


print(partOne(inputString))

print(partTwo(inputString))
