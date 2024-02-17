def PrintArray(DataArray):
    output = ""
    for X in range(0, len(DataArray)):
        output = output + str(DataArray[X]) + " "
    print(output)



def LinearSearch(DataArray, SearchValue):
    counter = 0
    for i in range(0, len(DataArray)):
        if SearchValue == DataArray[i]:
            counter += 1

    return counter

if __name__ == '__main__':
    DataArray = []

    file = open("Data.txt", "r")
    for i in range(0, 25):
        data = file.readline()
        DataArray.append(data)

    # PrintArray(DataArray)

    SearchValue = int(input("1. Enter whole number between 0 and 100 inclusive: "))
    while SearchValue > 100 or SearchValue < 0:
        SearchValue = int(input("2. Enter whole number between 0 and 100 inclusive: "))
    print("The number " + str(SearchValue) + " is found " + str(LinearSearch(DataArray, SearchValue)) + " times")


    file.close()