
import PySimpleGUI as gui
import os.path

file_list_column = [
    [
        gui.Text("Image Folder"),
        gui.In(size=(25,1), enable_events=True,key="-FOLDER-"),
        gui.FolderBrowse()
    ],
    [
        gui.Listbox(
            values=[],
            enable_events=True,
            size=(40,20),
            key="-FILE LIST-"
        )
    ]
]

