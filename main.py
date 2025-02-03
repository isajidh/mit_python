import tkinter as tk
from second import SecondaryUI
from tkinter import ttk
from second import SecondaryUI
from usercreation import UserCreation
from add_asset_item import AddAssetItem
from add_amc_detail import AddAMCDetail

class App(tk.Tk):
    def __init__(self, title, size):
        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        self.state('zoomed')  # Maximizes the window

        # widgets
        self.top_bar = TopBar(self)  # Add the top frame
        self.menu = Menu(self)
        self.main = Main(self)

        # run
        self.mainloop()


class TopBar(tk.Frame):
    def __init__(self, parent):
        #super().__init__(parent)
        super().__init__(parent, bg="mediumseagreen")
        self.pack(side='top', fill='x', ipady=10)  # Top bar with fixed height

        self.create_widgets()

    def create_widgets(self):
        # Example widgets for the top bar
        label = ttk.Label(self, text="Top Bar", anchor="center")
        button = ttk.Button(self, text="Logout")

        # Layout
        label.pack(side="left", padx=10)
        button.pack(side="right", padx=10)


class Menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="lightblue")
        self.place(x=0, y=50, relwidth=0.2, relheight=0.9)  # Adjust to avoid overlapping with TopBar

        self.parent = parent  # Save reference to the main app
        self.create_widget()

    def create_widget(self):
        self.treeview = ttk.Treeview(self)
        self.treeview.pack(fill='both', expand=True, padx=0, pady=0)

        # Adding items to the treeview
        self.treeview.insert('', '0', '11', text='Setup')
        self.treeview.insert('', '1', '12', text='Assets')
        self.treeview.insert('', '2', '13', text='Reports')
        self.treeview.insert('', '3', '14', text='User Management')

        # Adding sub-items
        self.treeview.insert('11', 'end', '11-1', text='System Configuration')

        self.treeview.insert('12', 'end', '12-1', text='Add Asset Item')
        self.treeview.insert('12', 'end', '12-2', text='Modify Asset Record')
        self.treeview.insert('12', 'end', '12-3', text='Add AMC Detail')

        self.treeview.insert('13', 'end', '13-1', text='Full List of Assets')
        self.treeview.insert('13', 'end', '13-2', text='List of Items Expiring AMC')
        self.treeview.insert('13', 'end', '13-3', text='List of Items AMC Recently Renewed')
        self.treeview.insert('13', 'end', '13-4', text='List of Users')

        self.treeview.insert('14', 'end', '14-1', text='Add New User')
        self.treeview.insert('14', 'end', '14-2', text='Edit User')
        self.treeview.insert('14', 'end', '14-3', text='Deactivate User')

        # Bind the treeview selection
        self.treeview.bind("<<TreeviewSelect>>", self.on_tree_item_click)

    def on_tree_item_click(self, event):
        # Get selected item
        selected_item = self.treeview.selection()[0]
        item_text = self.treeview.item(selected_item, "text")
        iid=self.treeview.focus()

        # Update the main frame content
        self.parent.main.update_content(iid,item_text)

class Main(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        # style = ttk.Style()
        # style.configure("Custom.TFrame", background="red")  # Custom background color


        self.place(relx=0.203, y=50, relwidth=0.85, relheight=0.9)  # Adjust to avoid overlapping with TopBar

        self.current_label = None  # To hold reference to the current content

        # Initial content
        self.update_content('00',"Welcome to the Main Area")

    def update_content(self, iid,text):
        # Clear previous content
        for widget in self.winfo_children():
            widget.destroy()

        match iid:
            case '14-1':
                UserCreation(self,text)
            case '12-1':
                AddAssetItem(self,text)
            case '12-3':
                AddAMCDetail(self, text)
            case '13':
                print("Case 3")
            case _:
                SecondaryUI(self,text)


    def clear_content(self):
        # Clear the content when the close button is clicked
        for widget in self.winfo_children():
            widget.destroy()
        self.update_content("Main Area Cleared")


App('Class Based App', (600, 600))