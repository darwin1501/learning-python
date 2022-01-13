import PySimpleGUI as gui

layout = []

for a in range(4):
    numbers = []

    for b in range(4):
        numbers.append(gui.Button(f"{a},{b}"))
    layout.append(numbers)

window = gui.Window("Grid", layout)

while True:
    event, values = window.read()

    if event == gui.WIN_CLOSED:
        break

window.close()
