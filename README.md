# random_number_mykyta
## Usage
  ### usage: main.py [-h] [-l LEFT_BOUND] [-r RIGHT_BOUND] [-a ATTEMPTS_COUNT] [-m MENU] [--oe OE] [--ml ML] [--ri RI]<br><br>

  #### Using tips:
  :[tip_name]=[argument]<br>
  List of tips:<br>
  oe (Odd or Even) - will show whether the guessed number is even or odd. It has no arguments.<br>
  ml (More or Less) - will show if your provided number is greater or less than the guessed number. It has one required argument.<br>
  ri (Random Interval) - will show which interval the number belongs to. It has no arguments.<br><br>

  #### Example usage:
  1) :oe <br>
  2) :ml=54<br>
  3) :ri<br><br>


### options:
-h, --help            show this help message and exit<br>
-l LEFT_BOUND, --left_bound LEFT_BOUND
                      Left bound of range. Default=0 <br>
-r RIGHT_BOUND, --right_bound RIGHT_BOUND
                      Right bound of range. Default=1<br>
-a ATTEMPTS_COUNT, --attempts_count ATTEMPTS_COUNT
                      Number of attempts. Default=3<br>
-m MENU, --menu MENU  Display game menu. Default=1<br>
--oe OE               Count of :oe tips. Default=1<br>
--ml ML               Count of :ml tips. Default=1<br>
--ri RI               Count of :ri tips. Default=1<br>
