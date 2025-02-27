from datetime import datetime
from string import capwords

spacecraft_model_price = {
    "Rocket Lab Photon": 10_000,
    "SpaceX Falcon 9": 5_000,
    "Blue Origin New Shepard": 8_000
}

def welcome():
    print(r'''
 ____                        ____            __ _   
/ ___| _ __   __ _  ___ ___ / ___|_ __ __ _ / _| |_ 
\___ \| '_ \ / _` |/ __/ _ \ |   | '__/ _` | |_| __|
 ___) | |_) | (_| | (_|  __/ |___| | | (_| |  _| |_ 
|____/| .__/ \__,_|\___\___|\____|_|  \__,_|_|  \__|
      |_|                                           
    ''')
    while True:
        user_name = input("ヾ(＾ ∇ ＾). What is your name?\n ")
        user_name_plain = user_name.replace(" ", "")
        if user_name_plain.isalpha():
            if (user_name_plain.lower().strip() == "wright" or user_name_plain.lower().strip() == "nickwright"
                or user_name_plain.lower().strip() == "nick"): user_name = "Mr Wright"
            user_name = capwords(user_name)
            print(f"Hello {user_name}! Hope you are well, thank you for choosing this program! ⸜(｡˃ ᵕ ˂ )⸝♡\n")
            return user_name
        else:
            print('🚨 user_name must be consisted by alpha. "( – ⌓ – ) ')


# Ask the user to confirm their input.
def confirm_input(prompt, value):
    while True:
        confirmation = input(f"\n  You entered '{value}'. Confirm? (Y/N): ").strip().lower()
        if confirmation in ["y", "yes"]:
            return value
        elif confirmation in ["n", "no"]:
            return None
        print("  🚨 Error: Please enter Y/N or Yes/No.")


# Get user-selected spacecraft model.
def get_spacecraft_model_price():
    while True:
        while True:
            print("\n  Please choose your spacecraft model: 👀")
            # Display modules available
            for index, model in enumerate(spacecraft_model_price.keys(), 1):
                print(f"{index}. {model:·<35}${spacecraft_model_price[model]:>6,}/day")

            model = input("  Please enter the index or full name: 👉").strip()

            if model.isdigit():
                index = int(model) - 1
                if 0 <= index < len(spacecraft_model_price):
                    selected_model = list(spacecraft_model_price.keys())[index]
                    if confirm_input("Spacecraft Model", selected_model):
                        return selected_model
                    else:
                        break  # Restart input immediately

            format_input = model.lower().replace(" ", "")
            for model in spacecraft_model_price:
                if format_input == model.lower().replace(" ", ""):
                    if confirm_input("Spacecraft Model", model):
                        return model
                    else:
                        break  # Restart input immediately

            print("  🚨 Error: Invalid spacecraft model, please try again!")


# Get hire duration (1-30 days).
def get_hire_period():
    while True:
        while True:
            try:
                period = int(input("\n  Please enter the hiring duration (1-30 days): 👉"))
                if 1 <= period <= 30:
                    if confirm_input("Hire Period", f"{period} days"):
                        return period
                    else:
                        break  # Restart input immediately
                else:
                    print("  🚨 Error: Hiring duration must be between 1 and 30 days.")
            except ValueError:
                print("  🚨 Error: Please enter a valid number!")


# Get number of passengers (0-10).
def get_passenger_count():
    while True:
        while True:
            try:
                count = int(input("\n  Please enter the number of passengers (0-10): 👉 "))
                if 0 <= count <= 10:
                    if confirm_input("Passenger Count", f"{count} passengers"):
                        return count
                    else:
                        break  # Restart section immediately
                else:
                    print("  🚨 Error: Number of passengers must be between 0 and 10!")
            except ValueError:
                print("  🚨 Error: Please enter a valid number!")


# Ask if the user needs a pilot.
def get_pilot_choice():
    while True:
        while True:
            pilot = input("\n  Do you need a pilot? (Y/N)🤔: ").strip().lower()
            if pilot in ["y", "yes"]:
                if confirm_input("Pilot Requirement", "Yes"):
                    return True
                else:
                    break  # Restart input immediately
            elif pilot in ["n", "no"]:
                if confirm_input("Pilot Requirement", "No"):
                    return False
                else:
                    break  # Restart input immediately
            print("  🚨 Error: Please enter Y/N or Yes/No.")


# Calculate total cost based on selections.
def calculate_cost(model, period, has_pilot, passengers):
    daily_rate = spacecraft_model_price[model]
    pilot_cost = 500 * period if has_pilot else 0
    passenger_cost = 500 * passengers * period
    return (daily_rate * period) + pilot_cost + passenger_cost

# Print the final hire receipt.
def print_receipt(spacecraft, period, passengers, has_pilot, total):
    print("\n" + "=" * 50)
    print("Inquiry Result".center(50))
    print("-" * 50)

    date = datetime.now().strftime("%d-%b-%Y--%H:%M:%S")
    print(f"Inquiry date: {date}")

    print("-" * 50)
    print(f"\tSpacecraft Model: {spacecraft}")
    print(f"\tHire Period: {period} days")
    print(f"\tPassengers: {passengers}")
    print(f"\tPilot Required: {'Yes' if has_pilot else 'No'}")
    print("*" * 50)
    print(f"\tTotal Cost: ${total:,.2f}")
    print("*" * 50)
    print("=" * 50)


def main():
    while True:
        user_name = welcome()
        #
        # print("=" * 50)
        # print("🚀Spacecraft Hire Calculator🚀".center(50))
        # print("-" * 50)
        #
        # spacecraft = get_spacecraft_model_price()
        # period = get_hire_period()
        # has_pilot = get_pilot_choice()
        # passengers = get_passenger_count()
        # total = calculate_cost(spacecraft, period, has_pilot, passengers)
        # print_receipt(spacecraft, period, passengers, has_pilot, total)

        while True:
            restart = input("\nWould you like to restart? (Y/N)🤔: ").strip().lower()
            if restart in ["n", "no"]:
                print(f"\nThank you for using our service {user_name}! Goodbye! („• ֊ •„)੭")
                print(r'''
 ____             __   __            _ 
/ ___|  ___  ___  \ \ / /__  _   _  | |
\___ \ / _ \/ _ \  \ V / _ \| | | | | |
 ___) |  __/  __/   | | (_) | |_| | |_|
|____/ \___|\___|   |_|\___/ \__,_| (_)
                ''')
                return
            elif restart  in ["y", "yes"]: break
            print("  🚨 Error: Please enter Y/N or Yes/No.")



if __name__ == "__main__":
    main()
