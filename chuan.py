import sys

def welcome():
    print(welcome_msg)

def illegal_input(user_input):
    print("\n\n*********************************************************")
    print(f"-------------------Illegal input [ {user_input} ]--------------------")
    print("*********************************************************\n")

def compute_id(id):
    global chosenID
    if id == 1 and store1 >= 1:
        chosenID = 1
    elif id == 2 and store2 >= 1:
        chosenID = 2
    elif id == 3 and store3 >= 1:
        chosenID = 3
    else:
        return False
    return True

def compute_days(days):
    global chosenDays
    if 1 <= days <= 30:
        chosenDays = days
        return True
    return False

def compute_pilot(pilot):
    global needPilot
    if pilot == 1:
        needPilot = True
        return True
    elif pilot == 2:
        needPilot = False
        return True
    return False

def compute_passenger(num):
    global passengerNumber
    if 1 <= num <= 10:
        passengerNumber = num
        return True
    return False

def calculate():
    global spacecraftPrice, pilotPrice, passengerPrice, totalPrice
    spacecraftPrice = prices[chosenID - 1] * chosenDays
    pilotPrice = chosenDays * (500 if needPilot else 0)
    passengerPrice = 500 * chosenDays * passengerNumber
    totalPrice = spacecraftPrice + passengerPrice + pilotPrice
    print("\n\n{*****************************************************}")
    print(f"{{ Spacecraft Model --> {names[chosenID - 1]} ${prices[chosenID - 1]} }}")
    print(f"{{ Hire Period --> {chosenDays} {'day' if chosenDays == 1 else 'days'} }}")
    print(f"{{ Total Hire Charge for spacecraft --> ${spacecraftPrice} }}")
    print(f"{{ Pilot Required --> {'Yes ($' + str(pilotPrice) + ' total)' if needPilot else 'No'} }}")
    print(f"{{ Passengers --> ${passengerPrice} ({passengerNumber} {'passenger' if passengerNumber == 1 else 'passengers'}) }}")
    print(f"{{ Total Hired Charged --> ${totalPrice} }}")
    print("{*****************************************************}")
    return totalPrice

store1, store2, store3 = 1, 1, 1
chosenID, chosenDays, passengerNumber = 0, 0, 0
needPilot = False
names = ["Rocket Lab Photon", "SpaceX Falcon 9", "Blue Origin New Shepard"]
prices = [10000, 5000, 8000]
price_table = """|*****************************************************|
|* ID *|  * Spacecraft Name *  |* Daily Hired Charge *|
|  1   |   Rocket Lab Photon   |      $10000.00       |
|  2   |    SpaceX Falcon 9    |       $5000.00       |
|  3   |Blue Origin New Shepard|       $8000.00       |
|*****************************************************|
\nPlease enter the ID of your preferred spacecraft model:> """
welcome_msg = """
Welcome to the Spacecraft Hire Program!

Here is the list of our product prices:
                    |
                    |
                    V"""

def main():
    welcome()
    while True:
        user_input = input(price_table)
        try:
            id = int(user_input)
        except ValueError:
            illegal_input(user_input)
            continue
        if compute_id(id):
            break
        illegal_input(user_input)
    print("*****************************************************")
    print(f"-----Spacecraft {names[chosenID - 1]} available-----")
    print("*****************************************************\n\n")
    while True:
        print("*****************************************************")
        print(f"---The {names[chosenID - 1]} costs ${prices[chosenID - 1]} per day---")
        print("*****************************************************")
        user_input = input("Please enter the hire period(in days) :>")
        try:
            days = int(user_input)
        except ValueError:
            illegal_input(user_input)
            continue
        if compute_days(days):
            break
        print("\n\n*****************************************************")
        print("----------------Input days is too small--------------" if days <= 0 else "----------------Input days is too large--------------")
    while True:
        print("\n\n*****************************************************")
        print("Price for hiring a pilot is: [$500] per day")
        print(f"Do you need a pilot?(cost ${chosenDays * 500} for the whole expedition)")
        print("*****************************************************")
        user_input = input("Enter 1 as Yes, 2 as No :>")
        try:
            pilot = int(user_input)
        except ValueError:
            illegal_input(user_input)
            continue
        if compute_pilot(pilot):
            break
        illegal_input(user_input)
    while True:
        print("\n\n*****************************************************")
        print("How many passenger will you bring? (Maximum 10 person)($500 per day for each passenger)")
        user_input = input("Please enter your answer(integer) :>")
        try:
            num = int(user_input)
        except ValueError:
            illegal_input(user_input)
            continue
        if compute_passenger(num):
            break
        illegal_input(user_input)
    calculate()

if __name__ == "__main__":
    main()