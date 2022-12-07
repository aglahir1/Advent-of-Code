
# Started
# Finished

from os import name
from typing import Sized


f = open('2022/07.txt', 'r')
inputString = f.read()

#inputString = """$ cd /
#$ ls
#dir a
#14848514 b.txt
#8504156 c.dat
#dir d
#$ cd a
#$ ls
#dir e
#29116 f
#2557 g
#62596 h.lst
#$ cd e
#$ ls
#584 i
#$ cd ..
#$ cd ..
#$ cd d
#$ ls
#4060174 j
#8033020 d.log
#5626152 d.ext
#7214296 k"""

global folders
global folderIndex
folderIndex = {}
folders = []

def backup():
    cF = folders[position]
    bF = cF.container
    if bF == None: return 0
    return bF.pos

def enter(nFn):
    cF = folders[position]
    for x in cF.contains:
        if x.name == nFn: return x.pos

class Folder:
    def __init__(self, name, container, pos):
        self.name = name
        self.container = container
        self.pos = pos
        self.contains = []
        self.size = 0

    def addFolder(self, name):
        global folders
        pos = len(folders)
        newFolder = Folder(name, self, pos)
        folders += [newFolder]
        self.contains += [newFolder]

    def addFile(self, name, size):
        self.contains += [File(name, size)]

    def getSize(self):
        if self.size > 0: return self.size
        calcsize = 0
        for x in self.contains:
            calcsize += x.getSize()
        self.size = calcsize
        return self.size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getSize(self):
        return self.size

    

def partOne():
    result = 0
    for x in folders:
        size = x.getSize()
        if size <= 100000: result += size
    return result
    

def partTwo():
    totalSize = 0
    sizes = []
    for x in folders:
        sizes.append(x.getSize())
    totalSize = folders[0].getSize()
    freeSpace = 70000000 - totalSize
    requiredSpace = 30000000
    necessarySpace = requiredSpace - freeSpace
    bigenough = []
    for x in sizes:
        if x >= necessarySpace: bigenough.append(x)
    bigenough.sort
    return bigenough[-1]


inputArray = inputString.splitlines()

position = 0

folders += [Folder('/', None, 0)]


for code in inputArray:
    code = code.split()
    if code[0] == '$':
        if code[1] == 'cd':
            if code[2] == '..':
                position = backup()
            else:
                if enter(code[2]): position = enter(code[2])
        elif code[1] == 'ls': continue
    else:
        if code[0] == 'dir': folders[position].addFolder(code[1])
        else: folders[position].addFile(code[1], int(code[0]))



print(partOne())

print(partTwo())
