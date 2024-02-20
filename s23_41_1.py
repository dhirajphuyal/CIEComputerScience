stackData = []

global StackPointer
StackPointer = 0


def PrintValues():
    for i in range(0, len(stackData)):
        print(stackData[i])
    print("Stack Pointer: ", str(StackPointer))


def Push(value):
    global StackPointer
    if StackPointer == 10:
        return False
    else:
        stackData.append(value)
        StackPointer += 1
        return True


def Pop():
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        StackPointer -= 1
        popValue = stackData[StackPointer]
        stackData[StackPointer] = 0
        return popValue


if __name__ == '__main__':

    for i in range(11):
        value = int(input("Enter a value: "))
        success = Push(value)
        if success:
            print("Value added")
        else:
            print("Stack full")

    PrintValues()

    Pop()
    Pop()
    PrintValues()
