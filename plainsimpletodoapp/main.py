import flet


def main(page: flet.Page):

    #Window size
    page.window_width = 1000
    page.window_height = 500
    page.padding = 0

    taskslist = flet.ListView(expand=1, spacing=16, padding=8, auto_scroll=False)

    bottom_input = flet.Container(margin=10, content=flet.TextField(label=None, border_radius=flet.border_radius.all(15), filled=True,))

    exampletask = flet.FilledTonalButton(content=flet.ListTile(leading=flet.Checkbox(), title=flet.Text("Example task"), subtitle=flet.Text("Due: 2024.05.25 - 20:40"), trailing=flet.PopupMenuButton(icon=flet.icons.MORE_VERT, items=[flet.PopupMenuItem(icon=flet.icons.EDIT, text="Edit"), flet.PopupMenuItem(icon=flet.icons.DELETE, text="Delete")])))

    for i in range(20):
        taskslist.controls.append(exampletask)


    page.add(taskslist)
    page.add(bottom_input)

flet.app(main)
