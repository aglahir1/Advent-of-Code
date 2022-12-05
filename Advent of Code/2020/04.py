
# Started
# Finished

f = open('2020/04.txt', 'r')
inputString = f.read()

#inputString = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
#byr:1937 iyr:2017 cid:147 hgt:183cm

#iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
#hcl:#cfa07d byr:1929

#hcl:#ae17e1 iyr:2013
#eyr:2024
#ecl:brn pid:760753108 byr:1931
#hgt:179cm

#hcl:#cfa07d eyr:2025 pid:166559648
#iyr:2011 ecl:brn hgt:59in"""

def partOne(i):
    valid = 0
    for p in i:
        if all(key in p.keys() for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']): valid += 1
    return valid

def partTwo(i):
    valid = 0
    for p in i:
        if all(key in p.keys() for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']): 
            if 1920 <= int(p['byr']) <= 2002: 
                if 2010 <= int(p['iyr']) <= 2020:
                    if 2020 <= int(p['eyr']) <= 2030:
                        if p['hgt'][-2:] in ['cm', 'in']:
                            if (150 <= int(p['hgt'][:-2]) <= 193 and p['hgt'][-2:] == 'cm') or (59 <= int(p['hgt'][:-2]) <= 76 and p['hgt'][-2:] == 'in'):
                                if p['hcl'][0] == '#' and all(figure in 'abcdef0123456789' for figure in p['hcl'][1:]) and len(p['hcl']) == 7:
                                    if p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                        if len(p['pid']) == 9 and all(c in '0123456789' for c in p['pid']): valid += 1
    return valid


inputArray = inputString.split('\n\n')
inputArray = [{j.split(':')[0]: j.split(':')[1] for j in x.replace('\n', ' ').split(' ')} for x in inputArray]

print(partOne(inputArray))

print(partTwo(inputArray))
