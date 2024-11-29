from assets.theory import *
from assets.options import *

# Main loop
while True:
    cls()
    user_input = input(TERMINAL_SEARCH)

    if user_input in OPTION_TERMINAL:
        user_input_scale_search = input("What notes do you have in mind?: ")
        print(scale_search(user_input_scale_search.upper()))
        next_cmd()
    else:
        redo()