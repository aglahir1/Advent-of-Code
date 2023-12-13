
# Started
# Finished

import re


f = open('2017/20.txt', 'r')
inputString = f.read()

class Particle:
    
    def __init__(self, x, y, z, vx, vy, vz, ax, ay, az):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.vx = int(vx)
        self.vy = int(vy)
        self.vz = int(vz)
        self.ax = int(ax)
        self.ay = int(ay)
        self.az = int(az)
        
    def tick(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        

def partOne(i):
    particles = []
    minAccel = 0
    for x, l in enumerate(i):
        l = [abs(int(j)) for j in l.split(', a=<')[1][:-1].split(',')]
        accel = sum(l)
        if accel < minAccel:
            minAccel = accel
            particles = [x]
        elif accel == minAccel:
            particles.append(x)
    return particles
        
        

def partTwo(i: list[str]):
    particles: dict[int, Particle] = {}
    for x, p in enumerate(i):
        parse = re.search('p=<([^>]+)>, v=<([^>]+)>, a=<([^>]+)>', p)
        pos = parse.group(1).split(',')
        vel = parse.group(2).split(',')
        acc = parse.group(3).split(',')
        particles[x] = Particle(pos[0], pos[1], pos[2], vel[0], vel[1], vel[2], acc[0], acc[1], acc[2])
    positions: list[list] = []
    removed: list[list[int]] = []
    for k in particles:
        p = particles[k]
        if [p.x, p.y, p.z] in removed:
            particles.pop(k)
            continue
        if [p.x, p.y, p.z] in [t[0] for t in positions]:
            removed.append([p.x, p.y, p.z])
            indx = [t[0] for t in positions].index(p.x, p.y, p.z)
            toRemove = positions[indx][1]
            positions.pop(indx)
            particles.pop(toRemove)
            particles.pop(k)
            continue
        positions.append([[p.x, p.y, p.z], k])
    for r in range(50):
        positions: list[list] = []
        removed: list[list[int]] = []
        toRemove = []
        for k in particles:
            p = particles[k]
            p.tick()
            if [p.x, p.y, p.z] in removed:
                toRemove.append(k)
                continue
            if [p.x, p.y, p.z] in [t[0] for t in positions]:
                removed.append([p.x, p.y, p.z])
                indx = [t[0] for t in positions].index([p.x, p.y, p.z])
                toRemove.append(positions[indx][1])
                toRemove.append(k)
                positions.pop(indx)
                continue
            positions.append([[p.x, p.y, p.z], k])
        for x in toRemove:
            particles.pop(x)
    return len(particles)
            

inputArray = inputString.splitlines()

print(partOne(inputArray))

print(partTwo(inputArray))
