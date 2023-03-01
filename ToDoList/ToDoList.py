import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3


class ToDoList():
    def __init__(self, master):
        self.todo_window = tk.Toplevel(master)
        self.todo_window.title('To do list')
        self.todo_window.iconbitmap('ToDoList/logo/Todolist.ico')
        self.todo_window.geometry('480x400')
        self.todo_window.minsize(480, 400)
        self.todo_window.maxsize(480, 400)


        self.conn = sqlite3.connect('ToDoList/ToDoList.db')
        self.cur= self.conn.cursor()
        self.cur.execute('create table if not exists tasks (title text)')

        self.create_widgets()

    
    def create_widgets(self):
        global new_logo

        logo= Image.open('ToDoList/logo/ToDoList.png')
        resized_logo = logo.resize((420, 110))
        new_logo = ImageTk.PhotoImage(resized_logo)
        self.logo_label= tk.Label(self.todo_window, image=new_logo)



        self.input_label = tk.Label(self.todo_window, text='Enter the task: ', font=('arial', 12))
        self.task_entry = tk.Entry(self.todo_window, width=23)

        self.add_button = tk.Button(self.todo_window, text='Add task', font=('arial', 12), width=15, command=self.add_task)
        self.delete_button = tk.Button(self.todo_window, text='Delete', font=('arial', 12), width=15, command=self.delete_task)
        self.delete_all_button = tk.Button(self.todo_window, text='Delete All', font=('arial', 12), width=15, command=self.delete_all)
        self.exit_button = tk.Button(self.todo_window, text='Exit', font=('arial', 12), width=15, command=self.exit)


        self.tasks_list = tk.Listbox(self.todo_window, height=16, width=40)


        #Place geometry
        self.logo_label.place(x=25, y=1)
        self.input_label.place(x=50, y=110)
        self.task_entry.place(x=50, y=140)
        self.add_button.place(x=50, y=170)
        self.delete_button.place(x=50, y=210)
        self.delete_all_button.place(x=50, y=250)
        self.exit_button.place(x=50, y =290)
        self.tasks_list.place(x=220, y = 110)    

        self.list_update()        


    def add_task(self):
        task = self.task_entry.get()
        if len(task) > 0:
            self.cur.execute('INSERT INTO Tasks VALUES(:title)',
            {
                'title':self.task_entry.get(),
            })

            self.conn.commit()
            self.task_entry.delete(0, tk.END)
        
        if len(task) == 0:
            messagebox.showinfo('Empty Entry', 'Enter Task Name')
        
        self.list_update()



    def delete_task(self):
        selected_task = self.tasks_list.get(self.tasks_list.curselection())
        task = ''
        for item in selected_task:
            task = '' + item
        self.cur.execute('DELETE FROM Tasks WHERE title = ?', (task,))
        self.conn.commit()

        self.list_update()

    def delete_all(self):
        mb = messagebox.askyesno('Delete All','Are you sure?')
        if mb== True:
            self.cur.execute('DELETE FROM Tasks')
            self.conn.commit()
        
        self.list_update()


    def exit(self):
        self.destroy()


    def list_update(self):
        self.tasks_list.delete(0, tk.END)
        self.cur.execute('SELECT title FROM Tasks')
        for row in self.cur:
            self.tasks_list.insert('end', row)        




if __name__ == '__main__':
    app = ToDoList()
    app.mainloop()

