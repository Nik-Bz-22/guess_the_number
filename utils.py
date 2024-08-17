from art import tprint
import re
from colorama import Fore
def display_welcome_message():
    tprint("Guess   Number", font="medium")


def handle_keyboard_interrupt(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print("\nBye-Bye ):")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    return wrapper



def error_handle(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception:
                print(Fore.RED+"Invalid input format"+Fore.RESET)
    return wrapper

def is_int(s):
    return re.fullmatch(r'-?\d+', s) is not None

def is_binary(s):
    return set(s).issubset({'0', '1'})