class Card:
    #Number as Integer
    #Colour as String
    def __init__(self, Number, Colour):
        self.Number = Number  #Integer
        self.Colour = Colour  #String

    def GetNumber(self):
        return self.Number

    def GetColour(self):
        return self.Colour

def ChooseCard(Cards):
    selected = []
    properSelection = False
    while not properSelection:
        userChoice = int(input("Enter a card number: "))
        while userChoice < 1 or userChoice > 30:
            userChoice = int(input("Enter a card number: "))

        if userChoice in selected:
            print("Card already chosen")
            properSelection = False
        else:
            properSelection = True

    selected.append(userChoice)
    for i in range(0, len(Cards)):
        if Cards[i].GetNumber() == userChoice:
            return i



if __name__ == '__main__':
    Cards = []
    Player1 = []
    for i in range(30):
        file = open("CardValues.txt", "r")
        number = file.readline()
        colour = file.readline()
        card = Card(number, colour)
        Cards.append(card)

    file.close()

    for i in range(4):
        index = ChooseCard(Cards)
        Player1.append(Cards[index])

    for i in range(4):
        print(Player1[i].GetNumber())
        print(Player1[i].GetColour())
        print(" ")