import PySimpleGUI as sg
import functions as func

sg.theme("Darkteal12")
headers = func.get_headers()
table = func.get_bills()
values = table.values.tolist()
sg.set_options(font=('Courier New', 12))
add_bill_button1 = sg.Button('Add New Bill', tooltip="Add A New Bill", key='Add')
bill_input_box = sg.InputText(tooltip="Enter New Bill Name:", key="new_bill")
bill_amount_box = sg.InputText(tooltip="Enter New Bill Amount:", key="new_bill_amount")
add_bill_button2 = sg.Button('Add Bill', tooltip="Add Bill", key='Add2')
layout = [[bill_input_box],
          [bill_amount_box],
          [add_bill_button1],
          [sg.Table(values=values, headings=headers,
                    auto_size_columns=False, key='table'
                    )]]

window = sg.Window('Bills', layout)

while True:
    event, value = window.read()
    print(event)
    match event:
        case "Add":
            func.create_new_bill(value["new_bill"], value["new_bill_amount"])
            new_bills = func.get_bills()
            table_data = new_bills.values.tolist()
            window['table'].update(values=table_data)
            window["new_bill"].update(value='')
            window['new_bill_amount'].update(value='')

        case sg.WIN_CLOSED:
            break

window.close()
