from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from datetime import datetime

import os
import sys



class Notes(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle("NoteTaker")

        #Widgets
        self.labelName = QLabel(self)
        self.labelName.setText("Your notes:")

        self.inputwindow = QTextEdit(self)
        self.inputwindow.setText("")

        self.savebutton = QPushButton(self)
        self.savebutton.setText("Save")
        self.savebutton.clicked.connect(self.SaveNote)

        self.deletebutton = QPushButton(self)
        self.deletebutton.setText("Delete all notes")
        self.deletebutton.clicked.connect(self.DeleteNote)

        self.spacer = QLabel(self)
        self.spacer.setText("")

        self.exitbutton = QPushButton(self)
        self.exitbutton.setText("Quit")
        self.exitbutton.clicked.connect(self.Quit)


        self.ui()
        self.ReadNote()

    def ui(self):
        layout = QVBoxLayout()

        #Adding widgets to layout
        layout.addWidget(self.labelName)
        layout.addWidget(self.inputwindow)
        layout.addWidget(self.savebutton)
        layout.addWidget(self.deletebutton)
        layout.addWidget(self.spacer)
        layout.addWidget(self.exitbutton)

        self.setLayout(layout)
        self.show()

    def SaveNote(self):
        text = self.inputwindow.toPlainText()
        time = datetime.now()

        print("\n",time, "\nNote is:", text, "\n")

        file = open("notes.txt", "w+")
        file.write(text)

    def DeleteNote(self):
        if os.path.isfile("notes.txt"):
            os.remove("notes.txt")
            print("\nNotes were removed!")
            self.inputwindow.setText("Notes were deleted...")
        else:
            print("\nNotes does not exist!")
            self.inputwindow.setText("Notes were deleted...")

    def ReadNote(self):
        if os.path.isfile("notes.txt"):
            file = open("notes.txt", "r+")
            notes = file.read()
            self.inputwindow.setText(str(notes))

            print("\nOld notes are:" + "\n  ", str(notes))

        else:
            self.inputwindow.setText("Write your notes here...")

    def Quit(self):
        sys.exit()

while __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Notes()
    sys.exit(app.exec())
