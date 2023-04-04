"""Random Chords 1.3.0 - Generate random chords.
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
notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
clashes=0
repeats=0
firstchord=0
clashlist=["CC#","C#D","DD#","D#E","EF","FF#","F#G","GG#","G#A","AA#","A#B","BC"]
steps=[[0, 1, 3, 4, 6, 8, 10, 0], [0, 1, 3, 5, 6, 8, 10, 0], [0, 1, 3, 5, 7, 8, 10, 0], [0, 1, 3, 5, 7, 9, 10, 0], [0, 2, 3, 5, 6, 8, 10, 0], [0, 2, 3, 5, 7, 8, 10, 0], [0, 2, 3, 5, 7, 9, 10, 0], [0, 2, 3, 5, 7, 9, 11, 0], [0, 2, 4, 5, 7, 8, 10, 0], [0, 2, 4, 5, 7, 9, 10, 0], [0, 2, 4, 5, 7, 9, 11, 0], [0, 2, 4, 6, 7, 9, 10, 0], [0, 2, 4, 6, 7, 9, 11, 0], [0, 2, 4, 6, 8, 9, 11, 0]]

stepsitem=[]
index=1
lowrange=2
hirange=7
notesnumber=4
trycheck=0
maxrepeats=False
def init():
    global oktwo
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
    global repeatthree
    global chordsteps
    global scale
    global scales
    global stepstransposed
    oktwo=0
    okfive=0
    okeight=0
    oknine=0
    okten=0
    okeleven=0
    chordnotes=[]
    chord=[]
    chordsteps=[]
    counter=1
    octave=4
    chordstring=""
    clash=0
    repeat=0
    repeatthree=False
    notelist=[]
    occurrencies=[]
    clash_occ=[0,0,0,0,0,0,0,0,0,0,0,0]
    random.seed()
    scale=[]
    scales=[]
    stepstransposed=[]
    



def validate_chord():
    global clash
    global repeat
    global notelist
    global occurrencies
    global clash_occ
    global clashcount
    global repeatthree
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
            repeat=repeat+value
        if value>2:
            repeatthree=True

def guess_scale():
    global match
    global matchlist
    global scale
    global scales
    global stepstransposed
    global stepsitem
    match=0
    matchlist=[]
    chordlen=len(chord)
    stepslen=len(steps)
    for n in range (0, stepslen):
        for m in range (0,7):
            transpose=steps[n][m]+root
            if transpose>11:
                transpose=transpose-12
            stepsitem.append(transpose)
            transpose=0
        stepstransposed.append(stepsitem)
        stepsitem=[]
    #print (stepstransposed)
    for n in range (0, stepslen):
        for m in range (0,7):
            for o in range (0,chordlen):
                #print (chordsteps[o],steps[n][m])
                if chordsteps[o]==stepstransposed[n][m]:
                    match=match+1
                    
        matchlist.append(match)
        match=0


    for n in range (0,stepslen):
        if matchlist[n]==max(matchlist):
            #print (steps[n])
            #print (stepstransposed[n])
            for x in range (0,7):
                noteindex=stepstransposed[n][x]
                scalenote=notes[noteindex]
                scale.append(scalenote)
        if scale!=[]:
            scales.append(scale)
        scale=[]
    scalestring=''
    print ("Scales:")
    guess=1
    for item in scales:
        for note in item:
            scalestring=scalestring+note+" "
        print ("Match",str(guess)+": ",scalestring)
        guess=guess+1
        scalestring=''
    guess=0
    print ("\n")
        
    
    
init()

while True:

    root= randint(0,11)
    randomloop=randint(3,15)
    for n in range (1,randomloop):
        randreset=randint(2,11)
    lowest=randint(2,11)
    chord.append(notes[root])
    chordsteps.append(root)
    lowestvalue=root+lowest
    if lowestvalue>11:
        lowestvalue=lowestvalue-12
    chord.append(notes[lowestvalue])
    chordsteps.append(lowestvalue)
    notevalue=lowestvalue
    
    while counter<notesnumber-1:
        interval=randint(lowrange,hirange)
        if interval!=2 and interval<8:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>11:
                notevalue=notevalue-11
            chord.append(notes[notevalue])
            chordsteps.append(notevalue)
            counter=counter+1
        if interval==2 and oktwo==0:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>11:
                notevalue=notevalue-11
            chord.append(notes[notevalue])
            chordsteps.append(notevalue)
            counter=counter+1
        if interval==8 and okeight==0:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>11:
                notevalue=notevalue-11
            chord.append(notes[notevalue])
            chordsteps.append(notevalue)
            counter=counter+1
        if interval==9 and oknine==0:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>11:
                notevalue=notevalue-11
            chord.append(notes[notevalue])
            chordsteps.append(notevalue)
            counter=counter+1
        if interval==10 and okten==0:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>11:
                notevalue=notevalue-11
            chord.append(notes[notevalue])
            chordsteps.append(notevalue)
            counter=counter+1
        if interval==11 and okeleven==0:
            chordnotes.append(interval)
            notevalue=notevalue+interval
            if notevalue>11:
                notevalue=notevalue-11
            chord.append(notes[notevalue])
            chordsteps.append(notevalue)
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

    if clash<=clashes and repeat<=repeats and repeatthree==False:
        if firstchord==1:
            print ("\n")
            print (clashes, " clashes allowed")
            print (repeats, " repeated notes allowed")

            print ("root= ",notes[root])
            print ("lowest= ",notes[lowestvalue])
            print ("Intervals= ",chordnotes)
            for items in chord:
                chordstring=chordstring+items+" "
            print ("chord= ",chordstring)
            print ("\n")
            guess_scale()
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
                clashesinput=input("How many clashes allowed? (0 to 13, default 0): ")
                if clashesinput.isdigit():
                    clashesyes=int(clashesinput)
                    clashes=clashesyes
                    clashes_mem=clashes
                if clashesinput=='':
                    clashesyes=0
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
                inputnotesnumber=input("How many notes? (4 to 13, default 4): ")
                if inputnotesnumber.isdigit():
                    notesnumber=int(inputnotesnumber)
                if inputnotesnumber=='':
                    notesnumber=4
            lowrange=-1
            while lowrange <1 or lowrange>11:
                lowrangeinput=input("Lowest interval? (1 to 11, default 2): ")
                if lowrangeinput.isdigit():
                    lowrange=int(lowrangeinput)
                if lowrangeinput=='':
                    lowrange=2
            hirange=-1
            while hirange <3 or hirange>11:
                hirangeinput=input("Highest interval? (3 to 11, default 7): ")
                if hirangeinput.isdigit():
                    hirange=int(hirangeinput)
                if hirangeinput=='':
                    hirange=7
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
        if clashes==0:
            clashes=clashes+1
        if maxrepeats==True:
            clashes=clashes+1
            maxrepeats=False
        print ("Clashes allowed:",clashes)
        if clashes>=13:
            clashes=13
        repeats=repeats+1
        print ("Repeated notes allowed:",repeats)
        if repeats>=13:
            maxrepeats=True
            repeats=0
    
            
        index=1
    init()


