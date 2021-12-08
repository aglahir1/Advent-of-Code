
#Started 17:20
#Finished 17:55

inputString = """Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds."""

inputString = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""

inputArray = inputString.splitlines()

reindeer = []

for entry in inputArray:
    entry = entry.split()
    deer = [entry[0], [int(entry[3]), int(entry[6])], int(entry[-2]), True, int(entry[6]), 0, 0]
    reindeer.append(deer)



racetime = 2503

racetime = 1000

times = []

for x in reindeer:
    rt = racetime
    distance = 0
    while rt > 0:
        if rt < x[1][1]: distance += rt * x[1][0]
        else: distance += x[1][1] * x[1][0]
        rt -= x[1][1]
        rt -= x[2]

    times.append([x[0], distance])

times.sort(key = lambda x: x[1])

print(times)



while racetime:

    for x in reindeer:
        if x[3]:
            x[5] += x[1][0]
        x[4] -= 1
        if not x[4]:
            x[3] = not x[3]
            x[4] = (x[2],x[1][1])[x[3]]
    reindeer.sort(key = lambda x: x[5])
    reindeer[-1][6] += 1
    racetime -= 1

times = []
for x in reindeer:
    times.append([x[0], x[5], x[6]])

times.sort(key = lambda x: x[2])
print(times)