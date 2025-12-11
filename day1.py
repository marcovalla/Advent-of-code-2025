from utils import FileReader

def getNumberOfTimesDialStopAt0():
    fileReader = FileReader()
    elements = fileReader.getElements("day1-input.txt")
    numberOfTimes = 0
    dial = 50
    for element in elements:
        rotation = element[0]
        if (len(element) > 3):
            times = int(element[1] + element[2] + element[3])
        else:
            if (len(element) > 2):
                times = int(element[1] + element[2])
            else:
                times = int(element[1])
        
        if (rotation == "L"):
            dial -= times
        else:
            dial += times
        
        while (dial < 0):
            dial += 100
        while (dial >= 100):
            dial -= 100
        
        if (dial == 0):
            numberOfTimes += 1

        print(element, times, dial, numberOfTimes)

    return numberOfTimes

def getNumberOfTimesDialPointAt0():
    fileReader = FileReader()
    elements = fileReader.getElements("day1-input.txt")
    numberOfTimes = 0
    dial = 50
    dialAt0 = False
    for element in elements:
        rotation = element[0]
        if (len(element) > 3):
            times = int(element[1] + element[2] + element[3])
        else:
            if (len(element) > 2):
                times = int(element[1] + element[2])
            else:
                times = int(element[1])
        
        while (times >= 100):
                times -= 100
                numberOfTimes += 1

        while (times < 0):
                times += 100
                numberOfTimes += 1

        if (rotation == "L"):
            dial -= times
        else:
            dial += times

        if (dial == 0):
            numberOfTimes += 1
            
        if (dial < 0):
            dial += 100
            if (not dialAt0):
                numberOfTimes += 1
        if (dial >= 100):
            dial -= 100
            if (not dialAt0):
                numberOfTimes += 1

        if (dial == 0):
            dialAt0 = True
        else:
            dialAt0 = False

    return numberOfTimes

print(getNumberOfTimesDialPointAt0())
