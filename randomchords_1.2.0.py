"""Random Chords 1.2.0 - A very simple random chord generator.
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
clashes=1
repeats=0
firstchord=0
clashlist=["CC#","C#D","DD#","D#E","EF","FF#","F#G","GG#","G#A","AA#","A#B","BC"]
index=1
lowrange=2
hirange=6
notesnumber=6
trycheck=0
def init():
    global oktwo
    global okfive
    global oksix
    global okseven
    global okeight
    global oknine
    global okten
    global okeleven
    global chordnotes
    global counter
    global chord
    global chordstring
    global clash
    global repeat
    global notelist
    global occurrencies
    global clash_occ

    oktwo=0
    okfive=0
    oksix=0
    okseven=0
    okeight=0
    oknine=0
    okten=0
    okeleven=0
    chordnotes=[]
    chord=[]
    counter=1
    octave=4
    chordstring=""
    clash=0
    repeat=0
    notelist=[]
    occurrencies=[]
    clash_occ=[0,0,0,0,0,0,0,0,0,0,0,0]




def validate_chord():
    global clash
    global repeat
    global notelist
    global occurrencies
    global clash_occ
    global clashcount
    for note in chord:
        #print (note)
        for checknote in chord:
            pair=note+checknote
            for clashtype in clashlist:
                if pair==clashtype:
                    clash_occ[clashlist.index(clashtype)]=clash_occ[clashlist.index(clashtype)]+1
    for eachclash in clash_occ:
        clash=clash+eachclash

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
    
    while counter<notesnumber-1:
        interval=randint(lowrange,hirange)
        if interval!=2 and interval<5:
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
        if interval==7 and okseven==0:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>12:
                notevalue=notevalue-12
            chord.append(notes[notevalue-1])
            counter=counter+1
        if interval==8 and okeight==0:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>12:
                notevalue=notevalue-12
            chord.append(notes[notevalue-1])
            counter=counter+1
        if interval==9 and oknine==0:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>12:
                notevalue=notevalue-12
            chord.append(notes[notevalue-1])
            counter=counter+1
        if interval==10 and okten==0:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>12:
                notevalue=notevalue-12
            chord.append(notes[notevalue-1])
            counter=counter+1
        if interval==11 and okeleven==0:
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
        if interval==7:
            okseven=1
        if interval==8:
            okeight=1
        if interval==9:
            oknine=1
        if interval==10:
            okten=1
        if interval==11:
            okeleven=1
        
    validate_chord()

    if clash<=clashes and repeat<=repeats:
        if firstchord==1:
            print ("\n")
            print (clashes, " clashes allowed")
            print (repeats, " repeated notes allowed")

            print ("root= ",notes[root-1])
            print ("lowest= ",notes[lowestvalue-1])
            print ("Intervals= ",chordnotes)
            for items in chord:
                chordstring=chordstring+items+" "
            print ("chord= ",chordstring)
            print ("\n")
            if trycheck==1:
                """clashes=clashes_mem
                repeats=repeats_mem"""
                True
                trycheck=0
            more=input("Enter for new chord, q to quit ")
            if more=="q":
                quit()
        firstchord=1
        configure=input("c to configure, Enter for default parameters: ")
        if configure=="c":
            clashesyes=-1
            while clashesyes<0 or clashesyes>13:
                clashesinput=input("How many clashes allowed? (0 to 13, default 1): ")
                if clashesinput.isdigit():
                    clashesyes=int(clashesinput)
                    clashes=clashesyes
                    clashes_mem=clashes
                if clashesinput=='':
                    clashesyes=1
                    clashes=clashesyes
            repeats=-1
            while repeats<0 or repeats>13:
                repeatinput=input("How many repeated notes allowed? (0 to 13, default 0): ")
                if repeatinput.isdigit():
                    repeats=int(repeatinput)
                    repeats_mem=repeats
                if repeatinput=='':
                    repeats=0
            notesnumber=-1
            while notesnumber <4 or notesnumber>13:
                inputnotesnumber=input("How many notes? (4 to 13, default 6): ")
                if inputnotesnumber.isdigit():
                    notesnumber=int(inputnotesnumber)
                if inputnotesnumber=='':
                    notesnumber=6
            lowrange=-1
            while lowrange <1 or lowrange>11:
                lowrangeinput=input("Lowest interval? (1 to 11, default 2): ")
                if lowrangeinput.isdigit():
                    lowrange=int(lowrangeinput)
                if lowrangeinput=='':
                    lowrange=2
            hirange=-1
            while hirange <2 or hirange>11:
                hirangeinput=input("Highest interval? (2 to 11, default 6): ")
                if hirangeinput.isdigit():
                    hirange=int(hirangeinput)
                if hirangeinput=='':
                    hirange=6
            if lowrange>hirange:
                low=lowrange
                high=highrange
                lowrange=high
                highrange=low

                
            index=1
    index=index+1
    if index>10000:
        print ("Trying 10.000 combinations")
        trycheck=1
        if clashes<=repeats:
            clashes=clashes+1
            print ("Clashes allowed:",clashes)
        if clashes>=13:
            clashes=13
        repeats=repeats+1
        print ("Repeated notes allowed:",repeats)
        if repeats>=13:
            repeats=13
            
        index=1
    init()


