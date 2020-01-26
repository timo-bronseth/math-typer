"""
...

Timo Brønseth, January 2020.
"""
from pynput.keyboard import Key, Listener, Controller
# Package docs: https://pythonhosted.org/pynput/


# GLOBAL VARIABLES
LAST_WORD = ""  # Need this to check against two-word symbols.
CURRENT_WORD = ""  # All keyboard presses gets recorded here and then recinded once space is pressed.
ALPHABET = tuple("abcdefghijklmnopqrstuvwxyz")

keyboard = Controller()
ctrl_modifier = False


def add_to_word(character: str) -> None:
    """
    Updates global word if character is in alphabet.
    """
    global CURRENT_WORD

    character = character.replace("'", "")
    if character in ALPHABET:
        CURRENT_WORD += character


def is_space(key):
    """
    Resets CURRENT WORD and returns True if key is space, False otherwise.
    """
    global CURRENT_WORD, LAST_WORD

    if key == Key.space:
        return True
    else:
        return False


def is_symbol(symbol: str) -> bool:
    global CURRENT_WORD, LAST_WORD
    phrase = LAST_WORD + " " + CURRENT_WORD

    if symbol == CURRENT_WORD:
        # You are currently pressing ctrl, so we only need to
        # press backspace once to delete the last word you typed.
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        CURRENT_WORD = ""
        return True

    elif symbol == phrase:
        # You are currently pressing ctrl, so we only need to
        # press backspace twice to delete the two last words you typed.
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        CURRENT_WORD = ""
        return True

    else:
        return False


def write_matching_symbols() -> None:
    """..."""
    global CURRENT_WORD, LAST_WORD

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
    global CURRENT_WORD, LAST_WORD, ctrl_modifier

    if is_space(key):

        # If ctrl was the last pressed key before space, write_matching_symbols
        if ctrl_modifier:
            write_matching_symbols()
            ctrl_modifier = False

        # Update words
        LAST_WORD = CURRENT_WORD
        CURRENT_WORD = ""
        return

    # Set ctrl_modifier to True if key is ctrl, otherwise reset it
    ctrl_modifier = True if key == Key.ctrl_l else False

    # Converts the native KeyCode type to str before adding it to CURRENT_WORD
    add_to_word(key.__str__())


def main():

    # Collect events until released
    with Listener(on_press) as listener:
        listener.join()


if __name__ == '__main__':
    main()
