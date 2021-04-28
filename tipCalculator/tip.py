from tkinter import Tk, Radiobutton, Button, Label, StringVar, IntVar, Entry
#Para la importacion de arriba no es necesario declarar todos los widgets
#Basta con solo importar tkinter, pero no es una muy buena practica

class TipCalculator():
    
    def __init__(self):
        window = Tk()
        window.title('Calculadora de propinas')#Titulo de ventana
        window.configure(background='sky blue')#Color de fondo
        window.geometry('425x250')#Tamaño de ventana
        window.resizable(width=False, height=False)#Fijar la ventaña a su tamaño
        #-----------------------------------------------
        self.costoPlatillo = StringVar()
        self.porcentajePropina = IntVar()
        self.propina = StringVar()
        self.costoTotal = StringVar()
        #-----------------------------------------------
        lblTipPercent = Label(window, text='Porcentaje de propina', bg='black', fg='white')
        lblTipPercent.grid(column=0, row=0, padx=15, pady=15)
        
        lblCantidadFacturar = Label(window, text='Cantidad a cobrar', bg='black', fg='white')
        lblCantidadFacturar.grid(column=1, row=0, padx=15)
        
        txtCantidadFacturar = Entry(window,textvariable=self.costoPlatillo, width=14)
        txtCantidadFacturar.grid(column=2,row=0)
        
        rbtnCincoPorciento = Radiobutton(window, text='05%', variable=self.porcentajePropina, value=5)
        rbtnCincoPorciento.grid(column=0,row=1)
        rbtnDiezPorciento = Radiobutton(window, text='10%', variable=self.porcentajePropina, value=10)
        rbtnDiezPorciento.grid(column=0,row=2)
        rbtnQuincePorciento = Radiobutton(window, text='15%', variable=self.porcentajePropina, value=15)
        rbtnQuincePorciento.grid(column=0,row=3)
        rbtnVeintePorciento = Radiobutton(window, text='20%', variable=self.porcentajePropina, value=20)
        rbtnVeintePorciento.grid(column=0,row=4)
        rbtnVeintiCincoPorciento = Radiobutton(window, text='25%', variable=self.porcentajePropina, value=25)
        rbtnVeintiCincoPorciento.grid(column=0,row=5)
        rbtnTreintaPorciento = Radiobutton(window, text='30%', variable=self.porcentajePropina, value=30)
        rbtnTreintaPorciento.grid(column=0,row=6)
        
        lblCantidadPropina = Label(window,text='Cantidad de propina',bg='brown', fg='white')
        lblCantidadPropina.grid(column=1,row=3, padx=15)
        txtCantidadPropina = Entry(window,textvariable=self.propina, width=14)
        txtCantidadPropina.grid(column=2, row=3) 
        
        lblTotalCosto = Label(window, text='Cantidad Total', bg='blue', fg='white')
        lblTotalCosto.grid(column=1, row=5, padx=15)
        txtTotalCosot = Entry(window,textvariable=self.costoTotal, width=14)
        txtTotalCosot.grid(column=2, row=5)    
        
        btnCalcular = Button(window, text='Calcular', bg='green', fg='white', command=self.calcular)
        btnCalcular.grid(column=1,row=7, padx=15)
        
        btnLimpiar = Button(window, text='Limpiar', bg='green', fg='white', command='')
        btnLimpiar.grid(column=2,row=7)
        
        
        
        
        
        
        window.mainloop()#Funcion que ejecuta la ventana, sin esto no saldria la ventana

    def calcular(self):
        pre_tip = float(self.costoPlatillo.get())
        percentage = self.porcentajePropina.get() / 100
        tip_amount_txt = pre_tip * percentage
        self.propina.set(tip_amount_txt)
        
        final_bill = pre_tip * tip_amount_txt
        self.costoTotal.set(final_bill)
        
TipCalculator()