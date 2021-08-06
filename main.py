# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import create_form
import fill_form
from tkinter import *
from tkdocviewer import *
from tkPDFViewer import tkPDFViewer as pdf






###
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_form.create_simple_form()
    fill_form.create_overlay()
    fill_form.merge_pdfs('simple_form_overlay.pdf', 'simple_form.pdf', 'merged_form.pdf')


    def clicked():
        res = "Привет {}".format(txt.get())
        lbl.configure(text=res)





    window = Tk()
    window.geometry('1000x800')
    window.title("Добро пожаловать")
    menu = Menu(window)
    new_item = Menu(menu, tearoff=0)
    new_item.add_command(label='Заполнить')
    new_item.add_separator()
    new_item.add_command(label='Новый шаблон')

    new_item.add_command(label='Новый шаблон', command=clicked)

    menu.add_cascade(label='Файл', menu=new_item)
    window.config(menu=menu)
    lbl = Label(window, text="Привет")
    lbl.grid(column=0, row=0)
    txt = Entry(window, width=10)
    txt.grid(column=1, row=0)
    btn = Button(window, text="Клик!", command=clicked)
    btn.grid(column=2, row=0)
    window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
