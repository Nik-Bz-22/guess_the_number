
import argparse
from art import tprint


def get_cli_args() -> dict:
    parser = argparse.ArgumentParser(description="""
    Using tips:
        :[tip_name]=[argument]
        List of tips:
        oe (Odd or Even) - will show whether the guessed number is even or odd. It has no arguments.
        ml (More or Less) - will show if your provided number is greater or less than the guessed number. It has one required argument.

    Example usage:
        1) :oe 
        2) :ml=54
    """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-l", "--left_bound", type=int, help="Left bound of range. Default=0 ", default=0)
    parser.add_argument("-r", "--right_bound", type=int, help="Right bound of range. Default=1", default=1)
    parser.add_argument("-a", "--attempts_count", type=int, help="Number of attempts. Default=3", default=3)
    # parser.add_help(False)
    args = parser.parse_args().__dict__
    return args


def display_welcome_message():
    tprint("Guess   Number", font="medium")