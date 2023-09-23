"""Random Chords 2.0.0 - Generate random chords.
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

import tkinter as tk
import tkinter.ttk as ttk
import random
from random import randint
import musicpy

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
prog=False
stepscale=[]
stepscales=[]
progyes=0
chord_play=[]
scales=[]

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
    global stepstransposed
    global chordn
    global scalecombo

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
    scalecombo=[]
    stepstransposed=[]
    progression=[]

    chordn=2

#Create app window
def create_app_window():
    global top
    global rootw
    img=b'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'
    rootw= tk.Tk()
    top= rootw
    top.geometry("470x505")
    top.resizable(0,0)
    top.title("Random Chords")
    favicon=tk.PhotoImage(data=img) 
    rootw.wm_iconphoto(True, favicon)

    """#Create menu
    global menubar
    global sub_menu
    menubar=tk.Menu(top, tearoff=0)
    top.configure(menu=menubar)
    #file menu
    sub_menu=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=sub_menu,compound="left", label="File")
    sub_menu.add_command(compound="left", label="Export chord", command=export_chord, accelerator="Alt+X")
    sub_menu.add_command(compound="left",label="Save chord", command=save_chord, accelerator="Alt+S")
    sub_menu.add_command(compound="left",label="Export history", command=export_history,accelerator="Alt+H")
    sub_menu.add_command(compound="left",label="Save history", command=save_history, accelerator="Alt+V")
    sub_menu.add_command(compound="left",label="Erase history", command=erase_history, accelerator="Alt+E")
    sub_menu.add_command(compound="left",label="Save Settings", command=save_settings, accelerator="Alt+T")
    sub_menu.add_command(compound="left",label="Default Settings", command=default_settings, accelerator="Alt+D")
    top.bind_all("<Alt-x>",export_chord_hotkey)
    top.bind_all("<Alt-s>",save_chord_hotkey)
    top.bind_all("<Alt-h>",export_history_hotkey)
    top.bind_all("<Alt-v>",save_history_hotkey)
    top.bind_all("<Alt-e>",erase_history_hotkey)
    top.bind_all("<Alt-t>",save_settings_hotkey)
    top.bind_all("<Alt-d>",default_settings_hotkey)
    #edit menu
    global edit_menu
    edit_menu=tk.Menu(top,tearoff=0)
    menubar.add_cascade(menu=edit_menu,compound="left", label="Edit")
    edit_menu.add_command(compound="left",label="Generate chord", command=generate_chord, accelerator="Alt+G")
    top.bind_all("<Alt-g>",generate_chord_hotkey)
    edit_menu.add_command(compound="left",label="Play chord", command=play_chord, accelerator="Alt+P")
    top.bind_all("<Alt-p>",play_chord_hotkey)
    edit_menu.add_command(compound="left",label="Play scale", command=play_scale, accelerator="Alt+L")
    top.bind_all("<Alt-l>",play_scale_hotkey)
    edit_menu.add_command(compound="left",label="Copy chord", command=copy_chord, accelerator="Alt+C")
    top.bind_all("<Alt-c>",copy_chord_hotkey)
    edit_menu.add_command(compound="left",label="Copy history", command=copy_history, accelerator="Alt+Y")
    top.bind_all("<Alt-y>",copy_chord_hotkey)
    menubar.bind_all("<Alt-f>",menubar.invoke(1))"""

    #Create settings entries
    #notes number
    global notes_number
    global notes_number_entry
    notes_number=4
    nn=tk.StringVar()
    nn.set(notes_number)
    notes_number_entry=tk.Entry(top, textvariable=nn,justify="right",font=("Arial",12))
    notes_number_entry.place(x=25,y=20,width=45,height=25)
    notes_number_label=tk.Label(top)
    notes_number_label.place(x=80,y=25,width=189,height=15)
    notes_number_label.configure(text="Number of notes (4-13)",anchor="w", justify="left",font=("Arial",12))
    #repeated notes
    global repeated_notes
    global repeated_notes_entry
    repeated_notes=0
    rn=tk.StringVar()
    rn.set(repeated_notes)
    repeated_notes_entry=tk.Entry(top, textvariable=rn,justify="right",font=("Arial",12))
    repeated_notes_entry.place(x=25,y=55,width=45,height=25)
    repeated_notes_label=tk.Label(top)
    repeated_notes_label.place(x=80,y=60,width=189,height=15)
    repeated_notes_label.configure(text="Repeated notes (0-13)",anchor="w", justify="left",font=("Arial",12))
    #clashes
    global clashes
    global clashes_entry
    clashes=0
    c=tk.StringVar()
    c.set(clashes)
    clashes_entry=tk.Entry(top, textvariable=c,justify="right",font=("Arial",12))
    clashes_entry.place(x=25,y=90,width=45,height=25)
    clashes_label=tk.Label(top)
    clashes_label.place(x=80,y=95,width=189,height=15)
    clashes_label.configure(text="Clashes (0-13)",anchor="w", justify="left",font=("Arial",12))
    #lowest interval
    global lowest_interval
    global lowest_interval_entry
    lowest_interval=2
    li=tk.StringVar()
    li.set(lowest_interval)
    lowest_interval_entry=tk.Entry(top, textvariable=li,justify="right",font=("Arial",12))
    lowest_interval_entry.place(x=25,y=125,width=45,height=25)
    lowest_interval_label=tk.Label(top)
    lowest_interval_label.place(x=80,y=130,width=189,height=15)
    lowest_interval_label.configure(text="Lowest interval (2-11)",anchor="w", justify="left",font=("Arial",12))
    #highest interval
    global highest_interval
    global highest_interval_entry
    highest_interval=7
    hi=tk.StringVar()
    hi.set(highest_interval)
    highest_interval_entry=tk.Entry(top, textvariable=hi,justify="right",font=("Arial",12))
    highest_interval_entry.place(x=25,y=160,width=45,height=25)
    highest_interval_label=tk.Label(top)
    highest_interval_label.place(x=80,y=165,width=189,height=20)
    highest_interval_label.configure(text="Highest interval (3-11)",anchor="w", justify="left",font=("Arial",12))
    #chord display
    global chord_display
    global chord_display_entry
    global chord_display_label
    chord_display=tk.Text(top)
    chord_display.place(x=25,y=195,height=25,width=420)
    chord_display.configure(state='disabled')    
    chord_display_label=tk.Label(top)
    chord_display_label.place(x=25,y=220,width=200)
    chord_display_label.configure(text="Chord",anchor="w", justify="left",font=("Arial",12))
    #scales display
    global scales_display
    scales_display=ttk.Combobox(top)
    scales_display.place(x=25,y=250,height=25,width=420)
    scales_display.configure(state="readonly",values=[" "])    
    scales_display_label=tk.Label(top)
    scales_display_label.place(x=25,y=275,width=200)
    scales_display_label.configure(text="Scale",anchor="w", justify="left",font=("Arial",12))
    #history display
    global history_display
    global history_display_entry
    history_display = tk.Text(top)
    history_display.place(x=25, y=310, height=160, width=405)
    scroll_1=tk.Scrollbar (top)
    scroll_1.place(x=440, y=310, height=160, anchor='n')
    history_display.configure(yscrollcommand=scroll_1.set)
    scroll_1.configure(command=history_display.yview)    
    #generate chord button
    global generate_chord_button
    generate_chord_button=tk.Button(top)
    generate_chord_button.place(x=310,y=20,height=40,width=140)
    generate_chord_button.configure(text="Generate chord",font=("Arial",12))
    generate_chord_button.bind("<Button-1>",generate_chord_hotkey)
    #play chord button
    global play_chord_button
    play_chord_button=tk.Button(top)
    play_chord_button.place(x=310,y=70,height=40,width=140)
    play_chord_button.configure(text="Play chord",font=("Arial",12))
    play_chord_button.bind("<Button-1>",play_chord_hotkey)
    #play scale button
    global play_scale_button
    play_scale_button=tk.Button(top)
    play_scale_button.place(x=310,y=120,height=40,width=140)
    play_scale_button.configure(text="Play scale",font=("Arial",12))
    play_scale_button.bind("<Button-1>",play_scale_hotkey)    
    

def export_chord():
    True

def export_chord_hotkey(event):
    export_chord()

def save_chord():
    True

def save_chord_hotkey(event):
    save_chord()

def export_history():
    True

def export_history_hotkey(event):
    export_history()

def save_history():
    True

def save_history_hotkey(event):
    save_history()

def erase_history():
    True

def erase_history_hotkey(event):
    erase_history()

def save_settings():
    True

def save_settings_hotkey(event):
    save_settings()

def default_settings():
    True

def default_settings_hotkey(event):
    default_settings()

def generate_chord():
    global clashes
    global repeats
    global notesnumber
    global lowrange
    global hirange
    global counter
    global oktwo
    global okeight
    global oknine
    global okten
    global okeleven
    global chordnotes
    global counter
    global chord
    global chordstring
    global chord_play
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
    global root
    global trycheck
    global chordok
    global firstchord
    global chordmem
    global progyes

    get_repeated_notes()
    repeats=repeated_notes
    get_notes_number()
    notesnumber=notes_number
    get_clashes()
    get_lowest_interval()
    lowrange=lowest_interval
    get_highest_interval()
    hirange=highest_interval
    #print ("generate chord",prog)
    chordok=False
    history_display.insert(tk.END,"\nPlease wait...\n")
    if prog==False:
        root= randint(0,11)
    while chordok==False:
        chord_play=[]
        scales=[]
        randomloop=randint(3,15)
        for n in range (1,randomloop):
            randreset=randint(2,11)
        lowest=randint(2,11)
        chord.append(notes[root])
        chordsteps.append(root)
        chord_play.append(notes[root]+'2')
        octave=4
        lowestvalue=root+lowest
        if lowestvalue>11:
            lowestvalue=lowestvalue-12
        chord.append(notes[lowestvalue])
        chordsteps.append(lowestvalue)
        chord_play.append(notes[lowestvalue]+str(octave))
        notevalue=lowestvalue

        while counter<notesnumber-1:
            interval=randint(lowrange,hirange)
            if interval!=2 and interval<8:
                chordnotes.append(interval)
                notevalue=notevalue+interval
                if notevalue>11:
                    notevalue=notevalue-11
                    octave=octave+1
                chord.append(notes[notevalue])
                chordsteps.append(notevalue)
                chord_play.append(notes[notevalue]+str(octave))
                counter=counter+1
            if interval==2 and oktwo==0:
                chordnotes.append(interval)
                notevalue=notevalue+interval
                if notevalue>11:
                    notevalue=notevalue-11
                    octave=octave+1
                chord.append(notes[notevalue])
                chordsteps.append(notevalue)
                chord_play.append(notes[notevalue]+str(octave))
                counter=counter+1
            if interval==8 and okeight==0:
                chordnotes.append(interval)
                notevalue=notevalue+interval
                if notevalue>11:
                    notevalue=notevalue-11
                    octave=octave+1
                chord.append(notes[notevalue])
                chordsteps.append(notevalue)
                chord_play.append(notes[notevalue]+str(octave))
                counter=counter+1
            if interval==9 and oknine==0:
                chordnotes.append(interval)
                notevalue=notevalue+interval
                if notevalue>11:
                    notevalue=notevalue-11
                    octave=octave+1
                chord.append(notes[notevalue])
                chordsteps.append(notevalue)
                chord_play.append(notes[notevalue]+str(octave))
                counter=counter+1
            if interval==10 and okten==0:
                chordnotes.append(interval)
                notevalue=notevalue+interval
                if notevalue>11:
                    notevalue=notevalue-11
                    octave=octave+1
                chord.append(notes[notevalue])
                chordsteps.append(notevalue)
                chord_play.append(notes[notevalue]+str(octave))
                counter=counter+1
            if interval==11 and okeleven==0:
                chordnotes.append(interval)
                notevalue=notevalue+interval
                if notevalue>11:
                    notevalue=notevalue-11
                    octave=octave+1
                chord.append(notes[notevalue])
                chordsteps.append(notevalue)
                chord_play.append(notes[notevalue]+str(octave))
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
        count()
        #print (clashes,repeats,repeatthree)
        #print (clash,repeat)
        if clash<=clashes and repeat<=repeats and repeatthree==False:
            #print ("\n")
            history_display.configure(state="normal")
            history_display.insert(tk.END,"\n")
            #print (clashes, " clashes allowed")
            history_display.insert(tk.END,str(clashes)+ " clashes allowed \n")
            #print (repeats, " repeated notes allowed")
            history_display.insert(tk.END,str(repeats)+ " repeated notes allowed")

            #print ("\n")
            history_display.insert(tk.END,"\n")

            for items in chord:
                chordstring=chordstring+items+" "
            #print ("chord: ",chordstring)
            history_display.insert(tk.END,chordstring)
            chord_display.configure(state="normal")
            chord_display.delete(1.0,tk.END)
            chord_display.insert(tk.END,chordstring)
            chord_display.configure(state="disabled")
            #print ("\n")
            history_display.insert(tk.END,"\n")
            name_chord()
            chord_display_label.configure(text="Chord: "+chordname_string)
            if prog==False:
                guess_scale()
            if trycheck==1:

                trycheck=0
            firstchord=1
            chordok=True
            history_display.configure(state='disabled')
        
        init()
    chordok=False
    chordmem=chord
            

def count():
    global clashes
    global repeats
    global index
    global maxrepeats
    #print (index)
    index=index+1
    rootw.delay=100
    history_display.configure(state='normal')
    if index>10000:
        #print ("Trying 10.000 combinations")
        history_display.insert(tk.END,"Trying 10.000 combinations\n")
        trycheck=1
        if clashes==0:
            clashes=clashes+1
        if maxrepeats==True:
            clashes=clashes+1
            maxrepeats=False
        #print ("Clashes allowed:",clashes)
        history_display.insert(tk.END,"Clashes allowed: "+ str(clashes)+'\n')
        if clashes>=13:
            clashes=13
        repeats=repeats+1
        #print ("Repeated notes allowed:",repeats)
        history_display.insert(tk.END,"Repeated notes allowed: "+str(repeats)+'\n')
        if repeats>=13:
            maxrepeats=True
            repeats=0
        index=1
        history_display.yview('end')
        history_display.configure(state='disabled')
        rootw.update_idletasks()

        


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
    global root
    global stepscale
    global stepscales
    match=0
    matchlist=[]
    stepscale=[]
    stepscales=[]
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
                stepscale.append(noteindex)
        if scale!=[]:
            scales.append(scale)
            stepscales.append(stepscale)
        scale=[]
        stepscale=[]
    scalestring=''
    #print ("Scales:")
    history_display.configure(state='normal')
    history_display.insert(tk.END,"Scales:\n")
    guess=1
    for item in scales:
        for note in item:
            scalestring=scalestring+note+" "
        #print ("Match",str(guess)+": ",scalestring)
        scalecombo.append(scalestring)
        history_display.insert(tk.END,"Match"+str(guess)+": "+str(scalestring)+"\n")
        guess=guess+1
        scalestring=''
    scales_display.configure(value=scalecombo)
    guess=0
    #print ("\n")
    #history_display.insert(tk.END,"\n")
    history_display.yview('end')
    history_display.configure(state="disabled")
    #print (scales)

def generate_chord_hotkey(event):
    generate_chord()

def play_chord():
    global chord_play
    #print (chord_play)
    if chord_play!=[]:
        c_one=musicpy.chord(notes=chord_play,interval=0, duration=2)
        musicpy.play(c_one,100)

def play_chord_hotkey(event):
    play_chord()

def play_scale():
    global scales_display
    global scales
    index=scales_display.current()
    octave=5
    c=musicpy.chord(scales[index],interval=0.3,duration=0.3)
    musicpy.play(c,100)    

def play_scale_hotkey(event):
    play_scale()

def copy_chord():
    True

def copy_chord_hotkey(event):
    copy_chord()

def copy_history():
    True

def copy_history_hotkey(event):
    copy_history()

def main():
    init()
    create_app_window()

def get_notes_number():
    global notes_number
    notes_number=notes_number_entry.get()
    if notes_number.isdigit()==True:
        notes_number=int(notes_number)
        #print (notes_number)
        if int(notes_number)<4:
            notes_number=4
        if int(notes_number)>13:
            notes_number=13
    else:
        notes_number=4

def get_repeated_notes():
    global repeated_notes
    repeated_notes=repeated_notes_entry.get()
    if repeated_notes.isdigit()==True:
        repeated_notes=int(repeated_notes)
        if int(repeated_notes)<0:
            repeated_notes=0
        if int(repeated_notes)>13:
            repeated_notes=13
    else:
        repeated_notes=0

def get_clashes():
    global clashes
    clashes=clashes_entry.get()
    if clashes.isdigit()==True:
        clashes=int(clashes)
        if int(clashes)<0:
            clashes=0
        if int(clashes)>13:
            clashes=13
    else:
        clashes=0

def get_lowest_interval():
    global lowest_interval
    global highest_interval
    lowest_interval=lowest_interval_entry.get()
    highest_interval=int(highest_interval_entry.get())
    if lowest_interval.isdigit()==True:
        lowest_interval=int(lowest_interval)
        if int(lowest_interval)<2:
            lowest_interval=2
        if int(lowest_interval)>11:
            lowest_interval=11
    else:
        lowest_interval=2
    if lowest_interval>highest_interval:
        lowest_interval=highest_interval
    lowest_interval_entry.delete(0,tk.END)
    lowest_interval_entry.insert(0,str(lowest_interval))

def get_highest_interval():
    global lowest_interval
    global highest_interval
    highest_interval=highest_interval_entry.get()
    lowest_interval=int(lowest_interval_entry.get())
    if highest_interval.isdigit()==True:
        highest_interval=int(highest_interval)
        if int(highest_interval)<3:
            highest_interval=3
        if int(highest_interval)>11:
            highest_interval=11
    else:
        highest_interval=7
    if highest_interval<lowest_interval:
        highest_interval=lowest_interval
    highest_interval_entry.delete(0,tk.END)
    highest_interval_entry.insert(0,str(highest_interval))

#Name Chord
def name_chord():
    global chordname_string
    chord_length=len(chord)
    chordname=[]
    chord_notes=[]
    chordname_string=''
    for n in range (0,12):
        if chord[0]==notes[n]:
            index=n
            for i in range (0,12):
                chord_notes.append(notes[index])
                index=index+1
                if index>11:
                    index=0
    #print (chord_notes)

    chordname.append(chord[0])

    sus=False
    sus_index=999
    ninth=False
    ninth_index=999
    seventh_maj=False
    seventh_maj_index=999
    seventh=False
    seventh_index=999
    sixth=False
    sixth_index=999
    eleventh=False
    eleventh_index=999
    ninth_maj=False
    ninth_maj_index=999
    thirteenth=False
    maj=False
    minr=False
    plusninth=False
    mincheck=False
    bfive=False
    fifth=False
    dim=False
    aug=False
    add_fifth=False
    minr_index=999
    for n in range (1,chord_length):
        step=chord_notes.index(chord[n])+1
        #print (step)
        if step==5:
            maj=True
            minr=False
        if step==4:
            minr=True
            maj=False
        if maj==True and minr==True and plusninth==False:
            plusninth=True
            minr=False
            chordname.append(" 9+")
            plusninth_index=len(chordname)
        elif minr==True and mincheck==False:
            chordname.append("m ")
            minr_index=len(chordname)
            mincheck=True
        if step==8:
            fifth=True

    for n in range (1,chord_length):
        step=chord_notes.index(chord[n])+1
        if step==6 and sus==False:
            sus=True
            chordname.append(" Sus")
            sus_index=len(chordname)
        if minr==True and step==7 and dim==False and fifth==False:
            dim=True
            chordname.append(" Dim")
            dim_index=len(chordname)
            if minr_index!=999:
                chordname[minr_index-1]='delete'
        if dim==False and step==7 and bfive==False:
            bfive=True
            chordname.append(" Add5b")
            bfive_index=len(chordname)
        if step==9 and fifth==False and aug==False:
            aug=True
            chordname.append(" Aug")
            aug_index=len(chordname)-1
        if step==9 and fifth==True and add_fifth==False:
            add_fifth_plus=True
            chordname.append(" Add5+")
            add_fifth_plus_index=len(chordname)
        if step==10:
            sixth=True
            chordname.append(" 6")
            sixth_index=len(chordname)
        if step==11:
            seventh=True
            chordname.append(" 7")
            seventh_index=len(chordname)
            #print (seventh_index)
        if step==12:
            seventh_maj=True
            chordname.append(" 7maj")
            seventh_maj_index=len(chordname)
        if step==3 and seventh==True:
            ninth=True
            chordname.append(" 9")
            ninth_index=len(chordname)
            if seventh_index!=999: 
                chordname[seventh_index-1]='delete'
        if step==3 and sus==False and seventh_maj==True:
            ninth_maj=True
            chordname.append(" 9maj")
            ninth_maj_index=len(chordname)
            if seventh_maj_index!=999:
                chordname[seventh_maj_index-1]='delete'
        if step==3 and seventh_maj==False and seventh==False:
            add_ninth=True
            chordname.append(" Add9")
            ninth_maj_index=len(chordname)
            if seventh_maj_index!=999:
                chordname[seventh_maj_index-1]='delete'        
        if step==2:
            ninthb=True
            chordname.append(" Add9b")
            ninthb_index=len(chordname)
        if ninth==True and sus==True and sixth==False and(seventh==True or seventh_maj==True):
            eleventh=True
            chordname.append(" 11")
            eleventh_index=len(chordname)
            #print (eleventh_index)
            chordname[ninth_index-1]='delete'
            chordname[sus_index-1]='delete'

        if ninth==True and sus==True and sixth==True and(seventh==True or seventh_maj==True):
            thirteenth=True
            chordname.append(" 13")
            thirteenth_index=len(chordname)
            if ninth_index!=999:
                chordname[ninth_index-1]='delete'
            if sixth_index!=999:
                chordname[sixth_index-1]='delete'
            if sus_index!=999:
                #print (sus_index)
                chordname[sus_index-1]='delete'
            if seventh_index!=999:
                #print (seventh_index)
                chordname[seventh_index-1]='delete'
            if eleventh_index!=999:
                chordname[eleventh_index-1]='delete'
            

    length=len(chordname)           
    for x in range(0,length):
        #print (x)
        if chordname[x]!='delete':
            chordname_string=chordname_string+chordname[x]

#CopyContextMenu
def create_context_menu():
    global menu
    menu = tk.Menu(rootw, tearoff = 0)
    menu.add_command(label="Copy", command=copy_text)
    rootw.bind("<Button-3>", context_menu)

def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()
        
def copy_text():
        history_display.event_generate(("<<Copy>>"))

main()
create_context_menu()
rootw.mainloop()
