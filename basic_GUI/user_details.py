import PySimpleGUI as gui

layout = [
    [gui.Text("Basic GUI")],
    [gui.Text(size=(20, 2), key="-OUTPUT-")],
    [gui.Input(default_text="Your Message", key="-MESSAGE-")],
    [gui.Button("Send", tooltip="Send A Message")]
]

window = gui.Window("Basic UI", layout, finalize=True)
window['-MESSAGE-'].bind("<Return>", "_Enter")

while True:
    event, values = window.read()

    if event == gui.WIN_CLOSED:
        break
    elif event == "Send":
        window["-OUTPUT-"].update(values["-MESSAGE-"])

window.close()
