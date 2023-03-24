RandomChords 1.0.0

The program will generate random 6 notes chords. For now it accepts no parameters and has no GUI.
Just run the executable and the chord will be displayed in a terminal window, in the following format:

root=  D
lowest=  C
Intervals=  [6, 2, 5, 3]
chord=  D2 C4 F# G# C# E

Root: the chord root, placed on octave n. 2 of a preset inside a DAW or other music program.
Lowest: the lowest note of the chord, placed on octave 4.
Intervals: first interval is the distance in semitones from the lowest note, second interval distance from
the second note and so on.
Chord: the chord expressed in note names. First note is the root on octave 2, second note the lowest note of
the chord on octave 4, the other notes are above the lowest note, ending possibly on higher octaves.

At prompt input Enter to generate new chord, "q" to quit the program. Just closing the terminal window will
also close the program. 