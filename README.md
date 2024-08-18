# random_number_mykyta
## Usage
  ### usage: main.py [-h] [-l LEFT_BOUND] [-r RIGHT_BOUND] [-a ATTEMPTS_COUNT] [-m MENU] [--oe OE] [--ml ML] [--ri RI]

  #### Using tips:
  :[tip_name]=[argument]<br>
  List of tips:
  oe (Odd or Even) - will show whether the guessed number is even or odd. It has no arguments.
  ml (More or Less) - will show if your provided number is greater or less than the guessed number. It has one required argument.
  ri (Random Interval) - will show which interval the number belongs to. It has no arguments.

  #### Example usage:
  1) :oe 
  2) :ml=54
  3) :ri


### options:
-h, --help            show this help message and exit
-l LEFT_BOUND, --left_bound LEFT_BOUND
                      Left bound of range. Default=0 
-r RIGHT_BOUND, --right_bound RIGHT_BOUND
                      Right bound of range. Default=1
-a ATTEMPTS_COUNT, --attempts_count ATTEMPTS_COUNT
                      Number of attempts. Default=3
-m MENU, --menu MENU  Display game menu. Default=1
--oe OE               Count of :oe tips. Default=1
--ml ML               Count of :ml tips. Default=1
--ri RI               Count of :ri tips. Default=1
