from datetime import datetime

patientID = input("Patient room #: ")
currentSBP = input("Current systolic BP: ")
currentDBP = input("Current diastolic BP: ")
hr = input("Current HR")

BP = currentSBP + currentDBP

dateTimeObj = datetime.now()
def bpRecord(ID, pressure, heartrate):
    patientInfo = 'Room ' + ID
    f = open("records.txt", "a")
    f.writelines(['=================\n', patientInfo, '\n'])
    f.write('=================\n')
    f.writelines([str(dateTimeObj.hour), ':', str(dateTimeObj.minute), '\n\n', "Blood pressure: " + str(pressure), '\n', "HR: " + str(heartrate), '\n\n', '=================\n'])
    f.close()

bpRecord(patientID, BP, hr)