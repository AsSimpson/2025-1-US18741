spacecraft_model = {
    "Rocket Lab Photon": 10_000,
    "SpaceX Falcon 9": 5_000,
    "Blue Origin New Shepard": 8_000
}


def confirm_input(prompt, value):
    """Ask the user to confirm their input."""
    while True:
        confirmation = input(f"\n  You entered '{value}'. Confirm? (Y/N): ").strip().lower()
        if confirmation in ["y", "yes"]:
            return value
        elif confirmation in ["n", "no"]:
            return None
        print("  ⚠ Error: Please enter Y/N or Yes/No.")


def get_user_input(prompt, validation, error_msg, formatter=lambda x: x):
    """Generalized input function with validation and confirmation."""
    while True:
        try:
            value = input(f"\n  {prompt}: ").strip()
            value = formatter(value)
            if validation(value):
                if confirm_input(prompt, value):
                    return value
        except ValueError:
            pass
        print(f"  ⚠ Error: {error_msg}")


def get_spacecraft_model():
    """Get user-selected spacecraft model."""
    while True:
        print("\n  Please choose your spacecraft model:")
        models = list(spacecraft_model.keys())
        for index, model in enumerate(models, 1):
            print(f"\t{index}. {model} (${spacecraft_model[model]:,}/day)")

        def validate_model(value):
            if value.isdigit():
                index = int(value) - 1
                return 0 <= index < len(models)
            normalized_value = value.lower().replace(" ", "")
            return any(normalized_value == m.lower().replace(" ", "") for m in models)

        def format_model(value):
            if value.isdigit():
                return models[int(value) - 1]
            normalized_value = value.lower().replace(" ", "")
            for model in models:
                if normalized_value == model.lower().replace(" ", ""):
                    return model

        return get_user_input("Enter the index or full name", validate_model, "Invalid spacecraft model", format_model)


def get_hire_period():
    """Get hire duration (1-30 days)."""
    return get_user_input("Enter the hiring duration (1-30 days)", lambda x: x.isdigit() and 1 <= int(x) <= 30,
                          "Hiring duration must be between 1 and 30 days", int)


def get_passenger_count():
    """Get number of passengers (0-10)."""
    return get_user_input("Enter the number of passengers (0-10)", lambda x: x.isdigit() and 0 <= int(x) <= 10,
                          "Number of passengers must be between 0 and 10!", int)


def get_pilot_choice():
    """Ask if the user needs a pilot."""
    return get_user_input("Do you need a pilot? (Y/N)", lambda x: x.lower() in ["y", "yes", "n", "no"],
                          "Please enter Y/N or Yes/No", lambda x: x.lower() in ["y", "yes"])


def calculate_cost(model, period, has_pilot, passengers):
    """Calculate total cost based on selections."""
    daily_rate = spacecraft_model[model]
    pilot_cost = 500 * period if has_pilot else 0
    passenger_cost = 500 * passengers * period
    return (daily_rate * period) + pilot_cost + passenger_cost


def print_receipt(spacecraft, period, passengers, has_pilot, total):
    """Print the final hire receipt."""
    print("\n" + "=" * 50)
    print("Hire Receipt".center(50))
    print("-" * 50)
    print(f"\tSpacecraft Model: {spacecraft}")
    print(f"\tHire Period: {period} days")
    print(f"\tPassengers: {passengers}")
    print(f"\tPilot Required: {'Yes' if has_pilot else 'No'}")
    print("*" * 50)
    print(f"\tTotal Cost: ${total:,.2f}")
    print("*" * 50)


def main():
    while True:
        print("=" * 50)
        print("Space Exploration Company".center(50))
        print("-" * 50)

        spacecraft = get_spacecraft_model()
        period = get_hire_period()
        has_pilot = get_pilot_choice()
        passengers = get_passenger_count()
        total = calculate_cost(spacecraft, period, has_pilot, passengers)

        print_receipt(spacecraft, period, passengers, has_pilot, total)

        if input("\nWould you like to restart? (Y/N): ").strip().lower() not in ["y", "yes"]:
            print("\nThank you for using our service! Goodbye!")
            break


if __name__ == "__main__":
    main()
