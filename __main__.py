"""
Lets you type math symbols by first activating CAPS LOCK, typing their names,
and then deactivating CAPS LOCK again. E.g. '[CAPS] for all [CAPS]' = ∀.

Define your own shortcuts in the replace_matching_symbols function.

OBS! Start it with CAPS LOCK inactive.

Timo Brønseth, January 2020.
"""
from pynput.keyboard import Key, Listener, Controller
# Package docs: https://pythonhosted.org/pynput/


# GLOBAL CONSTANTS
ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"  # Includes space.

# GLOBAL VARIABLES
current_phrase = ""  # All characters get recorded here
keyboard = Controller()
caps_lock = False  # Start in inactive mode


def add_to_phrase(character: str) -> None:
    """
    Adds character to global phrase if it is in ALPHABET.
    """
    global current_phrase

    character = character.replace("'", "")
    character = " " if character == 'Key.space' else character
    if character in ALPHABET:
        current_phrase += character


def is_symbol(symbol: str) -> bool:
    """
    Checks if user has typed anything that corresponds to one of the
    defined symbols, and then presses backspace to delete that/those
    words before returning True or False to caller function.
    """
    global current_phrase

    if symbol == current_phrase.lower():

        # Press backspace as many times as there are letters in current_phrase
        for letter in current_phrase:
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)

        # Reset current_phrase
        current_phrase = ""
        return True
    else:
        return False


def replace_matching_symbols() -> None:
    """Replaces text typed by user with the corresponding symbol, if it exists."""
    global current_phrase

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

    elif is_symbol("iff") or is_symbol("if and only if") or is_symbol("exclusive conditional"):
        keyboard.type("↔")
        return

    elif is_symbol("there exists"):
        keyboard.type("∃")
        return

    elif is_symbol("negative existential") or is_symbol("there does not exist"):
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

    elif is_symbol("not a subset"):
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

    elif is_symbol("is not element of"):
        keyboard.type("∉")
        return

    elif is_symbol("empty set"):
        keyboard.type("∅")
        return

    elif is_symbol("less than or equal to") or is_symbol("inclusive less"):
        keyboard.type("≤")
        return

    elif is_symbol("more than or equal to") or is_symbol("inclusive more"):
        keyboard.type("≥")
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

    elif is_symbol("cup of tea"):
        keyboard.type("cÚ")
        return


def on_press(key):
    global current_phrase, caps_lock

    # Do these things upon hitting the caps lock key.
    if key == Key.caps_lock:
        # Toggle caps_lock variable
        caps_lock = True if caps_lock is False else False

        # Check for matching symbols and type them in if caps_lock is being deactivated
        if caps_lock is False:
            replace_matching_symbols()
            current_phrase = ""  # Reset phrase

    # Only add characters to current_phrase if caps lock is on
    if caps_lock:
        # Converts the native KeyCode type to str before adding it to current_phrase
        add_to_phrase(key.__str__())


def main():

    # Collect events until released
    with Listener(on_press) as listener:
        listener.join()


if __name__ == '__main__':
    main()
