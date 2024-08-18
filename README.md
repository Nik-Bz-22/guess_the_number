# Guess The Number

## Usage

### usage: `main.py` [-h] [-l LEFT_BOUND] [-r RIGHT_BOUND] [-a ATTEMPTS_COUNT] [-m MENU] [--oe OE] [--ml ML] [--ri RI]<br><br>

#### Using tips:
`:[tip_name]=[argument]`<br>
List of tips:<br>
- **oe** (Odd or Even) - показывает, является ли загаданное число чётным или нечётным. Не требует аргументов.<br>
- **ml** (More or Less) - указывает, больше или меньше ваше число по сравнению с загаданным. Требует один обязательный аргумент.<br>
- **ri** (Random Interval) - показывает, в какой интервал попадает загаданное число. Не требует аргументов.<br><br>

#### Example usage:
1) `:oe`<br>
2) `:ml=54`<br>
3) `:ri`<br><br>

### Options:
- `-h, --help`  &nbsp;&nbsp;&nbsp;&nbsp;  Показать справку и выйти<br>
- `-l LEFT_BOUND, --left_bound LEFT_BOUND` &nbsp;&nbsp;&nbsp;&nbsp; Левый предел диапазона. По умолчанию = 0<br>
- `-r RIGHT_BOUND, --right_bound RIGHT_BOUND` &nbsp;&nbsp;&nbsp;&nbsp; Правый предел диапазона. По умолчанию = 1<br>
- `-a ATTEMPTS_COUNT, --attempts_count ATTEMPTS_COUNT` &nbsp;&nbsp;&nbsp;&nbsp; Количество попыток. По умолчанию = 3<br>
- `-m MENU, --menu MENU` &nbsp;&nbsp;&nbsp;&nbsp; Показать меню игры. По умолчанию = 1<br>
- `--oe OE` &nbsp;&nbsp;&nbsp;&nbsp; Количество подсказок :oe. По умолчанию = 1<br>
- `--ml ML` &nbsp;&nbsp;&nbsp;&nbsp; Количество подсказок :ml. По умолчанию = 1<br>
- `--ri RI` &nbsp;&nbsp;&nbsp;&nbsp; Количество подсказок :ri. По умолчанию = 1<br>

