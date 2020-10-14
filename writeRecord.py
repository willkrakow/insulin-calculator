from datetime import datetime

def record(record, stat):
  dateTimeObj = datetime.now()
  
  
  f = open("records.txt", "a")
  f.write('=================\n')
  f.writelines([str(dateTimeObj.hour), ':', str(dateTimeObj.minute), '\n\n', "Insulin rate: " + str(record), '\n', "Blood glucose: " + str(stat), '\n\n', '=================\n'])
  f.close()

def newPatient(ID):
  f = open('records.txt', 'a')
  patientInfo = 'Room ' + ID
  f.writelines(['=================\n', patientInfo, '\n'])
  f.close

