# imports
from assets.music_theory import *
from assets.menu_options import *

# Main loop
while True:
    cls()
    user_input = input(TERMINAL_SEARCH)

    if user_input in OPTION_TERMINAL:
        print('For flats like G-flat or B-flat: \'Gb\' or \'Bb\'')
        user_input_scale_search = input("What notes do you have in mind?: ")
        print_options(scale_search(user_input_scale_search.upper()))
        next_cmd()
    elif user_input in OPTION_CHORD_PROG:
        print_options(f'{CHORD_PROGRESSION_FEELINGS.keys()}')
        user_input_chord_progression_search = input("What emotion are you going for?: ")
        pass
    elif user_input in OPTION_QUIT:
        cls()
        print('Thanks for using the \'Music-Theory-Search\' Program')
        break
    else:
        redo()