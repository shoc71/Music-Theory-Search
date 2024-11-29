# Functions
def cls():
    print("\x1b[2J\x1b[H",end="")

def string_cleaning(string: str):
    for s in string.lower():
        if s not in ['a','b','c','d','e','f','g',"#"," ",","]:
            return False
    return True

def edge_case_list_check(klist: list):
    if len(klist) <= 1:
        return []

    if (klist[0] == "#") or (klist[0] == "♭"):
        del klist[0]

    return klist


def music_str_to_list(string: str):
    new_list = []

    a_list = edge_case_list_check(list(string.upper()))

    # making sure that something like G# goes together instead of 'G', "#"
    skip = False
    for index in range(len(a_list)):

        if skip == True:
            skip = False # Skip this iteration
            continue

        if (index + 1 < len(a_list)) and (a_list[index + 1] in "#♭"):
            new_list.append(a_list[index] + a_list[index + 1])
            skip = True # Skip the next character as it's part of the current note
        else:
            new_list.append(a_list[index])

    return new_list

def redo():
    input("Re-type the string again without using foriegn characters." + "\n"
              "Press ['Enter key'] to try again.")
    
def next_cmd():
    input("\nHere are the results...\nPress ['Enter key'] to continus.")