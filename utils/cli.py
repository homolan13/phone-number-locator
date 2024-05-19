import sys
import argparse
from colorama import init, Fore

# Function to handle command-line arguments.
def cli_argument():
    init()
    # Create an ArgumentParser object and specify a description.
    parser = argparse.ArgumentParser(description="Get approximate location of a Phone number.")
    # Define a command-line argument: -p or --phone. This is to receive the user's number from terminal.
    parser.add_argument("-p", "--phone", dest="phone_number", type=str,
                        help="Phone number to track. Please include the country code when specifying the number.",
                        required=True, nargs="+")
    # Parse the command-line arguments.
    argument = parser.parse_args()
    # Check if the 'phone_number' argument is not provided.
    if not argument.phone_number:
        # Print an error message indicating that the phone number is required.
        print(f"{Fore.RED}[-] Please specify the phone number to track (including country code)."
              " Use --help to see usage.")
        # Exit the script.
        sys.exit()
    # Return the parsed command-line arguments.
    return argument