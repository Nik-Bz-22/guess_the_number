import random
import utils
from colorama import Fore


class Tips:

    def odd_or_even(self, settings={}):
        print("Odd" if settings["game"].target_number % 2 == 1 else "Even")
        return 1

    def more_or_less_then(self, settings={}):
        if not settings["arg"]:
            print("You missed an argument for:", "(ml=?)")
            return 0
        try:
            int_arg = int(settings["arg"])
        except ValueError:
            print("Argument must be a number")
            return 0
        target = settings["game"].target_number
        if target > int_arg:
            print(f"{int_arg} is less then target number")

        elif target == int_arg:
            print("It is right answer!!")

        else:
            print(f"{int_arg} is greater then target number")
        return 1

class GuessTheNumberGame:
    tips_gen = Tips()
    def __init__(self, attempts_count=1, left_bound=0, right_bound=1, oe=1, ml=1):
        self.left_bound      = left_bound if left_bound < right_bound else 0
        self.right_bound     = right_bound if right_bound > left_bound else 1
        self.attempts_count  = attempts_count if attempts_count > 0 else 1
        self.target_number   = None
        self.set_and_get_num()

        self.tips            = {
                                    ":oe": {"func": GuessTheNumberGame.tips_gen.odd_or_even, "count": oe},
                                    ":ml": {"func": GuessTheNumberGame.tips_gen.more_or_less_then, "count": ml},
                                }


    def __str__(self):
        return f"Game[{self.left_bound} : {self.right_bound}] ({self.attempts_count})"

    # def set_bounds(self, left, right):
    #     self.left_bound = left
    #     self.right_bound = right

    def set_and_get_num(self):
        self.target_number = random.randint(self.left_bound, self.right_bound)

    def is_right(self, answ):
        if answ == self.target_number:
            return 1
        return 0

    def check_in_range_status(self, answ):
        if self.left_bound > answ or self.right_bound < answ:
            return 0
        return 1

    def command_handle(self, answer) -> bool:
        param = answer.split("=")[:2]
        command = param[0]
        if command in self.tips:
            if self.tips[command]["count"] > 0:
                if self.tips[command]["func"]({"game": self, "arg": param[-1] if len(param) > 1 else None}):
                    self.tips[command]["count"] -= 1
            else:
                print(f"You've run out of ({command}) tips")

            return 1
        return 0


    @utils.handle_keyboard_interrupt
    def play(self):
        # self.set_and_get_num()
        print(self.target_number)
        ll = [f"{item[0]} - {item[1]["count"]}" for item in self.tips.items()]
        print("#" * 30)
        print(f"Yoy have:\t", "\t".join(ll), sep='')
        print("#" * 30)
        for atmp in range(1, self.attempts_count+1):
            rest = self.attempts_count-atmp

            print(f"Your attempt #{atmp} ({rest} more left)")
            print(f"[{self.left_bound} : {self.right_bound}]")

            while (answer := input('Enter your number: ').strip()) and (not answer.lstrip('-').isdigit()) or (len(answer) <= 0):

                if ":" in answer:
                    if self.command_handle(answer):
                        continue
                print(f"<{answer}>", "[It isn't a number]")

            else:
                answer = int(answer)


            if not self.check_in_range_status(answer):
                print("[Your number out of range]")

            if self.is_right(answer):
                print("YOU WIN")
                return

            if rest != 0:
                print("TRY AGAIN\n", "_"*30, sep="")
            else:
                print("This was your last attempt. Bye")



class GameMenu:
    invalid_binary_choice_message = Fore.RED + "You need to enter (0-No or 1-Yes)" + Fore.RESET
    def __init__(self):
        self.selected_lvl_cont = None
        self.selected_lvl_num = None
        self.all_lvls = None

    def _read_config_json(self, filename):
        with open(filename, "r") as config:
            return json.loads(config.read())

    def start_game(self):
        game = GuessTheNumberGame(**self.selected_lvl_cont)
        game.play()

    @utils.error_handle
    def handle_user_lvl(self):
        user_input = input("Enter: ")
        user_input = user_input.strip().split("|")
        settings = user_input[0].split("-")
        tips = user_input[1].split("-")
        if len(user_input) != 2 or len(settings) != 3 or len(tips) != 2 or not list(map(lambda i: int(i), settings+tips)):
            raise Exception
        return settings, tips
    def create_menu(self):
        while True:
            created = input(f"Do you want to play already created levels? (0/1): ")
            if utils.is_binary(created):created = int(created)
            else:
                print(GameMenu.invalid_binary_choice_message)
                continue

            if created:
                self.all_lvls = self._read_config_json("config.json")
                lvl_count = len(self.all_lvls)

                while lv_ch := input(f"Which level do you want to play? (1 - {lvl_count}): "):
                    if not lv_ch.isdigit() or (1 > int(lv_ch) or int(lv_ch) > lvl_count):
                        print(Fore.RED + "Invalid level number" + Fore.RESET)
                        continue
                    break
                self.selected_lvl_num = int(lv_ch)
                # if utils.is_int(lv_ch) and (lvl_num := int(lv_ch)) and 1 >= lvl_num >= lvl_count:
                #     self.selected_lvl_num = lvl_num
                # else:
                #     print(Fore.RED+"Invalid level number"+Fore.RESET)
                self.selected_lvl_cont = self.all_lvls[f"lv{self.selected_lvl_num}"]
                break
            else:
                # yes_create = input("Do you want to create level? (0/1)")

                while (yes_create := input("Do you want to create level? (0/1): ")) and not utils.is_binary(yes_create):
                    print(GameMenu.invalid_binary_choice_message)

                # if utils.is_binary(yes_create): yes_create = int(yes_create)
                # else: print(GameMenu.invalid_binary_choice_message)

                if yes_create:
                    print("Format: left bound(integer)-right bound(integer)-attempts count(integer)|count of tips oe,ml(also written with a hyphen). Example: 1-10-2|1-1")



                    data = self.handle_user_lvl()
                    print(data)


                    valid_settings = list(map(lambda i: int(i), data[0]))
                    valid_tips = list(map(lambda i: int(i), data[1]))

                    self.selected_lvl_cont = {"left_bound": valid_settings[0], "right_bound": valid_settings[1],
                                "attempts_count": valid_settings[2], "oe": valid_tips[0], "ml": valid_tips[1]}
                    break

                else:
                    continue



if __name__ == "__main__":
    import sys
    import json
    if sys.stdin.isatty():    # CLI
        import cli_handler
        args_ = cli_handler.get_cli_args()
    else:      # IDE
        args_ = {"left_bound": 100, "right_bound": 200, "attempts_count": 10, "oe": 3, "ml": 3}
    utils.display_welcome_message()
    # while True:
    #     created = int(input(f"Do you want to play already created levels? (0/1): "))
    #     if created:
    #         with open("config.json", "r") as levels_file:
    #             data = levels_file.read()
    #
    #         lvls = json.loads(data)
    #         lvl_count = len(lvls)
    #
    #         lvl_choice = int(input(f"Which level do you want to play? (1 - {lvl_count}): "))
    #
    #         print(lvls[f"lv{lvl_choice}"])
    #         game = GuessTheNumberGame(**lvls[f"lv{lvl_choice}"])
    #         game.play()
    #     else:
    #         yes_create = int(input("Do you want to create level? (0/1)"))
    #         if yes_create:
    #             print("Format: left bound(integer)-right bound(integer)-attempts count(integer)|count of tips oe,ml(also written with a hyphen). Example: 1-10-2|1-1")
    #             user_input = input("Enter: ").strip().split("|")
    #             settings = user_input[0].split("-")
    #             tips = user_input[1].split("-")
    #             user_lvl = {"left_bound": int(settings[0]), "right_bound": int(settings[1]), "attempts_count": int(settings[2]), "oe": int(tips[0]), "ml": int(tips[1])}
    #             game = GuessTheNumberGame(**user_lvl)
    #             game.play()
    #         else:
    #             continue

    menu = GameMenu()
    menu.create_menu()
    menu.start_game()



