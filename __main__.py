"""
...

Timo Brønseth, January 2020.
"""
from pynput.keyboard import Key, Listener
# Package docs: https://pythonhosted.org/pynput/


# GLOBAL VARIABLES
CURRENT_WORD = ""  # All keyboard presses gets recorded here and then recinded once space is pressed.
ALPHABET = tuple("abcdefghijklmnopqrstuvwxyz")


def update_word(character: str) -> None:
    """
    Updates global word if character is in alphabet.
    """
    global CURRENT_WORD

    character = character.replace("'", "")
    if character in ALPHABET:
        CURRENT_WORD += character


def check_if_space(key):
    """
    Returns True if key is space, False otherwise.
    """
    if key == Key.space:
        return True
    else:
        return False


def on_press(key):
    global CURRENT_WORD

    if check_if_space(key):
        CURRENT_WORD = ""
        return

    # Converts the native KeyCode type to str, and then passes it to _get_char()
    # before adding it to CURRENT_WORD.
    update_word(key.__str__())
    check_if_symbol():

    if CURRENT_WORD == "timo":
        print("TIMO")



def on_release(key):
    # print('{0} release'.format(
    #     key))
    if key == Key.esc:
        # Stop listener
        return False


def main():
    # TODO: DEFINE GLOBAL VARIABLES HERE
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    main()
