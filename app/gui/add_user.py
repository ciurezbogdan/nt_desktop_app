import tkinter as tk

# from threading import Thread
# from app.data.base import add_user
labels = 'First Name', 'Last Name', 'Email', 'Role'


# class AddUserFrame(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         super(AddUserFrame, self).__init__(*args, **kwargs)
#
#         self.first_name = tk.Entry
#         self.last_name = None
#         self.email = None
#         self.role = None
#         self.add_user_btn = tk.Button(self, text='Add User', command=add_user)


def fetch(entries):
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        print('%s: "%s"' % (field, text))


def makeform(roots, fieldss):
    entries = []
    for field in fieldss:
        row = tk.Frame(roots)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries


# def widget_add_user():


def add_user():
    root = tk.Tk()
    root.winfo_toplevel().title('Add User')
    ents = makeform(root, labels)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = tk.Button(root, text='Show', command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()

