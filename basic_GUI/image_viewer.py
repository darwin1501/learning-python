import PySimpleGUI as gui
import os.path

file_list_column = [
    [
        gui.Text("Image Folder"),
        gui.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        gui.FolderBrowse()
    ],
    [
        gui.Listbox(
            values=[],
            enable_events=True,
            size=(40, 20),
            key="-FILE LIST-"
        )
    ]
]

image_viewer_column = [
    [gui.Text("Choose an image from list on left:")],
    [gui.Text(size=(40, 1), key="-TOUT-")],
    [gui.Image(key="-IMAGE-")]
]

# ----- Full layout ----
layout = [
    [
        gui.Column(file_list_column),
        gui.VSeparator(),
        gui.Column(image_viewer_column)
    ]
]

# add your layout to the frame
window = gui.Window("Image viewer", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == gui.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
               and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass

window.close()
