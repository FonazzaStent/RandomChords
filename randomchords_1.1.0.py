"""Random Chords 1.1.0 - A very simple random chord generator.
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
clashes=2
repeats=0
firstchord=0

def init():
    global oktwo
    global okfive
    global oksix
    global chordnotes
    global counter
    global chord
    global chordstring
    global clash
    global repeat
    global notelist
    global occurrencies
    oktwo=0
    okfive=0
    oksix=0
    chordnotes=[]
    chord=[]
    counter=1
    octave=4
    chordstring=""
    clash=0
    repeat=0
    notelist=[]
    occurrencies=[]



def validate_chord():
    global clash
    global repeat
    global notelist
    global occurrencies
    for note in chord:
        #print (note)
        for checknote in chord:
            #print (checknote)
            diff=notes.index(note)-notes.index(checknote)
            if diff==1 or diff==-1 or diff==11 or diff==-11:
                clash=clash+1
    occ_check=0
    note_occ=chord[0]
    notelist.append(note_occ)
    occurrencies.append(0)
    for note in chord:
        note_occ=note
        items=len(notelist)
        for x in range (0,items):
            if note_occ==notelist[x]:
                count=int(occurrencies[x])
                occurrencies[x]=count+1
                occ_check=1
        if occ_check==0:
            notelist.append(note_occ)
            occurrencies.append(1)
        occ_check=0
    for value in occurrencies:
        if value>1:
            repeat=repeat+1
    
init()
while True:

    root= randint(1,12)
    
    lowest=randint(2,11)
    chord.append(notes[root-1])
    lowestvalue=root+lowest
    if lowestvalue>12:
        lowestvalue=lowestvalue-12
    chord.append(notes[lowestvalue-1])
    
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
    validate_chord()
    if clash<clashes and repeat<=repeats:
        if firstchord==1:
            print ("\n")
            if clashes==1000:
                print ("More than one clash allowed")
            else:
                print("Only one clash allowed")
            print (repeats, "repeated notes allowed")

            print ("root= ",notes[root-1])
            print ("lowest= ",notes[lowestvalue-1])
            print ("Intervals= ",chordnotes)
            for items in chord:
                chordstring=chordstring+items+" "
            print ("chord= ",chordstring)
            print ("\n")
            more=input("Enter for new chord, q to quit ")
            if more=="q":
                quit()
        firstchord=1
        configure=input("c to configure, Enter for default parameters: ")
        if configure=="c":
            clashesyes=""
            while clashesyes!="y" and clashesyes!="n":
                clashesyes=input("Allow more than one clash? (y=yes n=no): ")
                if clashesyes=="y":
                    clashes=1000
                if clashesyes=="n":
                    clashes=2
            repeats=-1
            while repeats<0 or repeats>4:
                repeats=int(input("How many repeated notes allowed? (0 to 3): "))
                
    init()


