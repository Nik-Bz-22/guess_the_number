import random
class GuessTheNumberGame:

    def __init__(self, attempts_count=1, left_bound=0, right_bound=1):
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.attempts_count = attempts_count
        self.target_number = None

    def __str__(self):
        return f"[{self.left_bound} : {self.right_bound}] ({self.attempts_count})"

    def set_bounds(self, left, right):
        self.left_bound = left
        self.right_bound = right

    def set_and_get_num(self):
        self.target_number = random.randint(self.left_bound, self.right_bound)


    def compare_answer(self, answ):
        if answ == self.target_number:
            return 1
        return 0

    def check_answer(self, answ):
        if self.left_bound > answ or self.right_bound < answ:
            return 0
        return 1

    def play(self):
        self.set_and_get_num()
        print(self.target_number)
        for atmp in range(1, self.attempts_count+1):
            print(f"Your attempt #{atmp}")

            while (answer := input('Enter your number: ')) and (not answer.isdigit()):
                print(f"<{answer}>", "[It isn't a number]")
            else:
                answer = int(answer)


            if not self.check_answer(answer):
                print("[Your number out of range]")

            if self.compare_answer(answer):
                print("YOU WIN")
                return

            print("TRY AGAIN\n", "_"*20, sep="")



game = GuessTheNumberGame(attempts_count=3, left_bound=5, right_bound=20)
game.play()