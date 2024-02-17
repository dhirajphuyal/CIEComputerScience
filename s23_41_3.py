Animal = []
Colour = []

global AnimalTopPointer
global ColourTopPointer

AnimalTopPointer = 0
ColourTopPointer = 0


def PushAnimal(DataToPush):
    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer += 1
        return True


def PopAnimal():
    ReturnData = ""
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData


def PushColour(DataToPush):
    if ColourTopPointer == 10:
        return False
    else:
        Colour.append(DataToPush)
        ColourTopPointer += 1
        return True


def PopColour():
    ReturnData = ""
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData

def OutputItem():
    Animal = PopAnimal()
    Colour = PopColour()

    if Colour == "":
        PushAnimal(Animal)
        print("No colour")
    elif Animal == "":
        PushColour(Colour)
        print("No animal")
    else:
        print(Animal + " " + Colour)

def ReadData():
    try:
        file = open("AnimalData.txt", "r")
        AnimalName = file.readline()
        while AnimalName != "":
            AnimalName = file.readline()
            PushAnimal(AnimalName)
        file.close()
    except:
        print("Error reading animal file")

    try:
        file = open("ColourData.txt", "r")
        ColourName = file.readline()
        while ColourName != "":
            ColourName = file.readline()
            PushColour(ColourName)
        file.close()
    except:
        print("Error reading colour file")


if __name__ == '__main__':
    ReadData()
    for i in range(4):
        OutputItem()