import math
import re
import tkinter as tk
from typing import List


class Calculator:
    def __init__(self, app: tk.Tk, label: tk.Label, display: tk.Entry, buttons: List[List[tk.Button]]):
        self.app = app
        self.label = label
        self.display = display
        self.buttons = buttons

    def start(self):
        self.config_buttons()
        self.config_display()
        self.app.mainloop()

    def config_buttons(self):
        buttons = self.buttons
        for row_value in buttons:
            for buttons in row_value:
                buttons_txt = buttons['text']
                if buttons_txt == 'C':
                    buttons.bind('<Button-1>', self.clear)
                    buttons.config(bg='#EA4335',fg='black')
                if buttons_txt in '0123456789.+-/*^()':
                    buttons.bind('<Button-1>', self.add_txt_to_display)
                if buttons_txt in '=':
                    buttons.bind('<Button-1>', self.calculate)
                    buttons.config(bg='#4785F4', fg='black')

    def config_display(self):
        self.display.bind('<Return>', self.calculate)
        self.display.bind('<KP_Enter>', self.calculate)


    def fix_text(self, text):
        # Substitui tudo que nao for 0123456789.+-/*^()
        text = re.sub(r'[^\d./*_+^e()]', r'', text, 0)
        # Substitui operadores repetidos para apenaaas 1
        text = re.sub(r'([.+/-^])\1+', r'\1', text, 0)
        # Substitui () ou *() para nada
        text = re.sub(r'\*?\(\)', '', text)
        return text

    def clear(self, event=None  ):
        self.display.delete('0', 'end')

    def add_txt_to_display(self, event=None):
        self.display.insert('end', event.widget['text'])

    def calculate(self, event=None):
        fixed_text = self.fix_text(self.display.get())
        equations = self.get_equations(fixed_text)

        try:
            if len(equations) == 1:
                result = eval(self.fix_text(equations[0]))
            else:
                result = eval(self.fix_text(equations[0]))
                for equations in equations[1:]:
                    result = math.pow(result, eval(self.fix_text(equations)))
            self.display.delete(0,'end')
            self.display.insert('end',result)
            self.label.config(text=f'{fixed_text} = {result}')
        except OverflowError:
            self.label.config(text='Não consegui realizar a conta')
        except Exception:
            self.label.config(text='Conta invalida')

    def get_equations(self, text):
        return re.split(r'\^', text, 0)