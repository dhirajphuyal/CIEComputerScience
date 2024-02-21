CircularQueue = []
global Head
global Tail
global NumberOfItems


class SaleData:
    def __init__(self, id, quantity):
        self.ID = id
        self.Quantity = quantity


def Enqueue(saleData):
    global NumberOfItems
    global Tail
    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = saleData
        Tail += 1
        NumberOfItems += 1
        return 1


def Dequeue():
    global NumberOfItems
    global Head
    if NumberOfItems == 0:
        return SaleData("", -1)
    else:
        Head += 1
        NumberOfItems -= 1
        return CircularQueue[Head]


def EnterRecord():
    id = int(input("Enter ID: "))
    quantity = int(input("Enter Quantity: "))
    saleData = SaleData(id, quantity)
    queueOperation = Enqueue(saleData)
    if queueOperation == -1:
        print("Full")
    else:
        print("Stored")


if __name__ == '__main__':
    global Head
    global Tail
    global NumberOfItems

    Head = 0
    Tail = 0
    NumberOfItems = 0
    for i in range(5):
        CircularQueue.append(SaleData("", -1))

    for i in range(6):
        EnterRecord()

    saleData = Dequeue()

    if saleData.Quantity == -1:
        print("Error: The queue is empty")
    else:
        print("ID: ", saleData.ID, " Quantity: ", saleData.Quantity)

    EnterRecord()

    for i in range(len(CircularQueue)):
        print(CircularQueue[i].ID, CircularQueue[i].Quantity)