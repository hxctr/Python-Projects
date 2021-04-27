from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title('Pies a metros')
window.configure(background='sky blue')
window.geometry('320x220')
window.resizable(width=False, height=False)

def convert():
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_val.set('%.4f' % meter)

def clear():
    ft_val.set('')
    mt_val.set('')
    


ft_label = Label(window, text='Feet', bg='purple', fg='white', width=14)
ft_label.grid(column=0, row=0, padx=15, pady=15)

ft_val = DoubleVar()
ft_entry = Entry(window,textvariable=ft_val, width=14)
ft_entry.grid(column=1, row=0)
ft_entry.delete(0, 'end')

mt_label = Label(window, text='Meter', bg='purple', fg='white', width=14)
mt_label.grid(column=0, row=1)

mt_val = DoubleVar()
mt_entry = Entry(window,textvariable=mt_val, width=14)
mt_entry.grid(column=1, row=1, pady=30)
mt_entry.delete(0, 'end')

btnConvert = Button(window,text='Convert', bg='blue', fg='white', width=14, command=convert)
btnConvert.grid(column=0, row=3, padx=15)

btnClear = Button(window,text='Clear', bg='Black', fg='white', width=14, command=clear)
btnClear.grid(column=1, row=3, padx=15)

















window.mainloop()

