"""Random Chords 1.0.0 - A very simple random chord generator.
Copyright (C) 2023  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import random
from random import randint
intervals=[2,3,4,5,6]
notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

def init():
    global oktwo
    global okfive
    global oksix
    global chordnotes
    global counter
    global chord
    global chordstring
    oktwo=0
    okfive=0
    oksix=0
    chordnotes=[]
    chord=[]
    counter=1
    octave=4
    chordstring=""
    

init()
while True:
    print ("\n")
    root= randint(1,12)
    print ("root= ",notes[root-1])
    lowest=randint(2,11)
    chord.append(notes[root-1]+"2")
    lowestvalue=root+lowest
    if lowestvalue>12:
        lowestvalue=lowestvalue-12
    chord.append(notes[lowestvalue-1]+"4")
    print ("lowest= ",notes[lowestvalue-1])
    notevalue=lowestvalue
    
    while counter<5:
        interval=random.choice(intervals)
        if interval!=2 and interval!=5 and interval!=6:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>12:
                notevalue=notevalue-12
            chord.append(notes[notevalue-1])
            counter=counter+1
        if interval==2 and oktwo==0:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>12:
                notevalue=notevalue-12
            chord.append(notes[notevalue-1])
            counter=counter+1
        if interval==5 and okfive==0:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>12:
                notevalue=notevalue-12
            chord.append(notes[notevalue-1])
            counter=counter+1
        if interval==6 and oksix==0:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>12:
                notevalue=notevalue-12
            chord.append(notes[notevalue-1])
            counter=counter+1
        if interval==2:
            oktwo=1
        if interval==5:
            okfive=1
        if interval==6:
            oksix=1
    print ("Intervals= ",chordnotes)
    for items in chord:
        chordstring=chordstring+items+" "
    print ("chord= ",chordstring)
    init()
    print ("\n")
    more=input("Enter for new chord, q to quit ")
    if more=="q":
        quit()
