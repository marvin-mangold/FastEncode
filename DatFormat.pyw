#!python3
import sys
import tkinter as Tk
from tkinter import IntVar
from PIL import ImageTk
#------------------------------------------------------------------

#Funktion zum Kopieren des Eingabe- in den Ausgabetext
def CopyPaste():
    if StartStopButton.cget("text")== "Pause":
        try:
            Eingabe = (Eingabe_Textfeld.get("1.0","end"))
            Ausgabe = StringUmwandeln(Eingabe)
            Ausgabe_Textfeld.delete("1.0","end")
            Ausgabe_Textfeld.insert("1.0",Ausgabe)
        except:
            Ausgabe_Textfeld.delete("1.0","end")
            Ausgabe_Textfeld.insert("1.0","Ein Fehler ist aufgetreten, Kein ASCII Zeichen zu dieser Zahl möglich")
    StartStopButton.after(5, CopyPaste)

#Hiermit wird der Text des Button beim klicken des Button angepasst       
def StartStop(start_klick = [0]):
    start_klick[0] = not start_klick[0]
    if start_klick[0]:
        StartStopButton.config(text='Pause')
    else:
        StartStopButton.config(text='Start')

#Hier wird der String abhaengig der Programmnummer umgewandelt
def StringUmwandeln(String):
    String = String.strip()#Das \n am ende des String herausfiltern
    Liste = String.split(" ")#Bei den Leerzeichen schneiden und in Liste speichern
#----------Hex zu Ascii--------------------------------------------    
    if ((AuswalVon.get() == 1) and (AuswalZu.get() == 4)):
        for i in range(len(Liste)):
            try:
                Liste[i] = str(chr(int(Liste[i], 16)))
            except:
                Liste[i] = "Fehler"
#----------Ascii zu Hex--------------------------------------------    
    if ((AuswalVon.get() == 4) and (AuswalZu.get() == 1)):
        for i in range(len(Liste)):
            try:
                Liste[i] = str(hex(ord(Liste[i]))[2:])
            except:
                Liste[i] = "Fehler"
#----------Hex zu Dez----------------------------------------------  
    elif ((AuswalVon.get() == 1) and (AuswalZu.get() == 2)):
        for i in range(len(Liste)):
            try:
                Liste[i] = str(int(Liste[i],16))     
            except:
                Liste[i] = "Fehler"
#----------Dez zu Hex----------------------------------------------  
    elif ((AuswalVon.get() == 2) and (AuswalZu.get() == 1)):
        for i in range(len(Liste)):
            try:
                Liste[i] = str(hex(int(Liste[i]))[2:])     
            except:
                Liste[i] = "Fehler" 
#----------Hex zu Bin----------------------------------------------  
    elif ((AuswalVon.get() == 1) and (AuswalZu.get() == 3)):
        for i in range(len(Liste)):
            try:
                Liste[i] = str(bin(int(Liste[i],16))[2:])    
            except:
                Liste[i] = "Fehler"
#----------Bin zu Hex----------------------------------------------  
    elif ((AuswalVon.get() == 3) and (AuswalZu.get() == 1)):
        for i in range(len(Liste)):
            try:
                Liste[i] = str(hex(int(Liste[i],2))[2:])    
            except:
                Liste[i] = "Fehler" 
#----------Dez zu Bin----------------------------------------------  
    elif ((AuswalVon.get() == 2) and (AuswalZu.get() == 3)):
        for i in range(len(Liste)):
            try:
                Liste[i] = str(bin(int(Liste[i]))[2:])  
            except:
                Liste[i] = "Fehler"
#----------Bin zu Dez----------------------------------------------  
    elif ((AuswalVon.get() == 3) and (AuswalZu.get() == 2)):
        for i in range(len(Liste)):
            try:
                Liste[i] = str(int(Liste[i],2))   
            except:
                Liste[i] = "Fehler"
#----------Dez zu ASCII----------------------------------------------  
    elif ((AuswalVon.get() == 2) and (AuswalZu.get() == 4)):
        for i in range(len(Liste)):
            try:
                Liste[i] = str(chr(int(Liste[i]))) 
            except:
                Liste[i] = "Fehler"
#----------ASCII zu Dez----------------------------------------------  
    elif ((AuswalVon.get() == 4) and (AuswalZu.get() == 2)):
        for i in range(len(Liste)):
            try:
                Liste[i] = str(ord(Liste[i]))  
            except:
                Liste[i] = "Fehler"
#----------Bin zu ASCII----------------------------------------------  
    elif ((AuswalVon.get() == 3) and (AuswalZu.get() == 4)):
        for i in range(len(Liste)):
            try:
                Liste[i] = str(chr(int(Liste[i],2)))
            except:
                Liste[i] = "Fehler"
#----------ASCII zu Bin----------------------------------------------  
    elif ((AuswalVon.get() == 4) and (AuswalZu.get() == 3)):
        for i in range(len(Liste)):
            try:
                Liste[i] = str(bin(ord(Liste[i]))[2:])  
            except:
                Liste[i] = "Fehler"
#---------Eins nicht ausgewaehlt-------------------------------------
    elif ((AuswalVon.get() == 0) or (AuswalZu.get() == 0)):
        Liste = ["Datenformate auswählen"]
#------------------------------------------------------------------
    elif ((AuswalVon.get())==(AuswalZu.get())):
        Liste = ["Das ergibt keinen Sinn"]
#------------------------------------------------------------------   
    String = " ".join(Liste)
    return String    
#------------------------------------------------------------------
    
#Fenster erstellen
Fenster = Tk.Tk()
#Fenster einstellen
Fensterbreite = 600 
Fensterhoehe = 400 
Monitorbreite = Fenster.winfo_screenwidth()
Monitorhoehe = Fenster.winfo_screenheight()
FensterstartposX = (Monitorbreite/2) - (Fensterbreite/2)
FensterstartposY = (Monitorhoehe/2) - (Fensterhoehe/2)

#Hintergrundbild des Fensters
Hintergrundbild = Tk.Canvas(Fenster)
Hintergrundbild.pack(fill='both', expand=True)
image = ImageTk.PhotoImage(file = "Wicke.png")
Hintergrundbild.create_image(0, 0, anchor= "nw", image = image)
Fenster.geometry('%dx%d+%d+%d' %(Fensterbreite, Fensterhoehe, FensterstartposX, FensterstartposY))
Fenster.resizable(0, 0)
Fenster.title("DatFormat")
Fenster.iconbitmap("Wicke.ico")

#Label fuer Eingabe erstellen
Label_Eingabe = Tk.Label(Fenster, text="Eingabe:",background="#BCC6CC", fg="#44486A")
Label_Eingabe.place(x=((Fensterbreite/2)-280),y=((Fensterhoehe/2)-140),height="25")
#Textfeld fuer Eingabe erstellen
Eingabe_Textfeld = Tk.Text(Fenster, width=10, wrap="word")
Eingabe_Textfeld.place(x=((Fensterbreite/2)-272),y=((Fensterhoehe/2)-115), height="80", width="540")

#Label fuer Ausgabe erstellen
Label_Ausgabe = Tk.Label(Fenster, text="Ausgabe:",background="#BCC6CC", fg="#44486A")
Label_Ausgabe.place(x=((Fensterbreite/2)-280),y=((Fensterhoehe/2)+50),height="25")
#Textfeld fuer Ausgabe erstellen
Ausgabe_Textfeld = Tk.Text(Fenster, width=10, wrap="word", relief="sunken")
Ausgabe_Textfeld.place(x=((Fensterbreite/2)-272),y=((Fensterhoehe/2+75)), height="80", width="540")

#Button fuer Start und Stop erstellen.
StartStopButton = Tk.Button(text="Start", background="#BCC6CC", fg="#44486A", command= StartStop)
StartStopButton.place(x=((Fensterbreite/2)-70), y=((Fensterhoehe/2)+8), width="80")

#Radiobutton erstellen (mehrere Checkboxen von denen nur jeweil eine aktiv ist)
#Variablen definieren
AuswalVon= IntVar()#Tkinter Datentyp von Format
Datenformate=[("Hex",1,0),("Dec",2,25),("Bin",3,50),("ASCII",4,75)]
for formate,nummer,abstand in Datenformate:
    Tk.Radiobutton(Fenster, indicatoron= 0, background= "#BCC6CC", fg= "#44486A", text= formate, width= "5",height= "1", variable= AuswalVon, value= nummer).place(x=((Fensterbreite/2)-150),y=((Fensterhoehe/2)-30 +abstand))

#Radiobutton erstellen (mehrere Checkboxen von denen nur jeweil eine aktiv ist)
AuswalZu= IntVar()#Tkinter Datentyp in Format
Datenformate=[("Hex",1,0),("Dec",2,25),("Bin",3,50),("ASCII",4,75)]
for formate,nummer,abstand in Datenformate:
    Tk.Radiobutton(Fenster, indicatoron= 0, background= "#BCC6CC", fg= "#44486A", text= formate, width= "5",height= "1", variable= AuswalZu, value= nummer).place(x=((Fensterbreite/2)+45),y=((Fensterhoehe/2)-30 +abstand))
#------------------------------------------------------------------


CopyPaste()#Dauerschleife fuer das Kopieren und Uebersetzprogramm ausfuehren

Fenster.mainloop()
