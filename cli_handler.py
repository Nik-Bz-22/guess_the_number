import argparse


def get_cli_args() -> dict:
    parser = argparse.ArgumentParser(description="""
    Using tips:
        :[tip_name]=[argument]
        List of tips:
        oe (Odd or Even) - will show whether the guessed number is even or odd. It has no arguments.
        ml (More or Less) - will show if your provided number is greater or less than the guessed number. It has one required argument.
        ri (Random Interval) - will show which interval the number belongs to. It has no arguments.

    Example usage:
        1) :oe 
        2) :ml=54
        3) :ri
    """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-l", "--left_bound", type=int, help="Left bound of range. Default=0 ", default=0)
    parser.add_argument("-r", "--right_bound", type=int, help="Right bound of range. Default=1", default=1)
    parser.add_argument("-a", "--attempts_count", type=int, help="Number of attempts. Default=3", default=3)
    parser.add_argument("-m", "--menu", type=int, help="Display game menu. Default=1", default=1)

    # Tips list
    parser.add_argument("--oe", type=int, help="Count of :oe tips. Default=1", default=1)
    parser.add_argument("--ml", type=int, help="Count of :ml tips. Default=1", default=1)
    parser.add_argument("--ri", type=int, help="Count of :ri tips. Default=1", default=1)
    # parser.add_help(False)
    args = parser.parse_args().__dict__
    return args


