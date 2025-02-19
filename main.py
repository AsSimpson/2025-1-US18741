def confirm_input(prompt, value):
    """Ask the user to confirm their input."""
    while True:
        confirmation = input(f"\n  You entered '{value}'. Confirm? (Y/N): ").strip().lower()
        if confirmation in ["y", "yes"]:
            return value
        elif confirmation in ["n", "no"]:
            return None
        print("  ⚠ Error: Please enter Y/N or Yes/No.")


# Get the model user choose
def get_spacecraft_model():
    while True:
        print("\n  Please choose your spacecraft model：")
        # Display modules available
        for index, model in enumerate(spacecraft_model.keys(), 1):
            print(f"\t{index}. {model} (${spacecraft_model[model]:,}/day)")

        model = input("  Please enter the index or full name: ").strip()

        if model.isdigit():
            index = int(model) - 1
            if 0 <= index < len(spacecraft_model):
                return list(spacecraft_model.keys())[index]


        # Regularise input
        regularise_input = model.lower().replace(" ", "")
        for model in spacecraft_model:
            if regularise_input == model.lower().replace(" ", ""):
                return model

        print("  ⚠ Error: Invalid spacecraft model, try agine please! ")


def get_hire_period():
    """获取租赁day数（1-30day）"""
    while True:
        try:
            period = int(input("\n  Please enter the hire period: (1-30 days): "))
            if 1 <= period <= 30:
                return period
            print("  ⚠ Error: Hiring duration must be between 1 and 30 days. ")
        except ValueError:
            print("  ⚠ Error: Please enter a valid number!")


def get_passenger_count():
    """Get number of passengers (0-10)."""
    while True:
        try:
            count = int(input("\n  Enter the number of passengers: "))
            if 0 <= count <= 10:
                return count
            print("  ⚠ Error: the number of passengers must between 0 and 10! ")
        except ValueError:
            print("  ⚠ Error: Please enter a valid number！")



def get_pilot_choice():
    """Ask if the user needs a pilot."""
    while True:
        pilot = input("\n  Do you need a pilot? (Y/N): ").strip().lower()
        if pilot in ["y", "yes"]:
            return True
        elif pilot in ["n", "no"]:
            return False
        print("  ⚠ Error: Please enter Y/N or Yes/No.")


def calculate_cost(model, period, has_pilot, passengers):
    """Calculate total cost based on selections."""
    daily_rate = spacecraft_model[model]
    pilot_cost = 500 * period if has_pilot else 0
    passenger_cost = 500 * passengers * period
    return (daily_rate * period) + pilot_cost + passenger_cost

spacecraft_model = {
    "Rocket Lab Photon": 10_000,
    "SpaceX Falcon 9": 5_000,
    "Blue Origin New Shepard": 8_000
}

def main():
    print("=" * 50)
    print("Space Exploration Company".center(50))
    print("-" * 50)

    spacecraft = get_spacecraft_model()
    period = get_hire_period()
    has_pilot = get_pilot_choice()
    passengers = get_passenger_count()

    # Calculate expense in total
    total = calculate_cost(spacecraft, period, has_pilot, passengers)

    #
    print("\n" + "=" * 50)
    print("Hire Receipt".center(50))
    print("-" * 50)
    print(f"\tSpacecraft Model: {spacecraft}")
    print(f"\tHire period: {period} days")
    print(f"\tPassengers: {passengers}")
    print(f"\tPilot Required: {'Yes' if has_pilot else 'No'}")
    print("*" * 50)
    print(f"\tTotal: ${total:,.2f}")
    print("*" * 50)

    print("=" * 50)


if __name__ == "__main__":
    main()