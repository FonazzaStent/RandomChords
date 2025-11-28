"""Random Chords 2.1.5 - Generate random chords.
Copyright (C) 2023-2025  Maurizio Crescenzo

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
from shutil import copyfile
from os import remove
import os
from tkinter.filedialog import asksaveasfilename
from tkinter import *
from tkinter import messagebox
import webbrowser

notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
Dissonances=0
repeats=0
firstchord=0
clashlist=["CC#","C#D","DD#","D#E","EF","FF#","F#G","GG#","G#A","AA#","A#B","BC"]
steps=[[0, 2, 4, 5, 7, 9, 11, 0], [0, 2, 3, 5, 7, 9, 10, 0], [0, 1, 3, 5, 7, 8, 10, 0], [0, 2, 4, 6, 7, 9, 11, 0], [0, 2, 4, 5, 7, 9, 10, 0], [0, 2, 3, 5, 7, 8, 10, 0], [0, 1, 3, 5, 6, 8, 10, 0], [0, 2, 3, 5, 7, 9, 11, 0], [0, 1, 3, 5, 7, 9, 10, 0], [0, 2, 4, 6, 8, 9, 11, 0], [0, 2, 4, 6, 7, 9, 10, 0], [0, 2, 4, 5, 7, 8, 10, 0], [0, 2, 3, 5, 6, 8, 10, 0], [0, 1, 3, 4, 6, 8, 10, 0], [0, 2, 3, 5, 7, 8, 11, 0], [0, 2, 4, 6, 8, 10, 0], [0, 2, 3, 5, 6, 7, 8, 10, 0], [0, 2, 3, 5, 6, 8, 9, 11, 0], [0, 2, 3, 5, 6, 8, 9, 10, 0], [0, 1, 3, 4, 6, 7, 9, 10, 0], [0, 3, 5, 7, 10, 0], [0, 2, 4, 7, 9, 0], [0, 3, 5, 6, 7, 10, 0], [0, 2, 3, 4, 5, 7, 9, 10, 11, 0], [0, 2, 4, 5, 7, 8, 9, 11, 0], [0, 2, 3, 5, 7, 8, 10, 11, 0], [0, 2, 4, 5, 7, 9, 10, 11, 0]]
stepsnames=['Ionian', 'Dorian', 'Prhygian', 'Lydian', 'Mixolydian ', 'Aeolian ', 'Locrian', 'Melodic minor', 'Dorian b2', 'Lydian augmented', 'Lydian dominant ', 'Mixolydian b6 ', 'Aeolian b5 ', 'Altered scale', 'Minor Bebop', 'Whole Tone', 'Octatonic', 'Whole-Half Diminished', 'Whole-Half Diminished ', 'Half-Whole Diminished', 'Pentatonic minor ', 'Pentatonic major ', 'Blues scale ', 'Dorian Bebop ', 'Major Bebop', 'Harmonic Minor Bebop', 'Dominant Bebop']
stepsitem=[]
index=1
lowrange=2
hirange=7
notesnumber=5
trycheck=0
maxrepeats=False
prog=False
stepscale=[]
stepscales=[]
progyes=0
chord_play=[]
scales=[]
scalenames=[]

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
    rootw.protocol("WM_DELETE_WINDOW", QuitApp)

    #Create menu
    global menubar
    global sub_menu
    menubar=tk.Menu(top, tearoff=0)
    top.configure(menu=menubar)
    #file menu
    sub_menu=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=sub_menu,compound="left", label="File")
    sub_menu.add_command(compound="left",label="Save chord", command=save_chord, accelerator="Alt+C")
    sub_menu.add_command(compound="left",label="Save_scale", command=save_scale,accelerator="Alt+S")
    sub_menu.add_command(compound="left",label="Save history", command=save_history, accelerator="Alt+H")
    sub_menu.add_command(compound="left",label="Erase history", command=erase_history, accelerator="Alt+E")
    sub_menu.add_command(compound="left",label="Quit", command=QuitApp,accelerator="Alt+Q")

    top.bind_all("<Alt-c>",save_chord_hotkey)
    top.bind_all("<Alt-s>",save_scale_hotkey)
    top.bind_all("<Alt-h>",save_history_hotkey)
    top.bind_all("<Alt-e>",erase_history_hotkey)
    top.bind_all("<Alt-q>",QuitApp_hotkey)
    
    #edit menu
    global edit_menu
    edit_menu=tk.Menu(top,tearoff=0)
    menubar.add_cascade(menu=edit_menu,compound="left", label="Play")
    edit_menu.add_command(compound="left",label="Generate chord", command=generate_chord, accelerator="Alt+G")
    top.bind_all("<Alt-g>",generate_chord_hotkey)
    edit_menu.add_command(compound="left",label="Play chord", command=play_chord, accelerator="Alt+P")
    top.bind_all("<Alt-p>",play_chord_hotkey)
    edit_menu.add_command(compound="left",label="Play scale", command=play_scale, accelerator="Alt+L")
    top.bind_all("<Alt-l>",play_scale_hotkey)

    #About menu
    about=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=about,compound="left", label="?")
    about.add_command(compound="left", label="Help", command=helpbox, accelerator="Alt+H")
    about.add_command(compound="left", label="About", command=aboutbox)
    top.bind_all("<Alt-h>",helpbox_hotkey)
    


    #Create settings entries
    #notes number
    global notes_number
    global notes_number_entry
    notes_number=5
    nn=tk.StringVar()
    nn.set(notes_number)
    notes_number_entry=tk.Entry(top, textvariable=nn,justify="right",font=("Arial",12))
    notes_number_entry.place(x=25,y=20,width=45,height=25)
    notes_number_label=tk.Label(top)
    notes_number_label.place(x=80,y=25,width=189,height=15)
    notes_number_label.configure(text="Number of notes (4-12)",anchor="w", justify="left",font=("Arial",12))
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
    repeated_notes_label.configure(text="Repeated notes (0-12)",anchor="w", justify="left",font=("Arial",12))
    #Dissonances
    global Dissonances
    global Dissonances_entry
    Dissonances=0
    c=tk.StringVar()
    c.set(Dissonances)
    Dissonances_entry=tk.Entry(top, textvariable=c,justify="right",font=("Arial",12))
    Dissonances_entry.place(x=25,y=90,width=45,height=25)
    Dissonances_label=tk.Label(top)
    Dissonances_label.place(x=80,y=95,width=189,height=15)
    Dissonances_label.configure(text="Dissonances (0-12)",anchor="w", justify="left",font=("Arial",12))
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
    chord_display_label.place(x=25,y=220,width=350)
    chord_display_label.configure(text="Chord",anchor="w", justify="left",font=("Arial",12))
    #scales display
    global scales_display
    global scales_display_label
    scales_display=ttk.Combobox(top)
    scales_display.place(x=25,y=250,height=25,width=420)
    scales_display.configure(state="readonly",values=[" "])
    scales_display.bind("<<ComboboxSelected>>", scales_caption_display)
    scales_display_label=tk.Label(top)
    scales_display_label.place(x=25,y=275,width=420)
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
    

def save_chord():
    global midifilename
    if os.path.exists("chord.mid")==False:
        play_chord()
    if os.path.exists("chord.mid"):
        data=[('MIDI','*.mid')]
        midifilename=asksaveasfilename(filetypes=data, defaultextension=data)
        if midifilename!='':
            copyfile('chord.mid',midifilename)
            remove ('chord.mid')

def save_chord_hotkey(event):
    save_chord()

def save_scale():
    global midifilename
    if os.path.exists("scale.mid")==False:
        play_scale()
    if os.path.exists("scale.mid"):
        data=[('MIDI','*.mid')]
        midifilename=asksaveasfilename(filetypes=data, defaultextension=data)
        if midifilename!='':
            copyfile('scale.mid',midifilename)
            remove('scale.mid')

def save_scale_hotkey(event):
    True

def save_history():
    history_display.configure(state="normal")
    history_text=history_display.get("1.0", tk.END)
    if history_text!='':
        data=[('TXT','*.txt')]
        historyfilename=asksaveasfilename(filetypes=data, defaultextension=data)
        if historyfilename!='':
            historyfile=open(historyfilename,'w')
            historyfile.write(history_text)
            historyfile.close()
    history_display.configure(state='disabled')

def save_history_hotkey(event):
    save_history()

def erase_history():
    history_display.configure(state="normal")
    history_display.delete("1.0", tk.END)

def erase_history_hotkey(event):
    erase_history()

def generate_chord():
    global Dissonances
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
    global scalenames
    
    scalenames=[]
    get_repeated_notes()
    repeats=repeated_notes
    get_notes_number()
    notesnumber=notes_number
    get_Dissonances()
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
        #print (Dissonances,repeats,repeatthree)
        #print (clash,repeat)
        if clash<=Dissonances and repeat<=repeats and repeatthree==False:
            #print ("\n")
            history_display.configure(state="normal")
            history_display.insert(tk.END,"\n")
            #print (Dissonances, " Dissonances allowed")
            history_display.insert(tk.END,str(Dissonances)+ " Dissonances allowed \n")
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
    global Dissonances
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
        if Dissonances==0:
            Dissonances=Dissonances+1
        if maxrepeats==True:
            Dissonances=Dissonances+1
            maxrepeats=False
        #print ("Dissonances allowed:",Dissonances)
        history_display.insert(tk.END,"Dissonances allowed: "+ str(Dissonances)+'\n')
        if Dissonances>=12:
            Dissonances=12
        repeats=repeats+1
        #print ("Repeated notes allowed:",repeats)
        history_display.insert(tk.END,"Repeated notes allowed: "+str(repeats)+'\n')
        if repeats>=12:
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
    global scalenames
    match=0
    matchlist=[]
    stepscale=[]
    stepscales=[]
    chordlen=len(chord)
    stepslen=len(steps)
    for n in range (0, stepslen):
        scalelen=len(steps[n])
        for m in range (0,scalelen):
            transpose=steps[n][m]+root
            if transpose>11:
                transpose=transpose-12
            stepsitem.append(transpose)
            transpose=0
        stepstransposed.append(stepsitem)
        stepsitem=[]
    #print (stepstransposed)
    for n in range (0, stepslen):
        scalelen=len(steps[n])
        for m in range (0,scalelen):
            for o in range (0,chordlen):
                #print (chordsteps[o],steps[n][m])
                if chordsteps[o]==stepstransposed[n][m]:
                    match=match+1
                    
        matchlist.append(match)
        match=0


    for n in range (0,stepslen):
        scalelen=len(steps[n])
        if matchlist[n]==max(matchlist):
            #print (steps[n])
            #print (stepstransposed[n])
            for x in range (0,scalelen):
                noteindex=stepstransposed[n][x]
                scalenote=notes[noteindex]
                scale.append(scalenote)
                stepscale.append(noteindex)
            scalenames.append(stepsnames[n])
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
    i=0
    for item in scales:
        for note in item:
            scalestring=scalestring+note+" "
        #print ("Match",str(guess)+": ",scalestring)
        scalecombo.append(scalestring)
        history_display.insert(tk.END,"Match"+str(guess)+": "+str(scalestring)+scalenames[i]+"\n")
        guess=guess+1
        i=i+1
        scalestring=''
    scales_display.configure(value=scalecombo)
    scales_display.current(0)
    scales_display_label.configure(text=scalenames[0])
    guess=0
    i=0
    #print ("\n")
    #history_display.insert(tk.END,"\n")
    history_display.yview('end')
    history_display.configure(state="disabled")
    #print (scales)

def scales_caption_display (event):
    
    scales_index = scales_display.current()
    scales_display_label.configure(text=scalenames[scales_index])

def generate_chord_hotkey(event):
    generate_chord()

def play_chord():
    global chord_play
    #print (chord_play)
    if chord_play!=[]:
        c_one=musicpy.chord(notes=chord_play,interval=0, duration=2)
        musicpy.play(c_one,100)
        copyfile("temp.mid","chord.mid")
        remove("temp.mid")

def play_chord_hotkey(event):
    play_chord()

def play_scale():
    global scales_display
    global scales
    if scales!=[]:
        index=scales_display.current()
        octave=5
        c=musicpy.chord(scales[index],interval=0.3,duration=0.3)
        musicpy.play(c,100)
        copyfile("temp.mid","scale.mid")
        remove ("temp.mid")

def play_scale_hotkey(event):
    play_scale()

def QuitApp():
    okcancel= messagebox.askokcancel("Quit?","Do you want to quit the app?",default="ok")
    if okcancel== True:
        top.destroy()

def QuitApp_hotkey(event):
    QuitApp()

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
        if int(notes_number)>12:
            notes_number=12
    else:
        notes_number=5

def get_repeated_notes():
    global repeated_notes
    repeated_notes=repeated_notes_entry.get()
    if repeated_notes.isdigit()==True:
        repeated_notes=int(repeated_notes)
        if int(repeated_notes)<0:
            repeated_notes=0
        if int(repeated_notes)>12:
            repeated_notes=12
    else:
        repeated_notes=0

def get_Dissonances():
    global Dissonances
    Dissonances=Dissonances_entry.get()
    if Dissonances.isdigit()==True:
        Dissonances=int(Dissonances)
        if int(Dissonances)<0:
            Dissonances=0
        if int(Dissonances)>12:
            Dissonances=12
    else:
        Dissonances=0

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

    seventh=False
    seventh_maj=False

    ninthb=False
    ninth=False
    ninth_plus=False
    
    eleventh=False
    eleventh_plus=False

    thirteenthb=False
    thirteenth=False

    maj=False
    minr=False
    mincheck=False
    fifth=False

    for n in range (1,chord_length):
        step=chord_notes.index(chord[n])+1
        if step==5:
            maj=True
            minr=False
            #print ("maj")
           
        if step==8:
            fifth=True

    for n in range (1,chord_length):
        step=chord_notes.index(chord[n])+1
        if step==4 and maj==False:
            chordname.append("m ")
            minr=True

    for n in range (1,chord_length):
        step=chord_notes.index(chord[n])+1

        if step==4 and maj==True and ninth_plus==False:
            chordname.append(" #9")
            ninth_plus=True
        
        if step==6 and eleventh==False:
            chordname.append(" 11")
            eleventh=True

        if step==7 and eleventh_plus==False:
            chordname.append(" #11")
            eleventh_plus=True

        if step==9 and thirteenthb==False:
            chordname.append(" b13")
            thirteenthb=True
                
        if step==10 and thirteenth==False:
            chordname.append(" 13")
            thirteenth=True

        if step==11 and seventh==False:
            chordname.append(" b7")
            seventh=True
            
        if step==12 and seventh_maj==False:
            chordname.append(" 7")
            seventh_maj=True
            
        if step==3 and ninth==False:
            chordname.append(" 9")
            ninth=True
            
        if step==2 and ninthb==False:
            chordname.append(" b9")
            ninthb=True
                        

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
        x,y = rootw.winfo_pointerxy()
        widget = rootw.winfo_containing(x,y)

        if widget.winfo_name()=='!text2':

            history_display.event_generate(("<<Copy>>"))
        else:
            chord_display.event_generate(("<<Copy>>"))

#About
def aboutbox():
    global aboutbox
    #print ('about')
    aboutbox=tk.Toplevel(top)
    aboutbox.geometry("500x240")
    aboutbox.resizable(0,0)
    aboutbox.title("About")
    about_label=Label(aboutbox)
    logo=b'iVBORw0KGgoAAAANSUhEUgAAAaQAAABaCAYAAAD3oyLoAAAmTElEQVR4nO2dd3RVxfbHv7ff3PROCkFISAESIglgeCAdHqigiEoRiFRBQH9IL5FiQ3Gh1LfyaFLUIE8CKB2SiJEuRIQQeISSEFJIbzf3nnPm9we/c34pN8k5yb0hkvmsdZaLeGbPvnNmZk/Zs0cGgIBCoVAolKeM/GkrQKFQKBQKQA0ShUKhUJoJ1CBRKBQKpVlADRKFQqFQmgXUIFEoFAqlWUANEoVCoVCaBdQgUSgUCqVZoKz+B7mc2igKhUKhWBZCCAipegy2ikFq3749tm7dChsbG3Ac16TKUSgUCqVloFKpsHHjRkRHR1f5exWDZGVlheeffx42NjZNqhyFQqFQWhaenp41/lbFIBFCYDAYwDBMjRmSTCazrHYUCoVCeeaoviwHAGq1GizL1vh7jT2k6sjlciiVSpOJKRQKhUKpDZlMBrlcDqPRaNIwVadOgySXy1FcXIxVq1bh2rVrZlOSQqFQKM82hBDI5XIMHjwYM2fOhFwur9co1WmQlEolfvrpJ6xdu9asilIoFAqlZXDq1ClEREQgIiICRqOxznfr9fHOzs42m2IUCoVCaVlwHIeCggJRfgii9pB42rZti8jISFFTLwqFQqG0PORyOUpKSrBx40YUFxcDEO8UV69Bqkzbtm0RFRUlXUMKhUKhtBgKCgqwc+dOwSCJRZJBYlkW5eXlUCqVdIZEoVAolBooFAqUlZU1yEbQOEEUCoVCaRZQg0ShUCiUZgE1SBQKhUJpFlCDRKFQKJRmgSSnBksjk8mEpzJ8mHLqSEGhUCjPLk/NICkUCigUiip/MxqNKCsrQ0VFhRA7T6FQQKlUwsrKClqttoYcU4FgKc0LtVot+l2xMa+edVQqleizG3W1gad9vxkdSFKk0KQGiQ/UCgCZmZlISUlBcnIyrl+/jvv37+Px48coLS2FXq8XDJJSqYRSqYROp4OdnR08PDzg5+cHPz8/tG/fHu3atYOzszNkMhkIIWAYhjaAZoJMJoPBYMC6detw//79OjtHQgisra3x4YcfwsHBoUUPMpRKJXbv3o3z58/XGLRVhxCCadOmISgoCAzDVPl/HMdBr9c/tUj9hBCh/VIoYmiSmsIbory8PJw4cQKxsbE4e/Ys0tLSGtXxaLVaeHl5oXPnzhg4cCBefPFFBAQEQKFQ0JlTM0Amk4FhGOzcuVNUcF4bGxtMnToVTk5OLfrbyeVyHDlyBN9//72o9wcPHoyOHTtW+ZtKpUJiYiImT578VA3SO++8g/nz59cbw4xCAZrAIKnVapSWlmLr1q3YsGED/vrrL7PJ1uv1uHPnDu7cuYOffvoJ9vb26Nu3L0aPHo0hQ4bA1taWGqZmgNglO41GQ+/d+j9UKpXod03NPGUyGUpLS5GSkmJOtSSTmZlJvylFNBZdYFar1UhJScGIESPw7rvvmtUYmaKwsBCxsbF46623MGDAAOzatQssy9a77EGhPIs0B0NA2x5FChYzSGq1GteuXcOwYcNw/PhxS2VTKxcuXMD48eMxfPhwpKen04ZBoVAozRyLGCS5XI7c3FxMmjQJt27dskQWolGpVLC1taWODhQKhdLMsYhBUiqViI6OxsWLFy0hXjRDhgzBzp07W7zXFoVCofwdMLtTg1wuF0KPS8He3h4dOnSAt7c3bG1toVKpYDAYUFZWhsePHyMjIwMPHjxAaWmpKHl9+/bFjh074ODgQD18KJSnBH98g0IRg9kNkkKhwI0bN3D37l1R78vlcsycOROzZs2Ch4cHrK2ta7yj1+sFw5SUlITffvsNJ06cQHJyskmZL7zwAnbu3Ak3NzcYDIZG/Z7mjqkDxjyEELAsK2l2WJc84MnZFpZlm3QJVCaTQaFQ1HvIk2VZi3WAfP5iHQU4jhOevwMKhQJt2rSBRqMx27dlWRYeHh6S0/Hf21TUFlMQQoSyflpL87W1G3PXycpnOU0hNb/65DV1eze7QZLJZMjIyEBFRYWo94ODg7F69WpotVowDFPjpD5fOe3t7eHo6Ah/f3+88cYbKCgoQEJCArZs2YIjR44IH6Fz587YvXs3vL29YTAYIJPJJLnQAtKjBUg5VQ/8/8l6qbpVNq58no8fP8bt27dx8+ZNZGdno6KiAjqdDh4eHujQoQN8fX1hZ2dXb0XlXbOzs7ORmpqKlJQUZGdnC/dfOTs7w9/fH/7+/vD09BQOvVoSvpEbjUakp6fj3r17uHv3LnJyclBeXg7gydklDw8P+Pv7w8fHBy4uLgDME/Gh8nfNy8tDbm4uHj58iPT0dOTl5aGkpARGoxFyuRxqtRp2dnZwdXWFj48P3N3d4eLiIgywLGkszYGdnR327duHgIAAs60oEEKElY76qNwxGgwGZGZmIjs7G/fv30d2djYKCgqECC585BYnJyd4eHigdevWcHFxgYuLi3CbtZQD8mLbIcdxVQ4fV06XlZWF9PR0ZGRkoLS0FEqlEnZ2dujUqRNcXV0FXRoatYRvC4WFhbhz5w6Sk5Px6NEjlJWVQaPRwM3NDYGBgfD394ezs3MNXavD1+38/HzcvXsXKSkpyMjIQFlZGWQyGRwdHdGuXTsEBgaidevWUKlUTRJFxSLnkKR0VI8fP8bNmzcRGhpaxVLzox3+v9UbtI2NDYYPH46XXnoJv/zyCxYsWACWZfHdd9/B19cXBoMBcrkceXl5iIqKQmFhoSh9HB0dsWrVKjg4OIjqQFQqFU6ePIlt27aJ/s2LFy9Gx44dkZ+fjxUrViAnJ6feNJ06dcKCBQuERp6SkoItW7bg559/xq1bt0yOxNVqNUJCQvDWW29hwoQJcHV1rfFt+Ip+7tw57NixA6dPn8adO3dMypPJZPD09ETfvn0xZcoU9OrVSxhBmRO+g09PT8fBgwdx8OBBXLlyBTk5ObU2CKVSCV9fX/Ts2ROjRo3Ciy++CLVaLdlo8p0MIQS3bt1CQkICTp8+jRs3biA1NVXUxWNyuRxOTk4ICAhAaGgoBg4ciIiICLi5udXbUTwtZDIZdDoddDqdWfWrL3QQX/+Kiopw6dIlnDx5EhcuXEBKSgoyMzNF6aLRaODj44OAgAD07t0b/fr1Q6dOnaBWq+vtRBUKBbKysrBgwYJ685o4cSL69+8PhmGgVCrBcRyOHz+OXbt2ITExEQ8ePKjRFqKiorBixQrByEdFReH27dv1/qZWrVrho48+go2NDZRKJTIyMrBjxw785z//wbVr10wOGuRyOQIDA/Hqq69i0qRJaNeuXY36zxv+5ORk7Ny5E4cPH0ZycnKtgxBnZ2f84x//wMSJEzF06FAolUqL11/CP8HBwSQ3N5cYjUZSUVFBCCHk888/F/5/7969SVlZGTEYDKSiosLkQwghsbGxpLLc+h5PT08yceJEsnHjRnL06FFy8eJFcuvWLZKVlUX0ej3hOI6YgmVZwjAMIYSQe/fukeTkZEIIqaIPwzDk/fffl6TP1q1ba8gx9RgMBmIwGMjAgQNFy+7evTspKCggHMeR9PR04uHhISpdr169CMdxhGVZsmnTJuLm5ibpNwUHB5NTp05V+V2EEJKVlUVmzJhBdDqdJHlarZbMnj2bFBYWEpZlTZaP0WgkBQUFJCwsTJRMZ2dnkp6eTkpKSsjnn39OfHx8JOnEPwqFggwdOpScO3eOEELqrK+VH47jCMMw5OTJk+TNN98kTk5ODcrf1OPn50cWLlxIbt26RQghQhurrQ2NHz9etOzDhw/XqK+EEHLs2DHRMpycnMiNGzcIx3Giyqqxj8FgIIQQ8ujRI7JmzRrSuXNnIpPJzFLWVlZWZMCAAeSHH34gpaWldbZljuNISkqKKLnr168X+p579+6R0aNHE4VCUWeaJUuWCHXQaDSKbgs+Pj4kOzubEELI/v37iZ+fn6Qy8Pb2Jrt3765S/1mWJSUlJWTlypXE2dlZkjyZTEbefPNNkpaWVm/fyDAMefjwYZW+rXodJYSQZcuWmcrr//9hDoPEcRy5dOmS5A6ueoVydXUl7dq1IyEhIaRfv35kzJgxZM6cOeSLL74ge/bsIXFxcSQ5OZkUFhYKRslU58MwDMnMzCQBAQGi8+/atSspLi6us9Pgy+fXX38lGo1GlFylUkmOHDlCCCHCR2vbtq2otAMGDCCEEPLRRx81uFwdHR3JwYMHhbK6efMm6d69e4PlASDDhw8nBQUFhGGYRhskNzc3cvLkSdK/f/9G6cQ/dnZ2ZMOGDYRl2XqNEl8eo0aNIiqVyiz5m3pcXV3JJ598QoqKimrt/J+GQXJ2diZ37941OfBrDLV1WAzDkB07dpD27dtbrKwBkD59+pBff/3VZN/A91e3bt0S1YY3b95MCCHkr7/+Ip06dRKV/9KlS4W8jUYj6dGjh6h0/v7+pKioiHz77bdEq9U26LcrlUqybt06QsiTwXtOTg559dVXG1WeYWFh5O7du7UOQhtrkMy+ZMeyLPz9/eHr6ysqfpkpysvLUV5eXudSFr9G6+zsjODgYERERKBPnz4IDg6GRqMRpuosy8Ld3R1Lly7F+PHjRa2BXrp0CUePHsXIkSPrXPIhhGDr1q2i98tefvll9O/fX9h3kIJGo8H333+PlStXSkpXmfz8fEybNg0BAQGwt7fHmDFj8McffzRYHgAcOHAAy5Ytw9dffy0EuG0oRUVFGDduHB49etQonSrLmzVrFoqLi4UlGVP6qdVqxMbGYvbs2UhLSzNL3rWRk5ODJUuWID4+HtHR0XjuueeaheNNeXk5tmzZAnd3d7MtwXp6emLYsGFQKBRCuSuVShQXF2Pu3LnYsmWLWfKpi/j4eAwdOhQff/wxZs2a1agNeqVSiYKCAkycONHiUWc0Gg3OnDmD999/H3q9vkEyGIbBggULhKXMyZMn48CBA43S6/Lly5gxYwb27dsHtVptEacdwTqZY4ZkKl1TPTqdjgwcOJDs27ePGI1GwYobDAai1+vJkCFDRMvq168f0ev1tc6SWJYl169fJ46OjqJ1+/3334VRgtQZUmhoqNlGkyNHjiRjxowxW7mr1eoay4ENmSFZ6lEqlWTv3r0mR+yEEPLDDz8QGxubJtfr+eefJ3fv3q0xUyKk6WdIlnjCw8NJaWmp0IaMRiMpLCwkr7322lPR5+OPPyYcx1Xpv6TMkLZv306WLl0qKc+GzpB8fX3N1m66detGPvzwQ7OWZXR0dJ0z4IbOkCxyMJZlWUyaNAldunSxhPhaKSsrw4kTJzBy5EhMmDAB2dnZUCqVIIRAo9Fg+fLlsLW1FSXr119/RXx8fK0ukXK5HLt27UJ+fr4oeaNHj8YLL7zQ4NFwUlKSqM1QMezbtw/fffedWWQBT5xYNm/eDJZlzR4/zcrKCh4eHvDx8YGnpyesrKwky2AYBosWLUJGRkYV11yVSoULFy5gxowZKCkpkSzXwcEBHh4ecHd3h06nk5z+ypUrmDp1KkpLS5/6vUWWoPq3ksvlWLZsGfbv3y9ZlkqlgqurKzw8PODs7NwgfZYvX46YmBjJXrfAE6eP69evN8msDgBSU1Nx+fJls8i6cOECvvrqK7PI4tm0aROKi4vNXm8tZpBcXFywZcsW+Pr6WiKLevnuu+8wZswY5OfnQ6FQwGAwoFu3bpg2bZqo9AzDCJ1sdRQKBR49eoQ9e/aIkuXk5IT/+Z//kaR/dUwtM9jY2EhyI60PrVZr8hyYGOLi4nDv3j2zxQzs1asXNm3ahPj4eJw7dw4XL17EuXPnkJCQgK+//hqdO3eWJO/OnTvYs2ePoJ9cLkdFRQWWLFmCvLw80XKsra0RGRmJ/fv348yZMzh79izOnj0rLMG9+OKLkvQ6ceIEtm3b9szfGaRWq3H69Gls3rxZUrqOHTti9erVOH36NH7//XecP38ev/32G44fP465c+fCzc1NtCyGYbB48eIaAxMxyOVyHDhwAFlZWZLSNRRT7d3a2rpBA7LaUKlUsLGxaVDaa9eu4dKlSxapt8J0yVxLdtU3il9++eWnMkUHQObNmycsiTAMQzIyMoivr6+otFZWViQxMdHkksq6desk6VB9eit1yY5/bGxsyAcffEDi4uJIUlISuXjxItm2bVujpvc9e/Yke/bsIZcvXyZXr14lhw4dIiNHjpTs9VR9WawhS3bW1tZk/fr1pLy8XNgYZxiGGI3GKs4r+fn5ZMaMGZL0CwsLE+ovIYQcPnyYyOVy0en9/PxIfHy8oAPvlceyrPA3vV5P1qxZI9rRBQAJDAwkubm5gmPIs7Jk16tXL2HJjmEY8sorr0hKP336dJKbmyuULe9VW7m8k5OTSZ8+fSTJ/fLLL4XykrJk15Bn0aJFDVqy4x+lUknefvttcvjwYXL16lXyxx9/kB9//JEMHjy4wTp16NCBbN68mVy4cIEkJSWRkydPknfffVey88TKlStNLts1Ky87U14s5eXlJCYmhgwcOLBR3ncNeZydncmdO3eE/SRCCNm+fbvoznbcuHFVDBK/Dh4aGioqvZeXF7l3714NL7SGGCSdTid0+nyHyPP48WMyYMAAyeXz5ptvkqKiohoyOY6TvF7+0UcfNcogyeVy8s033xBC6naL5vfw9Hq9pE7O1taWJCUlEY7jCMdxZNq0aaLT2tnZkd9++81kA6y+b0YIIVFRUZLKrnKDfdYMEu9aLXa/FQB5/fXXq+wD1zXoffDggaT91R49ehC9Xk8MBkOjDZJMJiMdO3Ykb7zxBpk9ezZZtGgR+fDDD8nkyZPJ4MGDyaZNm4R9K6kGSSaTkdWrV5ts73q9nkyePFmyvj169CDp6ekmZW7btk1SOYwYMeLvZ5B4o8Qrk5SURL755hsyduxYEh4eTlxcXBrs1ij22bFjh5A/7+AwaNAgUWkrd2J8mezdu1d03p999lmdH02KQZoyZYow2jLVMM+fPy/J4Ht6epLU1NRa9SstLSVdu3YVLS8yMrJRBik4OJgUFRXVa4wq/+ZTp07Vexak8hMbG0sIIaS8vJw8//zzkn+bmLrPsizJzMwkrVu3Fi0/KirqmTNI//jHP4RzQPv37xedzsrKipw9e7Ze41/5t65du1a0fDc3N/Lf//6XsCzbKIM0dOhQcvz4cZKXl0dMYTAYSGlpqdDvSDVIffr0EdqRqT41PT1dUh3TarWCC3x1efyqwahRo0TLe+GFF4S05jJITXJjbFpaGgwGA3x9fRESEoKQkBAQQlBaWoqioiKkpaXh4cOHePToER49eoSHDx8KT15eHsrKylBaWtpgd9TKLpqkkoPD77//Xu9mdnFxMaKjo7FhwwZh3+Hf//63qHwDAgIwadIks7jRKpVKvPHGG8JvqA7DMAgJCUHnzp1x9uxZUTIHDRqEtm3bmnS0YFkWOp0OI0aMEB21vaCgoFFuoF26dIGNjY3ok+Acx6F9+/Zwd3dHRkaGaB2BJy7hYiJk8PTu3RuA6bKvDr+HGhYWJtqN/MGDB6J1sQQymQxardZsm9SEkCqOHvfv3xed1sfHBx06dJAUESAiIgIajUbUEQw+DJSvr2+DXcDfe+89fPXVV9BoNGBZ1mREiMpRPxrCyJEja402YjQa4eXlhb59+4oOZB0WFoZu3bqZLFdex1GjRiEmJkaUzmVlZdDr9dDpdGYLKWRRg6RWq/HXX39h/PjxKCgowObNmzF48GAh3IxWq4WVlRU8PT2rpCOEwGg0gmEYFBUVISsrC9nZ2Xj48CFu3ryJn3/+GdevXxetR25ubpV/GwwGREREYNKkSfjmm2/qTR8TE4PZs2fD398fiYmJiI+PF5XvnDlzTIbraQhOTk5o165drR0+b2iDgoJEG6TQ0NB635HiKdnY39kQ76f6gkNWh284BoNB0kDB3t5ekl4ymUxSGr7sntYtr3Z2dti+fTuee+45s4SGIYTA1tZWcB6QcpbGysoKVlZWojs5QgisrKxEGySGYRr1G7t27YpPP/203jh9jemkZTKZKMedoKAg0TJDQ0Oh0Whq1ZkQIsS+FBNqrbHlaAqLGCR+ZJCQkIDIyEjcu3cPAPDaa6/hvffew5w5c+Dh4SHEp6veMfBRfnlXT3d39yoNdc6cORg0aBCSkpJE61MdjuMwd+5cHDhwQNCvNh4/fozt27fj008/RXR0tKjgk+Hh4Rg1apTZPphOp4OtrW2dBkkmk8HBwUG0TFdX13rfsbe3F33gtbGjpLt370oqL7lcjpycHGRnZ4tOw7v9W1tbS/JQlDqDYVlW0iFbXi9zjTSlolAoEBwcDD8/P7PJrBy3T0q9zM/PR15eHlxcXEQNGvggw2KvptFqtdBqtaL1qZ7X1KlTYWdnZ9EDzVqtVtTFolLKlQ88XBscx8HW1hY6nU507E9zY3a3b96QxMTE4LXXXqvS2ZeXl2PNmjXo2bMn1q5di8zMTKjVaqjVaiHcPAAhICP5v0gLRqMRBoMBRqMRHMfBzc1NVGfKY+rcAsMw8Pb2xuLFi0XJ2Lt3L+Li4nD48OF635XJZJg/fz7s7OzMdpJZoVCImglImS2ImZHI5fImu/794sWLuHHjhqSZ0sGDB0WPvrVaLby9vQE8cZn38fERnc+hQ4dER9hQqVRITk7GpUuXRMtv37696HctBb/sZDAYzPJUHlz4+fmJnv2lp6fjzJkzouodL/PAgQOiZ7xubm4NjkhhZ2eH3r17W/xakfqugeGR0t7FDMDEXPNiScyaM798snbtWkyYMKHWQ6OpqamYM2cOIiIiMHPmTBw7dgy5ubmQyWSCgTL1KJVKFBYW4ssvv8SZM2dE6xUSEmLy7wzDYOzYsejbt2+9Mu7fv4+pU6cKexB10a9fP7zyyivNMqpzc6aoqAiLFy9GYWEh1Gp1rR0YHw387Nmz2LBhg2j53t7e8Pf3B8uyUKlU6NOnj+i0cXFx+Ne//gWlUllrJ8DX35KSEixbtgxFRUWiZKtUKvTq1eupzY4sDcuyCAoKQuvWrUW/v3z5cty/f7/OeqBQKKBSqXD06FHs2LFDtD6hoaHCCo1UPD090apVq7/NPVd/N8y2ZMcfPl24cKHoU8FpaWnYuHEjNm/eDC8vL4SGhgr32tjb2wsbhqWlpcjOzsbt27dx9uxZSRELXF1d0bNnT5MViOM46HQ6LF++HOfOnRPu2DEFy7K4c+dOvfmp1WosXLgQWq22WcQo+7tx+PBhvP766/jkk0/QpUsXk6M6vV6Pn376CfPnz5fkmDBo0CA4OjoK92SNGDECa9euFRWlgeM4zJs3D7m5uZg+fTrc3d1rvEMIQVJSEpYsWYJffvlFtF69evVCSEjIMzuAYVkWnp6eGD58ONavXy8qzfXr1/Hqq6/iyy+/FK4SqU5xcTFiYmKwZMkS0cYfAN5+++0GzwIcHR2F6C8U82MWgySXy1FUVIRp06bhxx9/lJye4zikpaVZJLDl2LFj6wxgaTAY8OKLL+Kdd97Bpk2bGp3f8OHD0bdvX3pteiM4deoUEhMT0bt3b3Tv3h1t27aFTqdDWVkZbt++jYSEBCQmJkqSqdPpMGHCBKEj4b0SIyMjRc+yKioqsGLFCuzatQv9+/dHaGgonJ2dwTAM0tPTcf78eZw8eRLFxcWi9VKpVJg3b94zP4DhOA4zZ87E3r17RUc7uHr1KoYMGYLevXujZ8+eaNeuHbRaLYqKipCcnIy4uDhcuXJFkh79+/fHSy+91OD22VTL1y0Vs82Q+OWK5kRgYCDmzp1b79Sc4zjMnz8fhw4dapRRtLGxwbx58yCXy5v17aB/B/R6PY4dO4Zjx46ZRd7kyZPRtWvXKrMQQgiWLFmCc+fOSdrvSU1NRWpqqln0mjNnDgYPHvxMGyPgyQDA398fq1evlnQUgmEYnDp1CqdOnWq0Dp6enlizZg2srKzogLGZYpY9JN47Y/v27di0aRM8PDzMIbZReHt7Y/v27fDy8qq38jMMgzZt2mDRokWNynPs2LHo2rUrrewNRKPRWERuREQEli5dKtw+zMOyLFq1aoWdO3ciODjYInnXxdSpU7F8+fIWM3gxGo0YP348PvvssyaP3efu7o4dO3YgNDSUts9mjNmcGvhGNX36dCQkJGDKlCmws7Mzl3hJhIWFITY2VlJ0baPRiAkTJkgOjsnj4uKCDz74gG52NoJx48ZhxowZZpXZvXt37Nq1q1YXYoPBgKCgIBw8eBDDhg0za961YWNjg1WrVmH9+vVQqVQtps4QQsAwDObNm4dt27Y12cA1PDwcBw4cwMCBA5/5mejfHbN62fEuo35+foiOjkZCQgLee+890d41jcXNzQ2LFy/G0aNHERYWJqny8SfLly9f3qAzClOmTEFgYOAzuTHdVBu4PXr0wLp167BixYoGRyHmkcvliIyMRGxsLHx9fescFRsMBrRp0wYxMTGIjo5Ghw4dGpV3XTr985//xJEjR7B06dJmtbTbVN+YP/Q+btw4xMXFITIyssER5uvD09MTK1aswNGjR9G9e3eLHWK1BM1Nn6bCIg7n/Lmh0NBQbNiwAefOncP27dsxcuRIeHl5mTUvjUaDkJAQrFixAmfOnMEnn3wieFI1RO++ffti8uTJkk7M+/j4YMaMGQ0a6UqZwYlBSgcnRl/+LJgYajPGYnSXyWTo2LEjFAoFoqKicPz4cbz++uuSOyutVouBAwciNjYWW7ZsgZubm6gyNhqNUCqVmDJlChISErBlyxYMGjRI0sHD2vDy8kJkZCSOHj2KAwcOoGfPnjAYDHWWv5SBTW1ypNRHU6FvLAU/cPX398e2bdsQHx+POXPmwN/fv0HROipjbW2N7t2744svvkBiYiKioqLg4OBQrzES274au9wnJR8x30PKNxbTjvlvIwZLLH1adCGX/2Hu7u6IjIzEuHHjkJ2djcuXL+Pq1au4cuUKbty4gYKCAhQVFaGsrKxOeVZWVsK15UFBQejevTsiIiLQuXNn4VRzXYWpUqmqGBr+g1c3PgMGDEB0dLToDzNr1ix4e3tLMoL8vtv69evrveiK4zjY2dlBq9XWWUkZhsHo0aMRHBxcpzcQL6O2uFaV5T333HPYvXs3OI6r00hzHAcvL68qDYQQArVajU8//RS5ubm1/kb+vaCgIKEhRkREICYmBklJSTh69Cji4+Nx+/ZtFBQUoKKiAizLQqlUCnWiffv26NmzJwYMGICwsDCo1WrJnSzHcTAYDHB0dMSkSZMwbtw4pKam4vz58/jjjz/w559/Ii0tDSUlJSgvL4fRaBQuJVQoFNBoNNDpdLC3t4evry+6dOmCsLAwhIeHC8tT/GCtLhiGwfTp0zFo0CBR39GUyzjDMOjUqRO+/fbbel2c+bBTrVq1atIZm9FohEwmQ3h4OMLDw7F06VJcvXoVFy5cwNWrV5GSkoLHjx8LMdMYhgHHccIhcSsrK9jY2MDd3R0dO3ZEly5d0K1bN3To0AE6nU74nnXBsixcXV2xe/fuei+Y5DgO7u7ukMvlko03//7KlSuRnZ1d5zchhEClUsHT07PO78EwDPr06SPqGzMMgy5dutTZ3jmOg729PTZv3lzvpZEcx8HR0bHePkkqMjyJsgoACA4ORnx8vBBhQK1WY/Xq1Vi4cCGAJwEmjxw50mA/fJlMVuXkP8dxKCsrQ05ODnJycoTKxwdT5Q9A2tjYwNbWFg4ODnBzc0OrVq2qBILkK2pdKJVKxMTEICUlBcHBwfD09IROpxPiUeXk5ODPP/9EXFwcEhMTRR2ABZ50BqdPn4aDg4PkxsxHtRCLGINX3ejWhamwTdWRGivOlI5ivS+rG5DK5cMwDAoKCpCZmYmSkhIYjUZoNBrY2trC3d0d9vb2Qr0y12ifNzR8PWNZFiUlJcjNzUVRURH0er0QvUGlUkGn08HBwQHOzs7QaDRV0lV3qKgPKR6rtX1Hqd+uKWdJpqisLz+4zM/PR35+PkpLS4X4g0qlUvj2Tk5OsLOzg1KpFOq91N9hiXZYG1K+q5jfoVQqRZ+pqhzKqTbMURYKhQJZWVkIDw/Ho0ePADw5XzhkyBDhfbVajaioKKxatapK2iZ1deGXfyo3Ho1GgzZt2qBt27aiZPCBWaXu1cjlcpw5c6bKjZXW1tZQqVSoqKio81BsbSgUCixfvhzOzs4NqqRSpsdiMfc0Wswosz4amr5y+fBx+pydnasYXI7jhMfco3t+E55HJpPB2toatra2QrzF6u9X1qUx+4nmqBfm+HZNSXV95XI5XF1d4ebmVqPT5UOL8Ya+MfXeEu2wNsydj7n3rJuyLEzx1O9Nrt7oLUl1yy82GGNtvP322xg2bBh1I20CKndALVmHloSU/UvKs8HTi6L3N6dLly5YvXo1gJbrEUOhUCjmhBqkBhAQEIBdu3Y1OGIwhUKhUGpCDZJEevTogdjYWHTo0OFvtT5PoVAozR1qkERib2+PefPm4dChQwgMDKTGiEKhUMzMU3dqaM7IZDIEBgZiyJAhGD9+PDp37gyWZakxolAoFAvQYgwSwzCYOXMmunbtitu3byMjIwOFhYWoqKgQbhy1srKCtbU1XFxc0L59e4SGhiIoKAjOzs5P3R2SQqFQnnVajEHiOA6+vr5Vroqufi7K1DXhdEZEoVAoTUOLMUhAzUNk/MFG/tAdf8COunFTKBRK09OiDFJ1qOGhUCiU5gP1sqNQKBRKs4AaJAqFQqE0C6hBolAoFEqzQNIeklwuh1arlXR5HYVCoVBaFhqNpkF2QpJBysrKQkxMDBQKBXUIoFAoFEoN5HI5CgsLG3SlT70GqbLhuXHjBkaPHi05EwqFQqG0XMROYOrdQ7KxsWm0MhQKhUJpuWi1WlHv1TlDYlkWw4cPx8mTJ5GcnEz3jigUCoUiCkIIZDIZ+vXrh65du4q6yLReg+Tp6YkffvgBJSUlZlOUQqFQKC0DBwcHABB103K9e0gsy0KhUMDR0bHRilEoFAqlZcFxnOg9pCoGSSaTQaFQQKFQ0OU5CoVCoTQaPlaomL9XMUhGoxEZGRkoLi4WNb2iUCgUCkUqarUaRUVFNf4uAyDMpVQqFVxdXensiEKhUCgWgz+rVN0oVTFIFAqFQqE8LWgsOwqFQqE0C6hBolAoFEqzgBokCoVCoTQLqEGiUCgUSrOAGiQKhUKhNAuoQaJQKBRKs+B/AXqF+j60xHAuAAAAAElFTkSuQmCC'
    logoimg=tk.PhotoImage(data=logo)
    about_label.place(x=35,y=40,height=102,width=430)
    about_label.configure(image=logoimg)
    about_label.image=logoimg
    about_label.bind("<Button-1>", lambda e: callback("https://symbolform.com/"))

    url_title=Label(aboutbox)
    url_title.place(x=35,y=10,height=40,width=430)
    url_title.configure(text="Random Chords 2.1.5", font=("Arial",15))
    url_title.bind("<Button-1>", lambda e: callback("https://symbolform.com/"))


    url_label=Label(aboutbox)
    url_label.place(x=35,y=152,height=15,width=430)
    url_label.configure(text="https://symbolform.com/")
    url_label.bind("<Button-1>", lambda e: callback("https://symbolform.com/"))

    url_label2=Label(aboutbox)
    url_label2.place(x=35,y=172,height=30,width=430)
    url_label2.configure(text="https://symbolform.com/generate-random-chords/")
    url_label2.bind("<Button-1>", lambda e: callback("https://symbolform.com/generate-random-chords/"))

    close_button=Button(aboutbox)
    close_button.place(x=220,y=200,height=30,width=40)
    close_button.configure(text="Close")
    close_button.bind("<Button-1>", close_aboutbox)
    
def close_aboutbox(event):
    aboutbox.destroy()

def callback(url):
    webbrowser.open_new_tab(url)

def aboutbox_hotkey(event):
    aboutbox()

def helpbox():
    global helpbox
    helpbox=tk.Toplevel(top)
    helpbox.geometry("440x540")
    helpbox.resizable(0,0)
    helpbox.title("Help")
    
    textbox1 = Text(helpbox)
    textbox1.place(x=20, y=20, height=470, width=400)
    scroll_2=Scrollbar (helpbox)
    scroll_2.place(x=421, y=20, height=470, anchor='n')
    textbox1.configure(yscrollcommand=scroll_2.set, wrap=WORD)
    scroll_2.configure(command=textbox1.yview)
    textbox1.focus_set()
    textbox1.bind("<Button-3>", context_menu)
    readme="RandomChords 2.1.5\nSymbolForm\n\
\n\
The purpose of the program is to generate random chords to inspire music \
creation. It can generate chords from 4 to 12 notes, with or without \
dissonances and repeated notes. All the scales matching the chord \
notes will also be generated and displayed. You can listen to the \
resulting chord and scales through the built-in play function.\n\
\n\
- Settings -\n\
\n\
Number of notes - This is the number of notes you want the chord to \
contain.\n\
Input a number from 4 to 12. The default value is 5.\n\
\n\
Repeated notes - Input a number from 0 to 12 to determine how many notes \
can be repeated in the chord. The default value is 0.\n\
\n\
Dissonances - Input a number from 0 to 12 to tell the program how many \
dissonances (notes at one semitone distance) the chord should contain. The \
default value is 0.\n\
\n\
Lowest interval - The lowest interval between notes expressed in number \
Of semitones. Accepts values from 2 to 11. The default value is 2.\n\
\n\
Highest interval - The highest interval between notes expressed in number \
of semitones. Accepts values from 3 to 11. The default value is 7.\n\
\n\
If the program cannot find a chord with the parameters you have set, it \
will try 10,000 combinations, then modify the parameters by increasing \
the number of dissonances and repeated notes allowed, then try 10,000 more \
combinations.\n\
\n\
- Play and Save chords, scales and history-\n\
\n\
The chord will be displayed in the Chord box (above the \"Chord\" label).\
All matching scales will be displayed in the Scale combo box (above the \
\"Scale\" label). You can click on the arrow at the right of the box to \
select the scale you want to play.\n\
\n\
Click on the \"Play chord\" button or Play menu- Play chord to play the \
chord.\n\
\n\
File menu - Save chord or Alt-C to save the chord as a MIDI file.\n\
\n\
Click on the \"Play scale\" button or Play menu - Play scale to play the \
scale selected in the \"Scale\" box.\n\
\n\
File menu - Save scale or Alt-S to save the scale as a MIDI file.\n\
\n\
You can import the MIDI files into a DAW or another kind of scoring \
program supporting MIDI import.\n\
\n\
The chord and the matching scales will also be displayed in the history \
Window (below the Chord and Scale boxes), in the following format:\n\
\n\
0  Dissonances allowed\n\
0  repeated notes allowed\n\
\n\
chord=  F D# G# C#\n\
\n\n\
Scales:\n\
Match 1:  F F# G# A B C# D#\n\
Match 2:  F F# G# A# B C# D#\n\
Match 3:  F F# G# A# C C# D#\n\
Match 4:  F G G# A# B C# D#\n\
Match 5:  F G G# A# C C# D#\n\
\n\n\
Chord: the chord expressed in letter notation. The first note is the \
root, on the lowest octave (the bass), the second note is the lowest note \
of the chord,the other notes are above the lowest note, ending possibly \
on higher octaves.\n\
\n\
Scales: all the scales built on the chord root containing the \
notes of the chord.\n\
\n\
The text in the chord box and in the history window can be copied for use \
in another program or for sharing through right click - Copy, CTRL-V or \
CTRL-Ins. It can also be saved to a text file through File menu - Save \
history. File menu - Erase history to erase the history window.\n\
\n\
New in this version:\n\
\n\
- Chord naming system updated"
    textbox1.insert(INSERT,readme)
    textbox1.configure(state=DISABLED)
    close_button1=Button(helpbox)
    close_button1.place(x=200,y=500,height=30,width=40)
    close_button1.configure(text="Close")
    close_button1.bind("<Button-1>", close_helpbox)

def close_helpbox(event):
    helpbox.destroy()

def helpbox_hotkey(event):
    helpbox()

main()
create_context_menu()
rootw.mainloop()
