# Guess The Number

## Usage

### usage: `main.py` [-h] [-l LEFT_BOUND] [-r RIGHT_BOUND] [-a ATTEMPTS_COUNT] [-m MENU] [--oe OE] [--ml ML] [--ri RI]<br><br>

#### Using hints:
`:[hint_name]=[argument]`<br>
List of hints:<br>
- **oe** (Odd or Even) - shows whether the guessed number is odd or even. Does not require arguments.<br>
- **ml** (More or Less) - indicates if your number is higher or lower compared to the guessed number. Requires one mandatory argument.<br>
- **ri** (Random Interval) - shows the interval in which the guessed number falls. Does not require arguments.<br><br>

#### Example usage:
1) `:oe`<br>
2) `:ml=54`<br>
3) `:ri`<br><br>

### Options:
- `-h, --help`  &nbsp;&nbsp;&nbsp;&nbsp;  Show help message and exit<br>
- `-l LEFT_BOUND, --left_bound LEFT_BOUND` &nbsp;&nbsp;&nbsp;&nbsp; Left bound of the range. Default = 0<br>
- `-r RIGHT_BOUND, --right_bound RIGHT_BOUND` &nbsp;&nbsp;&nbsp;&nbsp; Right bound of the range. Default = 1<br>
- `-a ATTEMPTS_COUNT, --attempts_count ATTEMPTS_COUNT` &nbsp;&nbsp;&nbsp;&nbsp; Number of attempts. Default = 3<br>
- `-m MENU, --menu MENU` &nbsp;&nbsp;&nbsp;&nbsp; Show game menu. Default = 1<br>
- `--oe OE` &nbsp;&nbsp;&nbsp;&nbsp; Number of :oe hints. Default = 1<br>
- `--ml ML` &nbsp;&nbsp;&nbsp;&nbsp; Number of :ml hints. Default = 1<br>
- `--ri RI` &nbsp;&nbsp;&nbsp;&nbsp; Number of :ri hints. Default = 1<br>