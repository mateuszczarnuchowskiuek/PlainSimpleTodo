import flet #Module for GUI: https://flet.dev/
import json 
import datetime

#taskslists is a data structure for tracking every list of tasks and their contents (individual tasks). For the time being there's only a single list of tasks called "tasks". It's basically future-proofing to be able to add multiple lists functionality later.
taskslists = {
#This data is a placeholder and is overwritten on LoadSaveFile()
    "tasks": [
        {
            "task_name": "Test task 1",
            "due_date": None, #due_date is for future use (not yet implemented)
            "done": False   #it's for checkbox next to the task
        },
        {
            "task_name": "Test task 2",
            "due_date": None,
            "done": False
        },
        {
            "task_name": "Test task 3",
            "due_date": None,
            "done": False
        },
        {
            "task_name": "Test task 4",
            "due_date": None,
            "done": False
        }
    ]
}

def main(ui_page: flet.Page):

    # ----------

    def addTask(e):
        #First we check if there is anything typed in the input field. If there is we create new task from this input. 
        if ui_main_input_textfield.value != "":
            new_task = {
                "task_name": ui_main_input_textfield.value,
                "due_date": None,
                "done": False
            }
            taskslists["tasks"].append(new_task) #it adds a task to our data structure
            UpdateSaveFile()
            Update_ui_taskslist() #it reloads the visual list of tasks to sync it with data structure list of tasks
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

    def DeleteTask(e): #e is an "event" and is passed from onClicked from flet by default
        #print(e.control) #debug
        #print(e.control.data) #debug
        taskslists["tasks"].remove(e.control.data) #e.control.data is how I can access parameter called "data" that I can set for each delete button instance so I can access the task (which is higher in the hierarchy) I want to delete. This line of code removes task from the DATA STRUCTURE ONLY!
        UpdateSaveFile()
        Update_ui_taskslist() #we now have to update the visual representation of the data structure
        ui_page.update()
        pass

    # ----------

    #This function updates visual representation of tasks to match our current data structure storing tasks
    def Update_ui_taskslist():
        ui_taskslist.controls.clear() #first we clear everything so that we can start from scratch
        
        #Now for each task in our data structure we create a visual element representing that task 
        for i in taskslists["tasks"]:
            ui_task = flet.FilledTonalButton(content=flet.ListTile(leading=flet.Checkbox(value=i["done"]), title=flet.Text(i["task_name"]), subtitle=flet.Text(ExtractDueDate(i)), trailing=flet.PopupMenuButton(icon=flet.icons.MORE_VERT, items=[flet.PopupMenuItem(icon=flet.icons.EDIT, text="Edit"), flet.PopupMenuItem(icon=flet.icons.DELETE, text="Delete", on_click=DeleteTask, data=i)])))
            
            ui_taskslist.controls.append(ui_task)
        pass
    
    # ----------

    def UpdateSaveFile():
        with open("save.json", "w") as save_file:
            json.dump(taskslists, save_file)

    # ----------

    def LoadSaveFile():
        try:
            with open("save.json", "r") as save_file:
                data = json.load(save_file)
                global taskslists #this variable has to be marked as global due to how python works: https://stackoverflow.com/questions/423379/how-to-use-a-global-variable-in-a-function#423596
                taskslists = data
        except:
            taskslists = {"tasks": []} #if file doesn't exist it creates an empty one
            

    # ---------- ACTUAL PROGRAM STARTS HERE ----------

    ui_page.padding = 0 #default is different and that's annoying

    #Window size (optional)
    ui_page.window_width = 1000
    ui_page.window_height = 500

    #We try to load the save file
    LoadSaveFile()

    # ---------- CREATING APP LAYOUT: ----------
    
    #Creating list view
    ui_taskslist = flet.ListView(expand=1, spacing=16, padding=8, auto_scroll=False)

    #Creating text input field
    ui_main_input_textfield = flet.TextField(on_submit=addTask, expand=True, label=None, border_radius=flet.border_radius.all(15), filled=True)

    #Eeserving space at the bottom and adding there the text input field and a button next to it
    ui_bottom_input = flet.Container(padding=10, content=flet.Row(controls=[ui_main_input_textfield, flet.IconButton(visible=False, icon=flet.icons.CALENDAR_MONTH_OUTLINED, bgcolor=flet.colors.BLUE_800), flet.IconButton(icon="add", bgcolor=flet.colors.BLUE_800, on_click=addTask)]))

    # ----------

    #We update our visual representation of tasks
    Update_ui_taskslist()

    #We add our layout to the page
    ui_page.add(ui_taskslist)
    ui_page.add(ui_bottom_input)

flet.app(main)
