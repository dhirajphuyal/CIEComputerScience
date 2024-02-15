class Employee:
    def __init__(self, hourlyPay, employeeNumber, jobTitle):
        self.HourlyPay = hourlyPay
        self.EmployeeNumber = employeeNumber
        self.JobTitle = jobTitle
        self.PayYear2022 = []

        for i in range(0, 52):
            self.PayYear2022.append(0.0)

    def GetEmployeeNumber(self):
        return self.EmployeeNumber

    def SetPay(self, weekNumber, hoursWorked):
        weeklyPay = hoursWorked * self.HourlyPay
        self.PayYear2022[weekNumber] = weeklyPay

    def GetTotalPay(self):
        totalPay = 0.0
        for i in range(0, 52):
            totalPay += self.PayYear2022[i]


class Manager(Employee):
    def __init__(self, bonusValue, hourlyPay, employeeNumber, jobTitle):
        self.BonusValue = bonusValue
        Employee.__init__(self, hourlyPay, employeeNumber, jobTitle)

    def SetPay(self, weekNumber, hoursWorked):
        hoursWorked = hoursWorked + ((self.BonusValue / 100) * hoursWorked)
        Employee.SetPay(self, weekNumber, hoursWorked)


EmployeeArray = []


def EnterHours():
    hoursFile = open("HoursWeek1.txt", "r")

    employeeNumber = hoursFile.readline()
    hoursWorked = hoursFile.readline()

    for i in range(0, len(EmployeeArray)):
        if EmployeeArray[i].GetEmployeeNumber() == employeeNumber:
            EmployeeArray[i].SetPay(0, hoursWorked)

    hoursFile.close()


if __name__ == '__main__':
    file = open("Employees.txt", "r")

    while file.readline() != "":
        hourlyPay = file.readline()
        employeeNumber = file.readline()
        bonusValue = file.readline()
        jobTitle = file.readline()

        if (bonusValue == ""):
            employee = Employee(hourlyPay, employeeNumber, jobTitle)
            EmployeeArray.append(employee)
        else:
            manager = Manager(bonusValue, hourlyPay, employeeNumber, jobTitle)
            EmployeeArray.append(manager)

    EnterHours()

    for i in range(0, len(EmployeeArray)):
        print(EmployeeArray[i].GetEmployeeNumber())
        print(EmployeeArray[i].GetTotalPay())

    file.close()


