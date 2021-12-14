

p = open('proforma.py', 'r')
proforma = p.read()

years = [2021]
days = [14]

for y in years:
    for d in days:
        if y == 2016 and d in (2, 1): continue
        f = open(str(y) + '/' + ('', '0')[d < 10] + str(d) + '.py', 'w')
        open(str(y) + '/' + ('', '0')[d < 10] + str(d) + '.txt', 'x')

        f.write(proforma.replace('Year', str(y)).replace('Day', ('', '0')[d < 10] + str(d)))
