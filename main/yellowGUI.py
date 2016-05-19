# coding: utf-8

import Tkinter as Tk
import os
import tkFileDialog as Ofd

import yellow


class YellowGUI:
    def __init__(self):
        self.yellow = 0
        self.txtPath = 0
        self.build()

    def build(self):
        fen = Tk.Tk()
        fen.title('MonProgramme')
        self.txtPath = Tk.StringVar()
        fen.resizable(0, 0)
        Tk.Label(fen, text='Source').grid(row=1, column=1, sticky='EW')
        Tk.Entry(fen, textvar=self.txtPath).grid(row=1, column=2, sticky='EW')
        Tk.Button(fen, text='Open', command=self.open).grid(row=1, column=3, sticky='EW')
        Tk.Button(fen, text='Read', command=self.read).grid(row=2, column=3, sticky='EW')
        Tk.Button(fen, text='Display', command=self.disp).grid(row=3, column=3, sticky='EW')
        fen.mainloop()

    def open(self):
        dirpath = Ofd.askdirectory(title='Open model', initialdir=os.getcwd())
        if dirpath:
            self.txtPath.set(dirpath)
            self.yellow = yellow.Yellow(dirpath)

    def read(self):
        if isinstance(self.yellow, yellow.Yellow):
            self.yellow.lire()
        else:
            print('choose srcDir')

    def disp(self):
        if isinstance(self.yellow, yellow.Yellow):
            self.yellow.afficher()
        else:
            print('choose srcDir')


if __name__ == '__main__':
    YellowGUI()
