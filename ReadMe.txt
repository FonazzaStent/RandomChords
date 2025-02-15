RandomChords 2.1.2
Fonazza-Stent

The purpose of the program is to generate random chords to inspire music
creation. It can generate chords from 4 to 13 notes, with or without
dissonances and repeated notes. All the 7 notes scales matching the chord
notes will also be generated and displayed. You can listen to the
resulting chord and scales through the built-in play function.

- Settings -

Number of notes - This is the number of notes you want the chord to
contain.
Input a number from 4 to 13. The default value is 5.

Repeated notes - Input a number from 0 to 13 to determine how many notes
can be repeated in the chord. The default value is 0.

Dissonances - Input a number from 0 to 13 to tell the program how many
dissonances (notes at one semitone distance) the chord should contain. The
default value is 0.

Lowest interval - The lowest interval between notes expressed in number
Of semitones. Accepts values from 2 to 11. The default value is 2.

Highest interval - The highest interval between notes expressed in number
of semitones. Accepts values from 3 to 11. The default value is 7.

If the program cannot find a chord with the parameters you have set, it
will try 10,000 combinations, then modify the parameters by increasing
the number of dissonances and repeated notes allowed, then try 10,000 more
combinations.

- Play and Save chords, scales and history-

The chord will be displayed in the Chord box (above the "Chord" label).
All matching scales will be displayed in the Scale combo box (above the
"Scale" label). You can click on the arrow at the right of the box to
select the scale you want to play.

Click on the "Play chord" button or Play menu- Play chord to play the
chord.

File menu - Save chord or Alt-C to save the chord as a MIDI file.

Click on the "Play scale" button or Play menu - Play scale to play the
scale selected in the "Scale" box.

File menu - Save scale or Alt-S to save the scale as a MIDI file.

You can import the MIDI files into a DAW or another kind of scoring
program supporting MIDI import.

The chord and the matching scales will also be displayed in the history
Window (below the Chord and Scale boxes), in the following format:

0  dissonances allowed
0  repeated notes allowed

chord=  F D# G# C#


Scales:
Match 1:  F F# G# A B C# D#
Match 2:  F F# G# A# B C# D#
Match 3:  F F# G# A# C C# D#
Match 4:  F G G# A# B C# D#
Match 5:  F G G# A# C C# D#


Chord: the chord expressed in letter notation. The first note is the
root, on the lowest octave (the bass), the second note is the lowest note
of the chord,the other notes are above the lowest note, ending possibly
on higher octaves.

Scales: all the scales built on the chord root containing the
notes of the chord.

The text in the chord box and in the history window can be copied for use
in another program or for sharing through right click - Copy, CTRL-V or
CTRL-Ins. It can also be saved to a text file through File menu - Save
history. File menu - Erase history to erase the history window.

New in this version:

- More scales added
