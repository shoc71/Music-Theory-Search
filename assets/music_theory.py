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

CHORD_PROGRESSION_FEELINGS = {
    'happy' : [
        'I-IV-V', 'I-IV-V7', 'i-III-v-IV', 'I-IV-vi-V', 
        'I-vi-IV-vi', 'ii-IV-I', 'I-ii-V-I', 'I-ii-vi-IV', 
        ' i-III-VII-VI','I-I/III-IV-V'
    ],
    'sad' : [
        'vi-IV-I-V', 'vi-iii-V-IV'
    ],
    'cheerful' : [
        'I-III-IV', 'i-VI-III-VII', 'I-vi-IV-V'
    ],
    'uplifting' : [
        'IV-V-vi-I'
    ]
}

def chord_prog_search(user_input: str):
    pass

'''
iinput doesnt work
'''

def parse_notes(input_str: str):
    valid_notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    accidentals = ['♭', '#']
    
    string_input = input_str.strip().replace(" ", "")
    
    notes = []
    i = 0
    
    while i < len(string_input):
        note = string_input[i]
        if note in valid_notes:
            if ((i + 1) < len(string_input)) and string_input[i + 1] in accidentals:
                note += string_input[i + 1]
                i += 1
            notes.append(note)
        i += 1
        
    return notes

def scale_search(user_input: str):
    cleaned_list = parse_notes(user_input)
        
    matching_scales = []
    for key, value in SCALE.items():
        # Check if the user's input matches the notes in the scale
        if all(note in value for note in cleaned_list):
            matching_scales.append({key: value})  # Store the result as a dictionary
        
    if matching_scales:
        return matching_scales
    else:
        return ["No matching scales found."]