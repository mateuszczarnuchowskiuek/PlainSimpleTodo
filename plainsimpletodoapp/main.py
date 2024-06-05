import flet
import json
import datetime

taskslists = {
    "tasks": [
        {
            "task_name": "Test task 1",
            "due_date": datetime.datetime(2024,5,30,12,0),
            "done": False
        },
        {
            "task_name": "Test task 2",
            "due_date": datetime.datetime(2024,6,2,13,5),
            "done": False
        },
        {
            "task_name": "Test task 3",
            "due_date": None,
            "done": False
        },
        {
            "task_name": "Test task 4",
            "due_date": datetime.datetime(2024,6,2,13,5),
            "done": False
        }
    ]
}

def main(ui_page: flet.Page):

    def addTask(e):
        if ui_main_input_textfield.value != "":
            new_task = {
                "task_name": ui_main_input_textfield.value,
                "due_date": None,
                "done": False
            }
            taskslists["tasks"].append(new_task)
            Update_ui_taskslist() #reloads the visual list of tasks
            ui_main_input_textfield.value = "" #clears text from text input field
            ui_page.update()
        ui_main_input_textfield.focus()
        pass

    # ----------

    def ExtractDueDate(i):
        if i["due_date"]!=None:
            extracted_due_date = f"Due: {i["due_date"].strftime("%Y.%m.%d - %H:%M")}"
        else:
            extracted_due_date = ""
        return extracted_due_date
        pass

    # ----------

    def DeleteTask(e):
        print(e.control)
        print(e.control.data)
        taskslists["tasks"].remove(e.control.data) #this is how I can access parameter called "data" that I can set for the delete button so I can access entire task
        Update_ui_taskslist()
        ui_page.update()
        pass

    # ----------

    def Update_ui_taskslist():
        ui_taskslist.controls.clear()

        for i in taskslists["tasks"]:
            ui_task = flet.FilledTonalButton(content=flet.ListTile(leading=flet.Checkbox(value=i["done"]), title=flet.Text(i["task_name"]), subtitle=flet.Text(ExtractDueDate(i)), trailing=flet.PopupMenuButton(icon=flet.icons.MORE_VERT, items=[flet.PopupMenuItem(icon=flet.icons.EDIT, text="Edit"), flet.PopupMenuItem(icon=flet.icons.DELETE, text="Delete", on_click=DeleteTask, data=i)])))
            
            ui_taskslist.controls.append(ui_task)
        pass
    
    # ---------- ACTUAL PROGRAM STARTS HERE ----------

    ui_page.padding = 0
    #Window size
    ui_page.window_width = 1000
    ui_page.window_height = 500



    ui_taskslist = flet.ListView(expand=1, spacing=16, padding=8, auto_scroll=False)
    ui_main_input_textfield = flet.TextField(on_submit=addTask, expand=True, label=None, border_radius=flet.border_radius.all(15), filled=True)

    ui_bottom_input = flet.Container(padding=10, content=flet.Row(controls=[ui_main_input_textfield, flet.IconButton(icon=flet.icons.CALENDAR_MONTH_OUTLINED, bgcolor=flet.colors.BLUE_800), flet.IconButton(icon="add", bgcolor=flet.colors.BLUE_800, on_click=addTask)]))

    
    Update_ui_taskslist()

    ui_page.add(ui_taskslist)
    ui_page.add(ui_bottom_input)

flet.app(main)
