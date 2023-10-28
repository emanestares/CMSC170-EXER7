import tkinter as tk
import math
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

nearestNeighbors = {}
trainingDataSet = []
inputDataSet = []
greatestNearestD = 0
distance = 0
index = 0
k = 0
zeroCount = 0
oneCount = 0

print("Select Training CSV file")
filePath = filedialog.askopenfilename()
trainingFile = open(filePath, "r")
for vector in trainingFile:
    trainingDataSet.append(vector[0:len(vector)-1].split(","))

trainingFile.close()

print("Select Input CSV file")
filePath = filedialog.askopenfilename()
inputFile = open(filePath, "r")
for vector in inputFile:
    inputDataSet.append(vector[0:len(vector)-1].split(","))

inputFile.close()

k = int(input("Enter k value:"))

for inputVector in inputDataSet:
    nearestNeighbors = {}
    print(inputVector)
    for trainingVector in trainingDataSet:
        greatestNearestD = 0
        zeroCount = 0
        oneCount = 0
        distance = 0
        index = 0
        for vectorElement in inputVector:
            distance += (float(vectorElement) - float(trainingVector[index]))**2
            index += 1
        distance = math.sqrt(distance)
        if len(nearestNeighbors) < k:
            nearestNeighbors[distance] = trainingVector
        else:
            for dist in nearestNeighbors:
                if dist > greatestNearestD:
                    greatestNearestD = dist

            if distance < greatestNearestD:
                del nearestNeighbors[greatestNearestD]
                nearestNeighbors[distance] = trainingVector
    for vector in nearestNeighbors:
        print(nearestNeighbors[vector], vector)
    for dist in nearestNeighbors:
        if int(nearestNeighbors[dist][len(inputVector)]) == 0:
            zeroCount += 1
        else:
            oneCount += 1
        
    if zeroCount > oneCount:
        inputVector.append(0)
        inputVector.append("Non-Diabetic")
    else:
        inputVector.append(1)
        inputVector.append("Diabetic")

filePath = open("output.txt", "w")

for inputVector in inputDataSet:
    index = 0
    for inputElement in inputVector:
        filePath.write(str(inputElement))
        if index < len(inputVector)-1:
            filePath.write(",")
        index+=1
    filePath.write("\n")

filePath.close()

print("Done! Check output.txt")