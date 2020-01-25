"""
...

Timo Brønseth, January 2020.
"""
from pynput.keyboard import Key, Listener
# Package docs: https://pythonhosted.org/pynput/


# TODO: Choose between these two packages
#           https://pypi.org/project/keyboard/
#           https://pythonhosted.org/pynput/


# GLOBAL VARIABLES
CURRENT_WORD = []  # All keyboard presses gets recorded here and then recinded once space is pressed.





def on_press(key):
    print('{0} pressed'.format(
        key))


def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False


if __name__ == '__main__':
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    # keyboard_module_test()