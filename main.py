import random


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



class Tips:
    def odd_or_even(self, settings={}):
        print("Odd" if settings["game"].target_number % 2 == 1 else "Even")


class GuessTheNumberGame:
    tips_gen = Tips()
    def __init__(self, attempts_count=1, left_bound=0, right_bound=1):
        self.left_bound      = left_bound if left_bound < right_bound else 0
        self.right_bound     = right_bound if right_bound > left_bound else 1
        self.attempts_count  = attempts_count if attempts_count > 0 else 1
        self.target_number   = None
        self.set_and_get_num()

        self.message         = f'[{self.left_bound} : {self.right_bound}]\nEnter your number: '
        self.tips            = {
                                    ":oe": {"func": GuessTheNumberGame.tips_gen.odd_or_even, "count": 1},

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

    @handle_keyboard_interrupt
    def play(self):
        # self.set_and_get_num()
        print(self.target_number)
        for atmp in range(1, self.attempts_count+1):
            rest = self.attempts_count-atmp
            print(f"Your attempt #{atmp} ({rest} more left)")

            while (answer := input(self.message).strip()) and (not answer.lstrip('-').isdigit()) or (len(answer) <= 0):

                if answer in self.tips:
                    if self.tips[answer]["count"] > 0:
                        self.tips[answer]["func"]({"game": self})
                        self.tips[answer]["count"] -= 1
                    else:
                        print(f"You've run out of ({answer}) tips")
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





if __name__ == "__main__":
    import cli_handler
    cli_handler.display_welcome_message()
    args_ = cli_handler.get_cli_args()
    game = GuessTheNumberGame(**args_)
    game.play()


