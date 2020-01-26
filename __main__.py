"""
Lets you type math symbols by typing their names and then hitting ctrl + space.

I wrote this in a haste, so I realise some things can be done more elegantly.
For example, you can only define shortcuts of up to two words, so "for all"
works but not "if and only if". Write your own fix to it if you need.

Define your own shortcuts in the replace_matching_symbols function.

Timo Brønseth, January 2020.
"""
from pynput.keyboard import Key, Listener, Controller
# Package docs: https://pythonhosted.org/pynput/


# GLOBAL CONSTANTS
ALPHABET = tuple("abcdefghijklmnopqrstuvwxyz")

# GLOBAL VARIABLES
last_word = ""  # Need this to check against two-word symbols.
current_word = ""  # All keyboard presses gets recorded here and then recinded once space is pressed.
keyboard = Controller()
ctrl_modifier = False


def add_to_word(character: str) -> None:
    """
    Updates global word if character is in alphabet.
    """
    global current_word

    character = character.replace("'", "")
    if character in ALPHABET:
        current_word += character


def is_space(key):
    """
    Returns True if key is space, False otherwise.
    """
    global current_word, last_word

    if key == Key.space:
        return True
    else:
        return False


def is_symbol(symbol: str) -> bool:
    """
    Checks if user has typed anything that corresponds to one of the
    defined symbols, and then presses backspace to delete that/those
    words before returning True or False to caller function.
    """
    global current_word, last_word
    phrase = last_word + " " + current_word

    if symbol == current_word:
        # You are currently pressing ctrl, so we only need to
        # press backspace once to delete the last word you typed.
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        current_word = ""
        return True

    elif symbol == phrase:
        # You are currently pressing ctrl, so we only need to
        # press backspace twice to delete the two last words you typed.
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        current_word = ""
        return True

    else:
        return False


def replace_matching_symbols() -> None:
    """..."""
    global current_word, last_word

    if is_symbol("and"):
        keyboard.type("∧")
        return

    elif is_symbol("or"):
        keyboard.type("∨")
        return

    elif is_symbol("xor"):
        keyboard.type("⊻")
        return

    elif is_symbol("implies"):
        keyboard.type("→")
        return

    elif is_symbol("biconditional"):
        keyboard.type("↔")
        return

    elif is_symbol("there exists"):
        keyboard.type("∃")
        return

    elif is_symbol("negative existential"):
        keyboard.type("∄")
        return

    elif is_symbol("for all"):
        keyboard.type("∀")
        return

    elif is_symbol("times"):
        keyboard.type("×")
        return

    elif is_symbol("union"):
        keyboard.type("∪")
        return

    elif is_symbol("intersection"):
        keyboard.type("∩")
        return

    elif is_symbol("proper subset"):
        keyboard.type("⊂")
        return

    elif is_symbol("subset"):
        keyboard.type("⊆")
        return

    elif is_symbol("not subset"):
        keyboard.type("⊄")
        return

    elif is_symbol("proper superset"):
        keyboard.type("⊃")
        return

    elif is_symbol("superset"):
        keyboard.type("⊇")
        return

    elif is_symbol("element of"):
        keyboard.type("∈")
        return

    elif is_symbol("not element"):
        keyboard.type("∉")
        return

    elif is_symbol("empty set"):
        keyboard.type("∅")
        return

    # Apparently keyboard won't type these.
    # elif is_symbol("natural numbers"):
    #     keyboard.type("ℕ")
    #     return
    #
    # elif is_symbol("rational numbers"):
    #     keyboard.type("ℚ")
    #     return
    #
    # elif is_symbol("universal set"):
    #     keyboard.type("𝕌")
    #     return
    #
    # elif is_symbol("real numbers"):
    #     keyboard.type("ℝ")
    #     return
    #
    # elif is_symbol("primes"):
    #     keyboard.type("ℙ")
    #     return
    #
    # elif is_symbol("complex numbers"):
    #     keyboard.type("ℂ")
    #     return

    elif is_symbol("not"):
        keyboard.type("¬")
        return


def on_press(key):
    global current_word, last_word, ctrl_modifier

    if is_space(key):

        # If ctrl was the last pressed key before space, write_matching_symbols
        if ctrl_modifier:
            replace_matching_symbols()
            ctrl_modifier = False

        # Update words
        last_word = current_word
        current_word = ""
        return

    # Set ctrl_modifier to True if key is ctrl, otherwise reset it
    ctrl_modifier = True if key == Key.ctrl_l else False

    # Converts the native KeyCode type to str before adding it to current_word
    add_to_word(key.__str__())


def main():

    # Collect events until released
    with Listener(on_press) as listener:
        listener.join()


if __name__ == '__main__':
    main()
