import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme('Topanga')

left_column_content = [[sg.Text('', key='current_time')],
                       [sg.Text("Type in a To-Do")],
                       [sg.InputText(tooltip="Enter ToDo", key='todo')],
                       [sg.Listbox(values=functions.get_todos(), key='todos',
                        enable_events=True, size=(45, 10))]]
right_column_content = [[sg.Button("Add", size=10)],
                        [],
                        [sg.Button('Edit', size=10)],
                        [sg.Button('Complete', size=10)],
                        [sg.Button('Quit', size=10)]]
left_column = sg.Column(left_column_content)
right_column = sg.Column(right_column_content)
layout = [[left_column, right_column]]

window = sg.Window("My To-Do App",
                   layout=layout,
                   font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=200)
    window['current_time'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'].strip('\n')
            new_todo = new_todo + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].strip('\n')
                new_todo = new_todo + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.Popup("Please select an item first", font=('Helvetica', 16))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.Popup("Please select an item first", font=('Helvetica', 16))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Quit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
