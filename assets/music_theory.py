try:
    from assets.utils import *
except:
    from .utils import *

SCALE = {
    'C Major' : ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'G Major (#1)' : ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
    'D Major (#2)' : ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
    'A Major (#3)' : ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
    'E Major (#4)' : ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
    'B Major (#5)' : ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
    'F# Major (#6)' : ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#'],
    'C# Major (#7)' : ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#'],
    'F Major (1♭)' : ['F', 'G', 'A', 'B♭', 'C', 'D', 'E'],
    'B♭ Major (2♭)' : ['B♭', 'C', 'D', 'E♭', 'F', 'G', 'A'],
    'E♭ Major (3♭)' : ['E♭', 'F', 'G', 'A♭','B♭', 'C', 'D'],
    'A♭ Major (4♭)' : ['A♭', 'B♭', 'C', 'D♭', 'E♭', 'F', 'G'],
    'D♭ Major (5♭)' : ['D♭', 'E♭', 'F', 'G♭', 'A♭', 'B♭', 'C'],
    'G♭ Major (6♭)' : ['G♭', 'A♭', 'B♭', 'C♭', 'D♭', 'E♭', 'F'],
    'C♭ Major (7♭)' : ['C♭', 'D♭', 'E♭', 'F♭', 'G♭', 'A♭', 'B♭']
}

def scale_search(user_input: str):
    if string_cleaning(user_input) == True:
        cleaned_str = user_input.replace(" ","").replace(',','').replace('-','').replace('b','♭').upper()
        cleaned_list = music_str_to_list(cleaned_str)
        
    matching_scales = []
    for key, value in SCALE.items():
        # Check if the user's input matches the notes in the scale
        if all(note in value for note in cleaned_list):
            matching_scales.append({key: value})  # Store the result as a dictionary
        
    if matching_scales:
        return matching_scales
    else:
        return ["No matching scales found."]