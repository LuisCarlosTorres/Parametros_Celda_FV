"""
Desarrollado por:
Luis Carlos Torres Vega, E-mail: luiscarlostv@ufps.edu.co
Andrea Paola Ardila Sanchez, E-mail: andreapaolaas@ufps.edu.co
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Configuración de la ventana de tkinter
ventana = Tk()                          # Crea la ventana
ventana.title("Solar cell modeling")    #Asigna el título de la ventana
ventana.iconbitmap('energia-solar.ico') #Asigna el icono de la ventana

#Posiciona la ventana en la mitad de la pantalla
ancho_ventana=1070  #850
alto_ventana=540
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.resizable(0,0)    #Impide que la ventana se pueda redimencionar

#Logos
Logo_U=tk.PhotoImage(file="Logo_UFPS.png")
Logo_U=Logo_U.subsample(2)
Logo_Ufps=ttk.Label(image=Logo_U,background="White")
Logo_Ufps.place(x=875, y=20)

#Obtener el valor actual de los slider
valor_actual_n = tk.DoubleVar()
valor_actual_T = tk.DoubleVar()
valor_actual_IL = tk.DoubleVar()
valor_actual_Ioo = tk.IntVar()

#Funciones para mostrar el valor del slider
def cambio_slider_n(event):
    valor_n.configure(text='{: .2f}'.format(valor_actual_n.get()))
def cambio_slider_T(event):
    valor_T.configure(text='{: .2f}'.format(valor_actual_T.get()))
def cambio_slider_IL(event):
    valor_IL.configure(text='{: .2f}'.format(valor_actual_IL.get()))
def cambio_slider_Io(event):
    valor_Ioo.configure(text=valor_actual_Ioo.get())

#Configuración inicial del slider 
slider_n = ttk.Scale(ventana, from_=1, to=2, orient='horizontal',  command=cambio_slider_n,variable=valor_actual_n, length=250)
slider_n.set(1)
slider_n.place(x=135,y=400)
slider_T = ttk.Scale(ventana, from_=-15, to=50, orient='horizontal', command=cambio_slider_T, variable=valor_actual_T, length=250)
slider_T.set(-15)
slider_T.place(x=135,y=450)
slider_IL = ttk.Scale(ventana, from_=0, to=8, orient='horizontal',  command=cambio_slider_IL,variable=valor_actual_IL, length=250)
slider_IL.place(x=560,y=400)
slider_Ioo = ttk.Scale(ventana, from_=-5, to=5, orient='horizontal', command=cambio_slider_Io, variable=valor_actual_Ioo, length=250)
slider_Ioo.place(x=560,y=450)

#Etiqueta correspondiente a la variable de cada slider
label_n = Label(ventana, text='n =',font=('Times', '12', 'bold italic'),background='white').place(x=25,y=400)
label_T = Label(ventana, text='T =',font=('Times', '12', 'bold italic'),background='white').place(x=25,y=450)
label_T = Label(ventana, text='°C',font=('Times', '12', 'bold italic'),background='white').place(x=103,y=450)
label_IL = Label(ventana, text='IL =',font=('Times', '12', 'bold italic'),background='white').place(x=465,y=400)
label_IL = Label(ventana, text='A',font=('Times', '12', 'bold italic'),background='white').place(x=535,y=400)
label_Ioo = Label(ventana, text='Ioo = 10',font=('Times', '12', 'bold italic'),background='white').place(x=428,y=450)
label_Ioo = Label(ventana, text='A/cm',font=('Times', '12', 'bold italic'),background='white').place(x=500,y=450)
label_Ioo = Label(ventana, text='2',font=('Times', '8', 'bold italic'),background='white').place(x=538,y=445)

#Muestra el valor de los sliders en la ventana
valor_n = Label(ventana, text='{: .2f}'.format(valor_actual_n.get()),font=('Times', '12', 'bold italic'),background='white')
valor_n.place(x=55,y=400)
valor_T = Label(ventana, text='{: .2f}'.format(valor_actual_T.get()),font=('Times', '12', 'bold italic'),background='white')
valor_T.place(x=55,y=450)
valor_IL = Label(ventana, text='{: .2f}'.format(valor_actual_IL.get()),font=('Times', '12', 'bold italic'),background='white')
valor_IL.place(x=498,y=400)
valor_Ioo = Label(ventana, text=valor_actual_Ioo.get(),font=('Times', '8', 'bold italic'),background='white')
valor_Ioo.place(x=488,y=445)

#Gráficas
fig1, ax1 = plt.subplots(figsize=(5,5),dpi=70)
ax1.set_xlabel('Voltaje (V)',color='black',loc='center')
ax1.set_ylabel('Corriente (A)',color='black',loc='center')

fig2, ax2 = plt.subplots(figsize=(5,5),dpi=70)
ax2.set_xlabel('Voltaje (V)',color='black',loc='center')
ax2.set_ylabel('Potencia (W)',color='black',loc='center')

#Label para los valores a mostrar
label_Voc = Label(ventana, text='Voc =',font=('Times', '12', 'bold italic'),background='white').place(x=870,y=150)
label_Isc = Label(ventana, text='Isc =',font=('Times', '12', 'bold italic'),background='white').place(x=870,y=190)
label_Vmp = Label(ventana, text='Vmp =',font=('Times', '12', 'bold italic'),background='white').place(x=870,y=230)
label_Imp = Label(ventana, text='Imp =',font=('Times', '12', 'bold italic'),background='white').place(x=870,y=270)
label_Pmax = Label(ventana, text='Pmáx =',font=('Times', '12', 'bold italic'),background='white').place(x=870,y=310)
label_FF = Label(ventana, text='FF =',font=('Times', '12', 'bold italic'),background='white').place(x=870,y=350)

#Función para la graficas y cálculo de variables
def graficas():
    n = slider_n.get() 
    T = slider_T.get() #[°C]
    T = T+273.15 #[K]
    IL=slider_IL.get() 
    Ioo=slider_Ioo.get() #Exponente
    Ioo = (10**(Ioo)) #[A/cm^2]
    
    v = np.arange(0, 5, 0.01) #Variable independiente
    #Constantes
    q = 1.602*(10**(-19)) # [C] Carga del electrón
    Eg = 1.12*(1.6022*(10**-19)) #[Joules]
    #k = 8.617*(10**(-5)) #[eV*K] Constante de Boltzmann
    k=1.381*(10**-23)

    #Funciones
    Io=Ioo*np.exp(-(Eg/(k*T)))
    funcion1=IL-(Io*(np.exp((q*v)/(n*k*T))-1))
    funcion2=v*(IL-(Io*(np.exp((q*v)/(n*k*T))-1)))
    
    line1, = ax1.plot(v, funcion1, color ='b', linestyle='solid')
    line2, = ax2.plot(v, funcion2, color ='b', linestyle='solid')
    
    #Graficar punto de Pmáx
    Voc=((n*k*T)/q)*np.log((IL/Io)+1)   #Voltaje a circuito abierto
    
    pot=np.multiply(funcion1,v)
    Pot_Max=max(pot)
    posicion=np.where(pot == Pot_Max)
    
    Imp=funcion1[posicion]
    Vmp=v[posicion]
    
    Pmax1, =ax1.plot([Vmp],[Imp],"o",color="red")
    
    LineV1=np.arange(0,Vmp,0.03)
    LineV2=Imp*np.ones(len(LineV1))
    Pline1, =ax1.plot(LineV1,LineV2,"--",color="red")
    
    LineH1=np.arange(0,Imp,0.01)
    LineH2=Vmp*np.ones(len(LineH1))
    Pline2, =ax1.plot(LineH2,LineH1,"--",color="red")
    
    Pmax2, =ax2.plot([Vmp],[Pot_Max],"o",color="red")
    
    LineV3=np.arange(0,Vmp,0.03)
    LineV4=Pot_Max*np.ones(len(LineV3))
    Pline3, =ax2.plot(LineV3,LineV4,"--",color="red")
    
    LineH3=np.arange(0,Pot_Max,0.01)
    LineH4=Vmp*np.ones(len(LineH3))
    Pline4, =ax2.plot(LineH4,LineH3,"--",color="red")
    
    #Gráficar punto de comportamiento ideal
    ideal, =ax1.plot([Voc],[IL],"o",color="black")
    
    LineV5=np.arange(0,Voc,0.03)
    LineV6=IL*np.ones(len(LineV5))
    Pline5, =ax1.plot(LineV5,LineV6,"--",color="black")
    
    LineH5=np.arange(0,IL,0.01)
    LineH6=Voc*np.ones(len(LineH5))
    Pline6, =ax1.plot(LineH6,LineH5,"--",color="black")
    
    #Ajusta los limites de las gráficas
    if (IL<1):
        y_lim1=0.1
    else:
        y_lim1=0.3
    
    if (Pot_Max<1):
        y_lim2=0.1
    else:
        y_lim2=0.3
    
    ax1.set_ylim(0,IL+y_lim1)
    ax1.set_xlim(0,Voc+0.3)
    ax2.set_ylim(0,Pot_Max+y_lim2)
    ax2.set_xlim(0,Voc+0.3)
    
    figure1.draw()
    figure2.draw()
    
    #Borra todas las curvas para actualizarse
    line1.set_ydata(v+(2**100))
    line2.set_ydata(v+(2**100))
    Pmax1.set_ydata([100])
    Pline1.set_ydata(LineV1+(2**10))
    Pline2.set_ydata(LineH1+(2**10))
    Pmax2.set_ydata([100])
    Pline3.set_ydata(LineV3+(2**10))
    Pline4.set_ydata(LineH3+(2**10))
    ideal.set_ydata(100)
    Pline5.set_ydata(LineV5+(2**10))
    Pline6.set_ydata(LineH6+(2**10))
    
    #Valores a mostrar en función de las gráficas
    valor_Voc = Label(ventana, text='{: .2f}'.format(Voc),font=('Times', '12', 'bold italic'),background='white').place(x=910,y=150)
    label_Voc2 = Label(ventana, text='V',font=('Times', '12', 'bold italic'),background='white').place(x=950,y=150)
    
    valor_Isc = Label(ventana, text='{: .2f}'.format(IL),font=('Times', '12', 'bold italic'),background='white').place(x=910,y=190)
    label_Isc2 = Label(ventana, text='A',font=('Times', '12', 'bold italic'),background='white').place(x=950,y=190)
    
    valor_Vmp = Label(ventana, text='{: .2f}'.format(Vmp[0]),font=('Times', '12', 'bold italic'),background='white').place(x=920,y=230)
    label_Vmp2 = Label(ventana, text='V',font=('Times', '12', 'bold italic'),background='white').place(x=960,y=230)
    
    valor_Imp = Label(ventana, text='{: .2f}'.format(Imp[0]),font=('Times', '12', 'bold italic'),background='white').place(x=920,y=270)
    label_Imp2 = Label(ventana, text='A',font=('Times', '12', 'bold italic'),background='white').place(x=960,y=270)
    
    valor_Pmax = Label(ventana, text='{: .2f}'.format(Pot_Max),font=('Times', '12', 'bold italic'),background='white').place(x=930,y=310)
    label_Pmax2 = Label(ventana, text='W',font=('Times', '12', 'bold italic'),background='white').place(x=980,y=310)
    
    FF=Pot_Max/(Voc*IL)
    valor_FF = Label(ventana, text='{: .2f}'.format(FF),font=('Times', '12', 'bold italic'),background='white').place(x=910,y=350)
    
    ventana.after(100, graficas) #Cada 100 milisegundos se revisa si existe un cambio

#Boton de inicio
iniciar = Button(ventana, text='Iniciar', width = 16, bg='chartreuse3', fg='black', font=('Times', '12', 'bold italic'), command= graficas)
iniciar.place(x=290,y=490)

#Boton de cerrar
cerrar= Button(ventana, text="Cerrar", width = 16, bg='red2', fg='black', font=('Times', '12', 'bold italic'), command=ventana.destroy) 
cerrar.place(x=460,y=490)

#Marco de las figuras
frame = Frame(ventana,bd=6)
frame.place(x=400,y=500)

#Área de las figuras
figure1=FigureCanvasTkAgg(fig1)
figure1.get_tk_widget().grid(column=0, row=0, columnspan=1, padx=60, pady=40)
figure2=FigureCanvasTkAgg(fig2)
figure2.get_tk_widget().grid(column=2, row=0, columnspan=1, padx=10, pady=40)

#Configuración de color de la ventana y sliders
ventana.configure(bg='white')
style = ttk.Style()
style.configure("Horizontal.TScale", background= 'white')

#Titulo
label_titulo = Label(ventana, text='Efecto de la temperatura y la Corriente Fotogenerada en una celda solar',font=('Times', '16', 'bold italic'),background='white',fg='black')
label_titulo.place(x=110,y=20)

#Información de estudiantes
Nombres= Label(ventana, text='Luis Torres     1161637\n Andrea Ardila     1161638',font=('Times', '12', 'bold italic'),background='white').place(x=850,y=400)
Materia= Label(ventana, text='Energía solar fotovoltaica \n2022 - II',font=('Times', '12', 'bold italic'),background='white').place(x=850,y=450)

mainloop()