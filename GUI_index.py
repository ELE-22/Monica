from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from webscrap_index import scrapping
from webscrap_index import save_result

# create the root window
root = Tk()
root.title('Web scraping')
root.iconbitmap(r'.\imagenes\pc.ico')
root.geometry('300x150')
root.config(bg='black')

# search file
file_label = Label(root, text="Archivo donde se optiene los tags")
file_label.pack()
file_label.config(fg="white", bg="green", font=("Verdana", 8))
file_label.place(relx=0.01, rely=0.01, relwidth=0.8, relheight=0.1)
display = Entry(root)
display.place(relx=0.003, rely=0.13, relwidth=0.5, relheight=0.14)

filetypes = (
    ('Excel Workbook', '*.xlsx'),
    ('All files', '*.*')
)
path_open_file = list()


def clear_display():
    if len(display.get()):
        display.delete(0, END)


def select_file():
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    clear_display()
    display.insert(0, filename)
    path_open_file.insert(0, filename)


def save_file():
    save = fd.asksaveasfile(
        title='Save file',
        initialdir='/',
        defaultextension='.xlsx',
        filetypes=filetypes)

    # funcion para crear el archivo
    save_result(save.name)


def run():
    scrapping(path_open_file[0])


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
).place(relx=0.52, rely=0.13, relwidth=0.3, relheight=0.14)

# Run button
open_button1 = ttk.Button(root, text='RUN', command=run).place(relx=0.01, rely=0.40, relwidth=0.2, relheight=0.14)

# save button
open_button2 = ttk.Button(
    root,
    text='SAVE',
    command=save_file

).place(relx=0.35, rely=0.40, relwidth=0.2, relheight=0.14)

# run the application
root.mainloop()
