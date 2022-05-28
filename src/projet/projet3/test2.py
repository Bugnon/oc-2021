tiles = """
01001001010010010000
01001001010010010000
010g1001010p10010000
01001001010010010000
01001001010g10010000
"""

state = []

"""This shows how to split into lines, and how to split lines into characters."""
for line in tiles.split():
    print(line)
    state.append(line)
    state_line = []
    for c in line:
        if c  == 'p':
            ...
        elif c == 'g':
            ...
        else:
            state_line.append(int(c))

    