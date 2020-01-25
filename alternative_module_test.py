import keyboard
# Package docs: https://pypi.org/project/keyboard/


def keyboard_module_test():
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                print('You Pressed A Key!')
                break  # finishing the loop
        except:
            break  # if user pressed a key other than the given key the loop will break


if __name__ == '__main__':
    keyboard_module_test()