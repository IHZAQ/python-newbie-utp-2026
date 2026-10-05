"""
PYTHON 2050: CODE THE FUTURE
Sprint 2 Python Console App Skeleton

This starter template demonstrates:
1. Variables and data types
2. Input and output
3. Arithmetic operators
4. Selection using if/elif/else
5. while and for loops
6. Lists and tuples
7. Functions

Suggested team size: 5–6 members
"""

from typing import Optional


def show_header() -> None:
    """Display the futuristic application header."""
    print("=" * 58)
    print(r"""
    ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
    ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
    ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
    ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
    ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
    ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

             2050: CODE THE FUTURE
    """)
    print("=" * 58)


def show_menu() -> str:
    """
    Member A — Menu & I/O Coder

    TODO: Member A should design the menu and collect user input here.

    This function demonstrates:
    - Output using print()
    - Input using input()
    - Returning a value to another function
    """
    print("\nMAIN MENU")
    print("1. Calculate energy score")
    print("2. Predict 2050 cost")
    print("Q. Quit")

    choice = input("Enter your choice: ").strip().lower()
    return choice


def calculate_energy(usage: float) -> float:
    """
    Member B — Core Logic Coder 1

    TODO: Member B should write the main calculation logic here.

    This function demonstrates:
    - Variables and data types
    - Arithmetic operators
    - if/elif/else selection
    - Returning a calculated result
    """
    # Variables and arithmetic operators
    base_score: float = 100.0
    energy_factor: float = 1.5
    score: float = base_score - (usage * energy_factor)

    # Selection using if/elif/else
    if score >= 80:
        rating = "Excellent"
    elif score >= 50:
        rating = "Good"
    else:
        rating = "Needs Improvement"

    print(f"\nEnergy usage: {usage:.2f} units")
    print(f"Energy score: {score:.2f}")
    print(f"Rating: {rating}")

    return score


def predict_2050_cost(score: float) -> float:
    """
    Member C — Core Logic Coder 2

    TODO: Member C should write the prediction logic here.

    This function demonstrates:
    - Lists
    - Tuples
    - A for loop iterating over 2050 records
    - Arithmetic using a score
    """
    # A list containing tuples representing future-year records.
    future_records = [
        (2050, 1.10),
        (2051, 1.15),
        (2052, 1.20),
    ]

    total_cost: float = 0.0

    print("\nFUTURE COST PREDICTION")

    # Iterate through the list of tuples using a for loop.
    for year, price_factor in future_records:
        estimated_cost = score * price_factor
        total_cost += estimated_cost
        print(f"{year}: estimated cost = {estimated_cost:.2f} credits")

    average_cost = total_cost / len(future_records)
    print(f"Average predicted cost: {average_cost:.2f} credits")

    return average_cost


def get_usage_value() -> Optional[float]:
    """
    Ask the user for an energy usage value.

    This helper keeps input validation separate from the main program flow.
    """
    try:
        usage_text = input("Enter today's energy usage in units: ").strip()
        usage = float(usage_text)

        if usage < 0:
            print("Usage cannot be negative.")
            return None

        return usage

    except ValueError:
        print("Please enter a valid number.")
        return None


def main() -> None:
    """
    Team Leader & Integrator

    TODO: The Team Leader should connect all functions here.

    This function demonstrates:
    - A while loop
    - Calling functions created by different team members
    - Clean integration of the whole application
    """
    show_header()

    running = True

    # The while loop keeps the application running until the user quits.
    while running:
        choice = show_menu()

        if choice == "1":
            usage = get_usage_value()

            if usage is not None:
                calculate_energy(usage)

        elif choice == "2":
            usage = get_usage_value()

            if usage is not None:
                score = calculate_energy(usage)
                predict_2050_cost(score)

        elif choice == "q":
            print("\nThank you for helping build the future. Goodbye! 🚀")
            running = False

        else:
            print("\nInvalid choice. Please select 1, 2, or Q.")


# This line starts the program when the file is run directly.
if __name__ == "__main__":
    main()
