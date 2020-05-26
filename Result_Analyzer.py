#Code written by Shimon Johnson

import os, csv
from visualization import make_pie

rootDir = 'Required_results'
resultItems = []
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    for fileName in fileList:
        with open(os.path.join(dirName, fileName), 'r') as f:
            reader = csv.reader(f, dialect='excel', delimiter=',')
            for row in reader:
                resultItems.append(row[4].lower())
resultItems = set(resultItems)

targetItems = []
targetDir = ''
with open(os.path.join('', 'target.csv'), 'r') as f:
    reader = csv.reader(f, dialect='excel', delimiter=',')
    for row in reader:
        targetItems.append(row[1].lower())

detectedCounter = 0
noMatchCounter = 0
for resultItem in resultItems:
    if resultItem in targetItems:
        detectedCounter += 1
        #print ("Detected words",resultItem)
    elif resultItem not in targetItems:
        noMatchCounter += 1
        #print ("Detected_Uncommon",resultItem)

absentCount = len(targetItems) - (detectedCounter + noMatchCounter)

calculatedResult = {
    "Detected_count": detectedCounter,
    "Detected_Uncommon": noMatchCounter,
    "Absent/Undetected": absentCount
}

make_pie(calculatedResult)

print("Calculated Result - ", calculatedResult)
