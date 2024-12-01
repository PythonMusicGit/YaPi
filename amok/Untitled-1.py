
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout


import json


app = QApplication([])

notes_win = QWidget()
notes_win.setWindowTitle('Ya Jesus')
notes_win.resize(900, 600)

list_notes = QListWidget()
list_notes_label = QLabel('Biibliia Verses')
button_note_create = QPushButton('Copy Verse')
button_note_del = QPushButton('Forget Verse')
button_note_save = QPushButton('Praise Verse')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Enter commentary... ')
field_text = QTextEdit()
button_tag_add = QPushButton('Add commentary')
button_tag_del = QPushButton('Lie')
button_tag_search = QPushButton('Follow the truth way. Follow the progressive protestantism Praise Jesus Praise Jesus Praise Jesus Praise Jesus Praise Jesus Praise Jesus Praise Jesus Praise Jesus Praise Jesus Praise Jesus')
list_tags = QListWidget()
list_tags_label = QLabel('Commentaries')
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
col_2 = QVBoxLayout()