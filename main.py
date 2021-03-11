import wolframalpha
import PySimpleGUI as sg

# Receive a free API key
client = wolframalpha.Client("QJV862-WP3V2U8PP3")

# Select theme for GUI
sg.theme('Black')

# Create the structure of your GUI setup
setup = [  [sg.Text('Computational Intelligence Answering Basic Questions')],
            [sg.Text('Enter a question'), sg.InputText()],
            [sg.Button('Answer'), sg.Button('Exit')]  ]

# Open up the GUI window
display = sg.Window('A Simple Computational Intelligence', setup)

# Allow the user to keep inputting a command until the command cannot be answered
while True:
    event, command = display.read()
    if event in (None, 'Exit'):
        break
    server = client.query(command[0])
    print('You entered', command[0])
    print('Answer: \n', next(server.results).text)

# Close the window
display.close()