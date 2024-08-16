
import argparse
from art import tprint


def get_cli_args() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--left_bound", type=int, help="Left bound of range. Default=0 ", default=0)
    parser.add_argument("-r", "--right_bound", type=int, help="Right bound of range. Default=1", default=1)
    parser.add_argument("-a", "--attempts_count", type=int, help="Number of attempts. Default=3", default=3)

    args = parser.parse_args().__dict__
    return args


def display_welcome_message():
    tprint("Guess   Number", font="medium")