import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from SPDb import SPDb

class SPDbGuiCtk(customtkinter.CTk):

    def __init__(self, dataBase= SPDb()):
        super().__init__()
        self.db = dataBase

        self.title('Dream Team Creator')
        self.geometry('1800x850')
        self.config(bg='#99ccff')
        self.resizable(False, False)

        self.font1 = ('Arial', 20, 'bold')
        self.font2 = ('Arial', 12, 'bold')

        # Data Entry Form
        # 'ID' Label and Entry Widgets
        self.number_label = self.newCtkLabel('Jersey Number')
        self.number_label.place(x=50, y=110)
        self.number_entry = self.newCtkEntry()
        self.number_entry.place(x=350, y=110)

        # 'Name' Label and Entry Widgets
        self.name_label = self.newCtkLabel('Player Name')
        self.name_label.place(x=50, y=170)
        self.name_entry = self.newCtkEntry()
        self.name_entry.place(x=350, y=170)

        # 'Role' Label and Combo Box Widgets
        self.position_label = self.newCtkLabel('Player Position')
        self.position_label.place(x=50, y=230)
        self.position_cboxVar = StringVar()
        self.position_cboxOptions = ['Point Guard', 'Shooting Guard', 'Small Forward', 'Power Forward', 'Center']
        self.position_cbox = self.newCtkComboBox(options=self.position_cboxOptions, 
                                    entryVariable=self.position_cboxVar)
        self.position_cbox.place(x=350, y=230)

        # 'Gender' Label and Combo Box Widgets
        self.role_label = self.newCtkLabel('Team Role')
        self.role_label.place(x=50, y=290)
        self.role_cboxVar = StringVar()
        self.role_cboxOptions = ['Starter', 'Bench', 'Reserve']
        self.role_cbox = self.newCtkComboBox(options=self.role_cboxOptions, 
                                    entryVariable=self.role_cboxVar)
        self.role_cbox.place(x=350, y=290)

        # 'Status' Label and Combo Box Widgets
        self.minutes_label = self.newCtkLabel('Playing Minutes')
        self.minutes_label.place(x=50, y=350)
        self.minutes_entry = self.newCtkEntry()
        self.minutes_entry.place(x=350, y=350)


        self.add_button = self.newCtkButton(text='Add Player',
                                onClickHandler=self.add_entry,
                                fgColor='#05A312',
                                hoverColor='#00850B',
                                borderColor='#05A312')
        self.add_button.place(x=50,y=470)

        self.new_button = self.newCtkButton(text='New Player',
                                onClickHandler=lambda:self.clear_form(True),
                                fgColor= '#9900ff',
                                hoverColor= '#4c0080',
                                borderColor= '#9900ff')
        self.new_button.place(x=420,y=470)

        self.update_button = self.newCtkButton(text='Change Player',
                                    onClickHandler=self.update_entry,
                                    fgColor= '#ffa500',
                                    hoverColor= '#cc8500',
                                    borderColor= '#ffa500')
        self.update_button.place(x=420,y=540)

        self.delete_button = self.newCtkButton(text='Remove Player',
                                    onClickHandler=self.delete_entry,
                                    fgColor='#E40404',
                                    hoverColor='#AE0000',
                                    borderColor='#E40404')
        self.delete_button.place(x=50,y=540)

        self.import_button = self.newCtkButton(text='Import from CSV', 
                                    onClickHandler=self.import_to_csv,
                                    fgColor= '#999966',
                                    hoverColor= '#8a8a5c',
                                    borderColor= '#999966')
        self.import_button.place(x=240, y=730) 

        self.export_button = self.newCtkButton(text='Export to CSV',
                                    onClickHandler=self.export_to_csv,
                                    fgColor= '#808080',
                                    hoverColor= '#666666',
                                    borderColor= '#808080')
        self.export_button.place(x=50,y=650)

        self.export_json_button = self.newCtkButton(text= 'Export to JSON',
                                    onClickHandler= self.export_to_json,
                                    fgColor= '#d2b48c',
                                    hoverColor= '#bf935a',
                                    borderColor= '#d2b48c')
        self.export_json_button.place(x=420, y=650)

        # Tree View for Database Entries
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('Treeview', 
                        font=self.font2, 
                        foreground='#fff',
                        background='#0066ff',
                        fieldlbackground='#313837')

        self.style.map('Treeview', background=[('selected', '#1A8F2D')])

        self.tree = ttk.Treeview(self, height=15)
        self.tree['columns'] = ('Jersey Number', 'Player Name', 'Position', 'Team Role', 'Playing Minutes')
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('Jersey Number', anchor=tk.CENTER, width=10)
        self.tree.column('Player Name', anchor=tk.CENTER, width=150)
        self.tree.column('Position', anchor=tk.CENTER, width=150)
        self.tree.column('Team Role', anchor=tk.CENTER, width=10)
        self.tree.column('Playing Minutes', anchor=tk.CENTER, width=150)

        self.tree.heading('Jersey Number', text='Jersey Number')
        self.tree.heading('Player Name', text='Player Name')
        self.tree.heading('Position', text='Position')
        self.tree.heading('Team Role', text='Team Role')
        self.tree.heading('Playing Minutes', text='Playing Minutes')

        self.tree.place(x=750, y=150, width=1000, height=550)
        self.tree.bind('<ButtonRelease>', self.read_display_data)

        self.add_to_treeview()

    # new Label Widget
    def newCtkLabel(self, text = 'CTK Label'):
        widget_Font=self.font1
        widget_TextColor='#0066ff'
        widget_BgColor='#99ccff'

        widget = customtkinter.CTkLabel(self, 
                                    text=text,
                                    font=widget_Font, 
                                    text_color=widget_TextColor,
                                    bg_color=widget_BgColor)
        return widget

    # new Entry Widget
    def newCtkEntry(self, text = 'CTK Label'):
        widget_Font=self.font1
        widget_TextColor='#000'
        widget_FgColor='#FFF'
        widget_BorderColor='#0C9295'
        widget_BorderWidth=2
        widget_Width=350

        widget = customtkinter.CTkEntry(self,
                                    font=widget_Font,
                                    text_color=widget_TextColor,
                                    fg_color=widget_FgColor,
                                    border_color=widget_BorderColor,
                                    border_width=widget_BorderWidth,
                                    width=widget_Width)
        return widget

    # new Combo Box Widget
    def newCtkComboBox(self, options=['DEFAULT', 'OTHER'], entryVariable=None):
        widget_Font=self.font1
        widget_TextColor='#000'
        widget_FgColor='#FFF'
        widget_DropdownHoverColor='#0C9295'
        widget_ButtonColor='#0C9295'
        widget_ButtonHoverColor='#0C9295'
        widget_BorderColor='#0C9295'
        widget_BorderWidth=2
        widget_Width=350
        widget_Options=options

        widget = customtkinter.CTkComboBox(self,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        border_color=widget_BorderColor,
                                        width=widget_Width,
                                        variable=entryVariable,
                                        values=options,
                                        state='readonly')
        
        # set default value to 1st option
        widget.set(options[0])

        return widget

    # new Button Widget
    def newCtkButton(self, text = 'CTK Button', onClickHandler=None, fgColor='#161C25', hoverColor='#FF5002', bgColor='#99ccff', borderColor='#F15704'):
        widget_Font=self.font1
        widget_TextColor='#FFF'
        widget_FgColor=fgColor
        widget_HoverColor=hoverColor
        widget_BackgroundColor=bgColor
        widget_BorderColor=borderColor
        widget_BorderWidth=10
        widget_Cursor='hand2'
        widget_CornerRadius=15
        widget_Width=260
        widget_Function=onClickHandler

        widget = customtkinter.CTkButton(self,
                                        text=text,
                                        command=widget_Function,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        hover_color=widget_HoverColor,
                                        bg_color=widget_BackgroundColor,
                                        border_color=widget_BorderColor,
                                        border_width=widget_BorderWidth,
                                        cursor=widget_Cursor,
                                        corner_radius=widget_CornerRadius,
                                        width=widget_Width)
       
        return widget

    # Handles
    def add_to_treeview(self):
        players = self.db.fetch_player()
        self.tree.delete(*self.tree.get_children())
        for player in players:
            print(players)
            self.tree.insert('', END, values=player)

    def clear_form(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
            self.tree.focus('')
        self.number_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.position_cboxVar.set('Point Guard')
        self.role_cboxVar.set('Starter')
        self.minutes_entry.delete(0, END)

    def read_display_data(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            row = self.tree.item(selected_item)['values']
            self.clear_form()
            self.number_entry.insert(0, row[0])
            self.name_entry.insert(0, row[1])
            self.position_cboxVar.set(row[2])
            self.role_cboxVar.set(row[3])
            self.minutes_entry.insert(0, row[4])
        else:
            pass

    def add_entry(self):
        number=self.number_entry.get()
        name=self.name_entry.get()
        position=self.position_cboxVar.get()
        role=self.role_cboxVar.get()
        minutes=self.minutes_entry.get()

        if not (number and name and position and role and minutes):
            messagebox.showerror('Error', 'Enter all fields.')
        elif self.db.id_exists(number):
            messagebox.showerror('Error', 'Jersey number already given')
        else:
            self.db.insert_player(number, name, position, role, minutes)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been inserted')

    def delete_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose a player to delete')
        else:
            number = self.number_entry.get()
            self.db.delete_player(number)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Player has been removed')

    def update_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose a player to change')
        else:
            number=self.number_entry.get()
            name=self.name_entry.get()
            position=self.position_cboxVar.get()
            role=self.role_cboxVar.get()
            minutes=self.minutes_entry.get()
            self.db.update_player(name, position, role, minutes, number)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Player has been updated')

    def import_to_csv(self):
        filename = filedialog.askopenfilename(title= "Select A File" , filetypes=[("Excel files", "*.csv")])
        self.db.import_csv(filename)
        self.add_to_treeview()
        messagebox.showinfo('Success', f'Data has been imported')

    def export_to_csv(self):
        self.db.export_csv()
        messagebox.showinfo('Success', f'Data exported to {self.db.dbName}')

    def export_to_json(self):
        self.db.export_json()
        messagebox.showinfo('Success', f'Data exported to SPDb.json')






