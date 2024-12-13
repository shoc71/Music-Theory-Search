from assets.music_theory import *
from assets.menu_options import *

# Main loop
while True:
    cls()
    user_input = input(TERMINAL_SEARCH)

    if user_input in OPTION_TERMINAL:
        user_input_scale_search = input("What notes do you have in mind?: ")
        print(scale_search(user_input_scale_search.upper()))
        next_cmd()
    elif user_input in OPTION_QUIT:
        cls()
        print('Thanks for using the \'Music-Theory-Search\' Program')
        break
    else:
        redo()