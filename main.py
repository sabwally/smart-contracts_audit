import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
from tkinter import Menu
import codecs

from tkinter import ttk

import tkinter.scrolledtext as st

from solidity import audit_sol as solidity


def open_file():
    filepath = askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if not filepath:
        return
    with codecs.open(filepath, "r", "utf-8") as input_file:
        txt_edit_in.delete("1.0", tk.END)
        text = input_file.read()
        txt_edit_in.insert(tk.END, text)
    window.title(f"Проверка смарт-контрактов - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
    )
    if not filepath:
        return
    with codecs.open(filepath, "w", "utf-8") as output_file:
        text = txt_edit_out.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Проверка смарт-контрактов - {filepath}")


def go():
    text = txt_edit_in.get("1.0", tk.END)
    ask = messagebox.askquestion('Страт проверки...', 'Welcome to Solidity!\nНачать проверку?')
    if ask == 'yes':
        program = solidity.audit(text)
        txt_edit_out.delete("1.0", tk.END)
        txt_edit_out.insert(tk.END, program)


def click():
    f = codecs.open('help.txt', "r", "utf-8")
    text = f.read()
    f.close()
    re = tk.Toplevel()
    re.title("HELP")
    re.geometry("900x450")
    text_area = st.ScrolledText(re, width=100, height=20, font='Times 12')
    text_area.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    text_area.insert(tk.INSERT, text)
    text_area.configure(state='disabled')


def save_l():
    text = ''
    for line in table.get_children():
        row = ''
        for value in table.item(line)['values']:
            row += value + '|'
        row = row[:-1]
        text += row + '\n'
    f = codecs.open('IniChecklist.txt', "w", "utf-8")
    f.write(text)
    f.close()


def delete_l():
    answer = messagebox.askyesno(
        title="Подтвердите действие",
        message="Удалит выбранные данные?")
    if answer:
        row_id = table.focus()
        table.delete(row_id)
        save_l()


class W_add(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.frm_form = tk.Frame(self, relief=tk.SUNKEN, borderwidth=3)

        self.frm_form.pack()

        self.lbl_code = tk.Label(self.frm_form, text="Код:")
        self.ent_code = tk.Entry(self.frm_form, width=100)
        self.lbl_code.grid(row=0, column=0, sticky="e")
        self.ent_code.grid(row=0, column=1)

        self.lbl_name = tk.Label(self.frm_form, text="Название:")
        self.ent_name = tk.Entry(self.frm_form, width=100)
        self.lbl_name.grid(row=1, column=0, sticky="e")
        self.ent_name.grid(row=1, column=1)

        self.lbl_check = tk.Label(self.frm_form, text="Проверять?:")
        self.ent_check = tk.Entry(self.frm_form, width=100)
        self.lbl_check.grid(row=2, column=0, sticky="e")
        self.ent_check.grid(row=2, column=1)

        self.lbl_path = tk.Label(self.frm_form, text="Файл для внешней проверки:")
        self.ent_path = tk.Entry(self.frm_form, width=100)
        self.lbl_path.grid(row=3, column=0, sticky=tk.E)
        self.ent_path.grid(row=3, column=1)

        self.lbl_content = tk.Label(self.frm_form, text="Описание уязвимости:")
        self.ent_content = tk.Entry(self.frm_form, width=100)
        self.lbl_content.grid(row=4, column=0, sticky=tk.E)
        self.ent_content.grid(row=4, column=1)

        self.frm_buttons = tk.Frame(self)
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

        self.btn_s = tk.Button(self.frm_buttons, text="Сохранить", command=self.save_add)
        self.btn_s.pack(side=tk.RIGHT, padx=10, ipadx=10)

        self.btn_cancel = tk.Button(self.frm_buttons, text="Отмена", command=self.destroy)
        self.btn_cancel.pack(side=tk.RIGHT, ipadx=10)

    def save_add(self):
        table.insert('', 'end', values=(self.ent_code.get(), self.ent_name.get(), self.ent_check.get(), self.ent_path.get(), self.ent_content.get()))
        save_l()
        self.destroy()


class W_change(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.frm_form = tk.Frame(self, relief=tk.SUNKEN, borderwidth=3)

        self.frm_form.pack()

        self.lbl_code = tk.Label(self.frm_form, text="Код:")
        self.ent_code = tk.Entry(self.frm_form, width=100, justify="left")
        self.lbl_code.grid(row=0, column=0, sticky="e")
        self.ent_code.grid(row=0, column=1)

        self.lbl_name = tk.Label(self.frm_form, text="Название:")
        self.ent_name = tk.Entry(self.frm_form, width=100)
        self.lbl_name.grid(row=1, column=0, sticky="e")
        self.ent_name.grid(row=1, column=1)

        self.lbl_check = tk.Label(self.frm_form, text="Проверять?:")
        self.ent_check = tk.Entry(self.frm_form, width=100)
        self.lbl_check.grid(row=2, column=0, sticky="e")
        self.ent_check.grid(row=2, column=1)

        self.lbl_path = tk.Label(self.frm_form, text="Файл для внешней проверки:")
        self.ent_path = tk.Entry(self.frm_form, width=100)
        self.lbl_path.grid(row=3, column=0, sticky=tk.E)
        self.ent_path.grid(row=3, column=1)

        self.lbl_content = tk.Label(self.frm_form, text="Описание уязвимости:")
        self.ent_content = tk.Entry(self.frm_form, width=100)
        self.lbl_content.grid(row=4, column=0, sticky=tk.E)
        self.ent_content.grid(row=4, column=1)

        self.lst = table.focus()
        self.contents = table.item(self.lst)
        self.items = self.contents['values']

        self.ent_code.insert(tk.END, self.items[0])
        self.ent_name.insert(tk.END, self.items[1])
        self.ent_check.insert(tk.END, self.items[2])
        self.ent_path.insert(tk.END, self.items[3])
        self.ent_content.insert(tk.END, self.items[4])

        self.frm_buttons = tk.Frame(self)
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

        self.btn_s = tk.Button(self.frm_buttons, text="Сохранить", command=self.save_change)
        self.btn_s.pack(side=tk.RIGHT, padx=10, ipadx=10)

        self.btn_cancel = tk.Button(self.frm_buttons, text="Отмена", command=self.destroy)
        self.btn_cancel.pack(side=tk.RIGHT, ipadx=10)

    def save_change(self):
        row_id = table.focus()
        table.item(row_id, text="", values=(self.ent_code.get(), self.ent_name.get(), self.ent_check.get(), self.ent_path.get(), self.ent_content.get()))
        save_l()
        self.destroy()


def add_l():
    wn = W_add()


def change_l():
    wn = W_change()


def bye():
    window.destroy()


window = tk.Tk()
window.title("Проверка смарт-контрактов")
window.geometry("1200x650")
window.resizable(False, False) #!

notebook = ttk.Notebook(window)
notebook.pack(pady=10, expand=True)


frame1 = tk.Frame(notebook, width=400, height=280)
frame2 = tk.Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

notebook.add(frame1, text='Код смарт-контракта')
notebook.add(frame2, text='Настройка проверок уязвимостей')

frame1.rowconfigure(0, minsize=10, weight=1)
frame1.rowconfigure(1, minsize=10, weight=1)
frame1.columnconfigure(0, minsize=10, weight=1)
frame1.columnconfigure(1, minsize=10, weight=1)
frame1.rowconfigure(2, minsize=10, weight=1)
frame1.columnconfigure(2, minsize=10, weight=1)

fr_buttons = tk.Frame(frame1)
fr_text = tk.Frame(frame1)
fr_out = tk.Frame(frame1)
lbl_in = tk.Label(fr_text, text="Исходный код контракта:", fg="red", font='Times 12')
lbl_out = tk.Label(fr_text, text="Скорректированный код контракта:", fg="red", font='Times 12')
txt_edit_in = st.ScrolledText(fr_text, width=70, height=30)
#txt_edit_in.resizable(true, true)
txt_edit_out = st.ScrolledText(fr_text, width=70, height=30)
#txt_edit_out.resizable(true, true)
btn_open = tk.Button(fr_buttons, text="Выбрать контракт", command=open_file)
btn_save = tk.Button(fr_out, text="Сохранить новый контракт как...", command=save_file)
btn_start = tk.Button(fr_buttons, text="Начать проверку", command=go)
btn_end = tk.Button(fr_out, text="Выход", command=bye)

menu = Menu(window)
doc = Menu(menu, tearoff=0)
ffile = Menu(menu, tearoff=0)

ffile.add_command(label='Выбрать контракт', command=click)
ffile.add_command(label='Проверить контракт', command=click)
ffile.add_command(label='Сохранить новый контракт', command=click)
ffile.add_command(label='Выход', command=click)
menu.add_cascade(label='Файл', menu=ffile)

doc.add_command(label='HELP', command=click)
menu.add_cascade(label='Информация о программе', menu=doc)

window.config(menu=menu)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_start.grid(row=0, column=1, sticky="ew", padx=5)
lbl_in.grid(row=0, column=0, sticky="n", padx=5)
lbl_out.grid(row=0, column=1, sticky="n", padx=5)
txt_edit_in.grid(row=1, column=0, sticky="ew", padx=5)
txt_edit_out.grid(row=1, column=1, sticky="ew", padx=5)
btn_save.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_end.grid(row=0, column=1, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="n")
fr_text.grid(row=1, column=0, sticky="n")
fr_out.grid(row=2, column=0, sticky="n")


f = codecs.open('IniChecklist.txt', "r", "utf-8")
text = f.read()
f.close()

lst = []
for str in text.splitlines():
    row = str.split('|')
    lst.append(row)

heads = ['Код', 'Название', 'Проверять?', 'Файл для внешней проверки', 'Описание уязвимости']
table = ttk.Treeview(frame2, show='headings')
table['columns'] = heads

for header in heads:
            table.heading(header, text=header, anchor=tk.CENTER)
            table.column(header, anchor="w", stretch=False)

for row in lst:
    table.insert('',tk.END, values=row)

table.column('Код', minwidth=0, width=100)
table.column('Название', minwidth=0, width=400)
table.column('Проверять?', minwidth=0, width=75)
table.column('Файл для внешней проверки', minwidth=0, width=420)
table.column('Описание уязвимости', minwidth=0, width=1000)

scrolly = ttk.Scrollbar(frame2, command=table.yview)
table.configure(yscrollcommand=scrolly.set)
scrolly.pack(side=tk.RIGHT, fill=tk.Y)

scrollx = ttk.Scrollbar(frame2,orient='horizontal', command=table.xview)
table.configure(xscrollcommand=scrollx.set)
scrollx.pack(side=tk.BOTTOM, fill=tk.X)

table.pack(expand=tk.YES, fill=tk.BOTH)

fr2_but = tk.Frame(frame2)
fr2_but.pack(fill=tk.X, ipadx=5, ipady=5)

btn_delete = tk.Button(fr2_but, text="Удалить", command=delete_l)
btn_delete.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_add = tk.Button(fr2_but, text="Добавить", command=add_l)
btn_add.pack(side=tk.RIGHT, ipadx=10)

btn_change = tk.Button(fr2_but, text="Изменить", command=change_l)
btn_change.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()
