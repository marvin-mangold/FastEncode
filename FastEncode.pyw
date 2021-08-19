"""
FastEncode - Encode: Hex <-> Bin <-> Dec <-> ASCII
Copyright (C) 2021  Marvin Mangold (Marvin.Mangold00@googlemail.com)
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import IntVar
from pathlib import Path


class Controller(object):
    def __init__(self):
        """
        -initialise window
        -set windowsize and position
        -set title and icon
        -call view class
        -bind button callbacks
        """
        self.window = tk.Tk()
        self.window_width = 600
        self.window_height = 400
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.screen_posX = (self.screen_width / 2) - (self.window_width / 2)
        self.screen_posY = (self.screen_height / 2) - (self.window_height / 2)
        self.window.title("FastEncode")  # window title
        self.window.iconbitmap("Media/icon.ico")  # icon in window titlebar
        self.window.resizable(0, 0)  # lock windowsize
        self.window.geometry('%dx%d+%d+%d' % (self.window_width, self.window_height,
                                              self.screen_posX, self.screen_posY))
        # load tkinter ttk style theme
        self.window.tk.call("lappend", "auto_path", Path("Tkinter_Theme/awthemes-9.5.0/"))
        self.window.tk.call("package", "require", Path("awdark"))
        self.style_main = ttk.Style()
        self.style_main.theme_use(Path("awdark"))
        # load screens
        self.container = ttk.Frame(self.window, style="TFrame")
        self.container.place(x=0, y=0, height="400", width="600")
        self.screens = {"Main": Mainscreen(self.container)}
        for screen in self.screens:
            self.screens[screen].place(x=0, y=0, height="400", width="600")
        # status flag
        self.encoding = False
        # buttons
        self.screens["Main"].btn_encode.bind("<ButtonRelease>", lambda x: self.toggle_encode())

    def run(self):
        """
        -open Main screen
        -start mainloop
        -start secondloop
        """
        self.show_screen("Main")
        self.window.after(0, self.encode)
        self.window.mainloop()

    def show_screen(self, screen="Main"):
        """
        -change screen
        """
        self.screens[screen].tkraise()

    def encode(self):
        """
        -retrigger self every 50ms
        -encode data
        """
        if self.encoding:
            inputstring = self.screens["Main"].entry_input.get("1.0", "end")
            outputstring = encoder(
                inputstring=inputstring,
                encodefrom=self.screens["Main"].convertfrom.get(),
                encodeto=self.screens["Main"].convertto.get())
            self.screens["Main"].entry_output.delete("1.0", "end")
            self.screens["Main"].entry_output.insert("1.0", outputstring)
        # trigger every 10ms
        self.window.after(10, self.encode)

    def toggle_encode(self):
        self.encoding = not self.encoding
        if self.encoding:
            self.screens["Main"].btn_encode.config(text='stop')
        else:
            self.screens["Main"].btn_encode.config(text='start')


class Mainscreen(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.background = tk.Canvas(self, background="#33393b")
        self.background.place(x=0, y=0, width=600, height=400)
        # create label for input
        self.lbl_input = ttk.Label(self, text="Input:", style="TLabel")
        self.lbl_input.place(x=20, y=25, height=25)
        # create entry for input
        self.entry_input = tk.Text(self, width=10, wrap="word", bg="#3d4145", fg="#ffffff", bd=5, font=("arial", 10))
        self.entry_input.place(x=20, y=50, height=80, width=560)
        # create label for output
        self.lbl_output = ttk.Label(self, text="Output:", style="TLabel")
        self.lbl_output.place(x=20, y=245, height=25)
        # create entry for output
        self.entry_output = tk.Text(self, width=10, wrap="word", bg="#3d4145", fg="#ffffff", bd=5, font=("arial", 10))
        self.entry_output.place(x=20, y=270, height=80, width=560)
        # create button to toggle live encoding
        self.btn_encode = ttk.Button(text="start", style="TButton")
        self.btn_encode.place(x=250, y=180, width=100, height=40)
        # create radiobuttons for "convert from" choice
        self.convertfrom = tk.IntVar()
        self.rdb_from_hex = ttk.Radiobutton(self, text="HEX", variable=self.convertfrom, value=1, style="TRadiobutton")
        self.rdb_from_hex.place(x=97, y=140, width=56, height=30)
        self.rdb_from_dec = ttk.Radiobutton(self, text="DEC", variable=self.convertfrom, value=2, style="TRadiobutton")
        self.rdb_from_dec.place(x=97, y=170, width=56, height=30)
        self.rdb_from_bin = ttk.Radiobutton(self, text="BIN", variable=self.convertfrom, value=3, style="TRadiobutton")
        self.rdb_from_bin.place(x=97, y=200, width=56, height=30)
        self.rdb_from_asc = ttk.Radiobutton(self, text="ASCII", variable=self.convertfrom, value=4, style="TRadiobutton")
        self.rdb_from_asc.place(x=97, y=230, width=56, height=30)
        # create radiobuttons for "convert to" choice
        self.convertto = tk.IntVar()
        self.rdb_to_hex = ttk.Radiobutton(self, text="HEX", variable=self.convertto, value=1, style="TRadiobutton")
        self.rdb_to_hex.place(x=447, y=140, width=56, height=30)
        self.rdb_to_dec = ttk.Radiobutton(self, text="DEC", variable=self.convertto, value=2, style="TRadiobutton")
        self.rdb_to_dec.place(x=447, y=170, width=56, height=30)
        self.rdb_to_bin = ttk.Radiobutton(self, text="BIN", variable=self.convertto, value=3, style="TRadiobutton")
        self.rdb_to_bin.place(x=447, y=200, width=56, height=30)
        self.rdb_to_asc = ttk.Radiobutton(self, text="ASCII", variable=self.convertto, value=4, style="TRadiobutton")
        self.rdb_to_asc.place(x=447, y=230, width=56, height=30)


def encoder(inputstring="", encodefrom=1, encodeto=1):
    inputstring = inputstring.strip()
    encodelist = inputstring.split(" ")
    # HEX to ASCII
    if encodefrom == 1 and encodeto == 4:
        for i in range(len(encodelist)):
            try:
                encodelist[i] = str(chr(int(encodelist[i], 16)))
            except Exception as errortext:
                print(errortext)
                encodelist[i] = "error"
    # ASCII to HEX
    elif encodefrom == 4 and encodeto == 1:
        for i in range(len(encodelist)):
            try:
                encodelist[i] = str(hex(ord(encodelist[i]))[2:])
            except Exception as errortext:
                print(errortext)
                encodelist[i] = "error"
    # HEX to DEC
    elif encodefrom == 1 and encodeto == 2:
        for i in range(len(encodelist)):
            try:
                encodelist[i] = str(int(encodelist[i], 16))
            except Exception as errortext:
                print(errortext)
                encodelist[i] = "error"
    # DEC to HEX
    elif encodefrom == 2 and encodeto == 1:
        for i in range(len(encodelist)):
            try:
                encodelist[i] = str(hex(int(encodelist[i]))[2:])
            except Exception as errortext:
                print(errortext)
                encodelist[i] = "error"
    # HEX to BIN
    elif encodefrom == 1 and encodeto == 3:
        for i in range(len(encodelist)):
            try:
                encodelist[i] = str(bin(int(encodelist[i], 16))[2:])
            except Exception as errortext:
                print(errortext)
                encodelist[i] = "error"
    # BIN to HEX
    elif encodefrom == 3 and encodeto == 1:
        for i in range(len(encodelist)):
            try:
                encodelist[i] = str(hex(int(encodelist[i], 2))[2:])
            except Exception as errortext:
                print(errortext)
                encodelist[i] = "error"
    # DEC to BIN
    elif encodefrom == 2 and encodeto == 3:
        for i in range(len(encodelist)):
            try:
                encodelist[i] = str(bin(int(encodelist[i]))[2:])
            except Exception as errortext:
                print(errortext)
                encodelist[i] = "error"
    # BIN to DEC
    elif encodefrom == 3 and encodeto == 2:
        for i in range(len(encodelist)):
            try:
                encodelist[i] = str(int(encodelist[i], 2))
            except Exception as errortext:
                print(errortext)
                encodelist[i] = "error"
    # DEC to ASCII
    elif encodefrom == 2 and encodeto == 4:
        for i in range(len(encodelist)):
            try:
                encodelist[i] = str(chr(int(encodelist[i])))
            except Exception as errortext:
                print(errortext)
                encodelist[i] = "error"
    # ASCII to DEZ
    elif encodefrom == 4 and encodeto == 2:
        for i in range(len(encodelist)):
            try:
                encodelist[i] = str(ord(encodelist[i]))
            except Exception as errortext:
                print(errortext)
                encodelist[i] = "error"
    # BIN to ASCII
    elif encodefrom == 3 and encodeto == 4:
        for i in range(len(encodelist)):
            try:
                encodelist[i] = str(chr(int(encodelist[i], 2)))
            except Exception as errortext:
                print(errortext)
                encodelist[i] = "error"
    # ASCII to BIN
    elif encodefrom == 4 and encodeto == 3:
        for i in range(len(encodelist)):
            try:
                encodelist[i] = str(bin(ord(encodelist[i]))[2:])
            except Exception as errortext:
                print(errortext)
                encodelist[i] = "error"
    # nothing chosen to encode from
    elif encodefrom == 0 or encodeto == 0:
        encodelist = ["choose encoding option"]
    # nothing to convert
    elif encodefrom == encodeto:
        encodelist = ["look before you leap"]
    return " ".join(encodelist)


if __name__ == '__main__':
    app = Controller()
    app.run()
