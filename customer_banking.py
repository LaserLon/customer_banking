# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance, savings_interest, savings_maturity = account_details()
    
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned =  create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print_details("Savings account interest", updated_savings_balance, interest_earned)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance, cd_interest, cd_maturity = account_details()

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print_details("CD account interest", updated_cd_balance, interest_earned)

# Print out the interest earned and account balance with interest earned.
def print_details(header, updated_balance, interest_earned):
    """Prints the details of the account.

    Args:
        header (str): The header for the output.
        updated_balance (float): The updated balance of the account.
        interest_earned (float): The interest earned on the account.
    """
    print (header)
    print (f"Interest earned: {interest_earned}")
    print (f"Current balance: {updated_balance}\n")
        
def account_details():
    """Prompts the user to enter account details.

    Returns:
        the balance (float), interest rate (float), and maturity (int).
    """
    balance = input_num("Enter current balance: ")
    interest = input_num("Enter current interest rate: ")
    maturity = input_num("Enter total number of months: ")
    return float(balance), float(interest), int(maturity)

# prompt for a numeric input and verify the input is a number
def input_num(prompt):
    """Prompts the user for a numeric input and validates it.

    Args:
        prompt (str): The prompt message for the user.

    Returns:
        The validated numeric input (float)
    """
    while True:
        value = input(prompt)
        try:
            return float(value)  # Try converting to float to validate the input
        except ValueError:
            print("Invalid entry. Please enter a number.\n")

if __name__ == "__main__":
    # Call the main function.
    main()
