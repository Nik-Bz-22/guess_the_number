from art import tprint

def display_welcome_message():
    tprint("Guess   Number", font="medium")


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