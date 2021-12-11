import tkinter as tk
import tkinter.scrolledtext as st
import os as s
from solidity import vulnerability as v

import codecs


def audit(text):
    report = "Отчёт:\n"
    version = []
    i_ver = -1
    program = ''
    code_str = ""

    # заменяем комментарии
    text = v.del_comment(text)
    # преобразуем пробелы
    # text = v.del_space(text)

    # Уязвимости:
    report, text, i_ver = v.sol_version(text, report, version, i_ver)
    if i_ver != -1:

        f = codecs.open('IniChecklist.txt', "r", "utf-8")
        try:
            text_to_check = f.read()
        finally:
            f.close()

        # проверяем ли эту уязвимость yes/no
        lst_to_check = []
        for str_to_check in text_to_check.splitlines():
            row = str_to_check.split('|')
            lst_to_check.append(row)

        for l in lst_to_check:
            if l[2] == 'yes':
                if l[0] == 'overflow':
                    if int(version[1]) < 8 and int(version[0]) == 0:
                        report, text = v.overflow(text, report, version, i_ver)
                elif l[0] == 'def_visibility':
                    report, text = v.def_visibility(text, report, version, i_ver)
                elif l[0] == 'self_destruct':
                    report, text = v.self_destruct(text, report, version, i_ver)
                elif l[0] == 'delegatecall':
                    report, text = v.delegatecall(text, report, version, i_ver)
                elif l[0] == 'callreentrancy':
                    report, text = v.callreentrancy(text, report, version, i_ver)
                elif l[0] == 'braces':
                    report, text = v.braces(text, report, version, i_ver)
                elif l[0] == 'def_notifcall':
                    report, text = v.def_notifcall(text, report, version, i_ver)
                elif l[0] == 'non_init_var':
                    report, text = v.non_init_var(text, report, version, i_ver)
                else:
                    # запуск внешней проверки динамически
                    try:
                        # открываем файл с кодом проверки и считываем содержимое
                        with open(s.path.abspath(l[3]), 'r') as f:
                            code_str = f.read()
                    except Exception as e:
                        report += '\nДля проверки ... файл с кодом проверки не найден. Проверьте наличие файла и скорректируйте настройки. ' + str(
                            e)
                    # сохраняем измененный код и отчет через файл
                    code_str = code_str + '\nf = open(s.path.abspath("tmp_text.my"), "w+")\n' + 'f.write(text_out)\nf.close\n'
                    code_str = code_str + '\nf = open(s.path.abspath("tmp_report.my"), "w+")\n' + 'f.write(report)\nf.close\n'
                    try:
                        code = compile(code_str, 'test_chk.py', 'exec')
                    except Exception as e:
                        report += '\nДля проверки ... код не может быть скомпилирован. Исправте код ' + str(e)
                    try:
                        exec(code, {'text_in': text, 's': s})
                        with open(s.path.abspath('tmp_text.my'), 'r') as f:
                            text = f.read()
                        s.remove(s.path.abspath('tmp_text.my'))
                        # f.seek(0)
                        with open(s.path.abspath('tmp_report.my'), 'r') as f:
                            report += '\n' + f.read()
                        s.remove(s.path.abspath('tmp_report.my'))
                        # f.seek(0)
                    except Exception as e:
                        report += '\nПри выполнении проверки ... произошла ошибка ' + str(e)

    # восстанавливаем комментарии
    text = v.repair_comment(text)
    program = text

    re = tk.Toplevel()
    re.title("Отчёт")
    re.geometry("1200x500")
    # label = tk.Label(re, text=report, font='Times 12', justify=tk.LEFT)
    text_area = st.ScrolledText(re, width=140, height=25, font='Times 12')
    text_area.grid(column=0, pady=10, padx=10)
    text_area.insert(tk.INSERT, report)
    text_area.configure(state='disabled')
    # label.pack()
    return program
