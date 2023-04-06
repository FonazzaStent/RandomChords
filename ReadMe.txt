RandomChords 1.3.0

The purpose of the program is to generate random chords to inspire music creation.
Run the executable and you will be asked if you want to configure parameters or generate a chord with
the default parameters.
Input "c" to configure or Enter for default.

- Parameters -
(Progression? - This option is available after the first chord. Read "Progression" paragraph below.)
How many clashes allowed? - Input a number from 0 to 13 to tell the program how many clashes (notes at one
semitone distance) the chord should contain. The default value is 0.
How many repeated notes allowed? - Input a number from 0 to 13 to determine how many notes can be repeated
in the chord. The default value is 0.
How many notes? - This is the number of notes you want the chord to contain. Input a number from 4 to 13.
The default value is 4.
Lowest interval? - The lowest interval between notes expressed in number of semitones. Accepts values from
1 to 11. The default value is 2.
Highest interval? - The highest interval between notes expressed in number of semitones. Accepts values
from 3 to 11. The default value is 7.

If the program cannot find a chord with the parameters you have set, it will try 10,000 combinations, then
modify the parameters by increasing the number of clashes and repeated notes allowed, then try 10,000 more
combinations. In order to reset the parameters, you will have to choose the configuration option again at
the prompt.

The chord will be displayed in a terminal window, in the following format:

0  clashes allowed
0  repeated notes allowed

chord=  F D# G# C#


Scales:
Match 1:  F F# G# A B C# D#
Match 2:  F F# G# A# B C# D#
Match 3:  F F# G# A# C C# D#
Match 4:  F G G# A# B C# D#
Match 5:  F G G# A# C C# D#


Chord: the chord expressed in letter notation. First note is the root on the lowest octave (the bass),
second note is the lowest note of the chord, the other notes are above the lowest note, ending possibly on
higher octaves.
Scales: all the 7 note scales built on the chord root containing the notes of the chord.

At the prompt input Enter to generate a new chord, "q" to quit the program. Just closing the terminal window
will also close the program.

Progression:
After the first chord, if you choose to configure and then choose "y" (for yes) at the "Progression?"
prompt, the program will generate a progression built on the first scale matching the previous chord.

How many chords? - input a number from 2 to 16, default 2.

The program will ask you if you want to configure the first chord. You can configure parameters or hit 
Enter to generate a chord with the same parameters as previous chord. Repeat the operation for the other
chords of the progression. When all the chords have been generated, the program will display the whole
progression.


New in this version:

- can generate progressions built on the first scale matching the chord notes