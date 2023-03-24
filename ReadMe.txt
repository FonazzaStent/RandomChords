RandomChords 1.1.0

The program can generate random 6 note chords.
Run the executable and you will be asked if you want to configure parameters or generate a chord with
default parameters.
Input "c" to configure or Enter for default.
If you choose to configure, you can choose if the chord should have more than one clash (notes at one
semitone distance) and how many repeated notes should be allowed. Just input the right value at the prompt.


The chord will be displayed in a terminal window, in the following format:

root=  D
lowest=  C
Intervals=  [6, 2, 5, 3]
chord=  D C F# G# C# E

Root: the chord root, placed on octave n. 2 of a preset inside a DAW or other music program.
Lowest: the lowest note of the chord, placed on octave 4.
Intervals: first interval is the distance in semitones from the lowest note, second interval distance from
the second note and so on.
Chord: the chord expressed in note names. First note is the root on octave 2, second note is the lowest note
of the chord on octave 4, the other notes are above the lowest note, ending possibly on higher octaves.

At prompt input Enter to generate a new chord, "q" to quit the program. Just closing the terminal window will
also close the program.

New in this version:

- Improved algorithm, now allows to configure number of clashes and repeated notes.