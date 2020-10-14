from datetime import datetime
import writeRecord

patientID = input("Patient room #: ")

writeRecord.newPatient(patientID)
priorBG = int(input("Prior blood glucose: "))
currentBG = int(input("Current blood glucose: "))
currentRate = float(input("Current rate: "))

currentRanges = [[85, 0], [100, 1], [120, 2], [140, 3], [160, 4], [175, 5], [200, 6], [225, 7], [250, 8], [275, 9], [300, 10], [325, 11], [350, 12], [375, 13], [400, 14], [450, 15], [1000, 16]]


def getRanges(BG, ranges):
    for i in range(0, len(ranges)):
        if ranges[0][0] > BG:
            return 0
        elif (ranges[i][0] <= BG) and (ranges[i+1][0] >= BG):
            return i+1
            break

def getPriorRanges(currentRange):
    switcher={
        0: [[0, 0.0]],
        1: [[120, 0.6], [150, 0.5], [200, 0.3], [1000, 0.1]],
        2: [[100, 1], [120, 0.9], [140, 0.7], [180, 0.6], [225, 0.5], [250, 0.4], [275, 0.3], [450, 0.1]],
        3: [[100, 1.1], [140, 1], [160, 0.9], [180, 0.8], [200, 0.7], [225, 0.5], [275, 0.4], [300, 0.3], [325, 0.2], [450, 0.1]],
        4: [[100, 1.2], [140, 1.1], [160, 1], [180, 0.9], [200, 0.7], [225, 0.6], [275, 0.5], [300, 0.4], [325, 0.2], [450, 0.1]],
        5: [[100, 1.4], [140, 1.2], [175, 1.1], [200, 1.0], [225, 0.9], [250, 0.7], [275, 0.5], [300, 0.4], [350, 0.2], [450, 0.1]],
        6: [[100, 1.5], [200, 1.2], [250, 1.0], [275, 0.7], [300, 0.5], [325, 0.4], [350, 0.3], [450, 0.2]],
        7: [[100, 1.5], [150, 1.4], [200, 1.3], [250, 1.2], [275, 1], [300, 0.8], [325, 0.5], [350, 0.3], [450, 0.2]],
        8: [[100, 1.8], [150, 1.6], [225, 1.4], [275, 1.2], [300, 1], [325, 0.8], [350, 0.5], [400, 0.4], [450, 0.2]],
        9: [[100, 2], [150, 1.8], [200, 1.6], [275, 1.4], [300, 1.2], [325, 1], [350, 0.8], [400, 0.5], [450, 0.4]],
        10: [[100, 2.2], [200, 1.8], [250, 1.6], [300, 1.4], [325, 1.2], [375, 1], [400, 0.5], [450, 0.4]],
        11: [[100, 2.4], [175, 2.0], [250, 1.8], [300, 1.6], [325, 1.4], [350, 1.2], [400, 1.0], [450, 0.5]],
        12: [[100, 2.5], [250, 2.0], [275, 1.8], [325, 1.6], [350, 1.4], [375, 1.2], [450, 1.0]],
        13: [[100, 2.8], [200, 2.2], [275, 2.0], [325, 1.8], [350, 1.6], [375, 1.4], [450, 1.2]],
        14: [[100, 3.0], [250, 2.2], [325, 2.0], [350, 1.8], [375, 1.6], [450, 1.4]],
        15: [[100, 3.2], [200, 2.4], [275, 2.2], [350, 2], [375, 1.8], [450, 1.6]]
    }
    return switcher.get(currentRange, lambda: "Invalid BG")

currentRange = getRanges(currentBG, currentRanges)

if (currentRange == 0) or (currentRange == 16):
    print("Get the doctor!")
else:
    priorRange = getPriorRanges(currentRange)
    rateInterval = getRanges(priorBG, priorRange)
    rate = priorRange[rateInterval][1]
    newRate = rate*currentRate
    writeRecord.record(newRate, currentBG)
    print("New insulin titration rate is: ", rate*currentRate)
