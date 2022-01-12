import PySimpleGUI as gui

layout = [
    [gui.Text("Basic GUI")],
    [gui.Input(default_text="Your Message", key="-MESSAGE-")],
    [gui.Button("Send", tooltip="Send A Message")]
]

window = gui.Window("Basic UI", layout, finalize=True)
window['-MESSAGE-'].bind("<Return>", "_Enter")


while True:
    event, values = window.read()

    if event == gui.WIN_CLOSED:
        break

    if event == "Send":
        print(values["-MESSAGE-"])
    elif event == "-MESSAGE-" + "_ENTER":
        window["-MESSAGE-"].update("")

window.close()
