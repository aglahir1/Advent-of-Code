
# Started
# Finished

from math import floor


pInput = 3005290

# pInput = 5

class Circle:
    def __init__(self, size: int):
        self.seats = size
        self.elves = list(range(1, size + 1))
        self.stealer = 0
    
def partOne(i):
    circle = list(range(i))
    while len(circle) > 1:
        if len(circle) % 2 == 0:
            circle = circle[::2]
        else:
            circle = [circle[-1]] + circle[:-1:2]
    return circle[0] + 1

def partTwo(i):
    circle = Circle(i)
    cycle = 0
    while circle.seats > 1:
        kickee = (circle.stealer + floor(circle.seats / 2)) % circle.seats
        circle.elves.pop(kickee)
        circle.seats -= 1
        circle.stealer = (circle.stealer + [0, 1][kickee > circle.stealer]) % circle.seats
        cycle += 1
        if cycle % 3000 == 0: print(cycle / 30000, '/ 100')
    return circle.elves[0]
        
        
print(partOne(pInput))

print(partTwo(pInput))
