

p = open('proforma.py', 'r')
proforma = p.read()

years = [2023]
days = range(1, 26)

for y in years:
    for d in days:
        f = open(str(y) + '/' + ('', '0')[d < 10] + str(d) + '.py', 'w')
        open(str(y) + '/' + ('', '0')[d < 10] + str(d) + '.txt', 'x')

        f.write(proforma.replace('Year', str(y)).replace('Day', ('', '0')[d < 10] + str(d)))
