import subprocess

toDo = input("What would you like to do?")


def insulin():
    exec(open('insulin.py').read())

def bloodpressure():
    exec(open('bloodpressure.py').read())

def controler(userinput):
    switcher={
        'insulin': insulin(),
        'bp': bloodpressure()
    }
    print(switcher[userinput])
    return switcher[userinput]

print(toDo)
controler(toDo)

class Patient:
    def __init__(self, room):
        self.room = room
        self.bps = []
        self.insulins = []

    def addBP(record):
        self.bps.append(record)
    
    def addInsulin(record):
        self.insulins.append(record)

