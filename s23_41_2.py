import random


def PrintArray(DataArray):
    for X in range(0, 10):
        output = ""
        for Y in range(0, 10):
            output = output + str(DataArray[X][Y]) + " "
        print(output)


if __name__ == '__main__':
    DataArray = []
    for i in range(0, 10):
        DataArray.append([])
        for j in range(0, 10):
            DataArray[i].append(random.randint(1, 100))

    PrintArray(DataArray)
    print("")
    print("Sorted array")

    ArrayLength = 10

    for X in range(0, ArrayLength):
        for Y in range(0, ArrayLength - 1):
            for Z in range(0, ArrayLength - Y - 1):
                if DataArray[X][Z] > DataArray[X][Z + 1]:
                    TempValue = DataArray[X][Z]
                    DataArray[X][Z] = DataArray[X][Z + 1]
                    DataArray[X][Z + 1] = TempValue

    PrintArray(DataArray)