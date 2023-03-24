RandomChords 1.2.0

The purpose of the program is to generate random chords to inspire music creation.
Run the executable and you will be asked if you want to configure parameters or generate a chord with
the default parameters.
Input "c" to configure or Enter for default.

- Parameters -
How many clashes allowed? - Input a number from 0 to 13 to tell the program how many clashes (notes at one
semitone distance) the chord should contain. The default value is 1.
How many repeated notes allowed? - Input a number from 0 to 13 to determine how many notes can be repeated
in the chord. The default value is 0.
How many notes? - This is the number of notes you want the chord to contain. Input a number from 4 to 13.
The default value is 6.
Lowest interval? - The lowest interval between notes expressed in number of semitones. Accepts values from
1 to 11. The default value is 2.
Highest interval? - The highest interval between notes expressed in number of semitones. Accepts values
from 2 to 11.

If the program cannot find a chord with the parameters you have set, it will try 10,000 combinations, then
modify the parameters, by increasing the number of clashes and repeated notes allowed, then try 10,000 more
combinations. In order to reset the parameters, you will have to choose the configuration option again at
the prompt.

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

- Improved algorithm, now allows to configure number of clashes, repeated notes, number of notes, lowest and
highest interval allowed in the chord.