from tkinter import *
from tkinter import ttk

#cores
cor1 = '#2b2b2b'
cor2 = '#38576b'
cor3 = '#dbb818'
cor4 = '#e0e0de'

#criando a janela
janela = Tk()
janela.title('Calculadora')
janela.geometry('342x385')
janela.config(bg=cor1)

#criando telas
Frame_tela = Frame(janela, width=340, height=110, bg=cor2)
Frame_tela.grid(row=0, column=0)

Frame_corpo = Frame(janela, width=340, height=410)
Frame_corpo.grid(row=1, column=0)

#variavel que armazena os valores
todos_valores = ('')
total = ('')

#criando função
def add_valores(event):
    global todos_valores
    todos_valores = str(todos_valores) + str(event)
    texto.set(todos_valores)

#função que faz o calculo
def resultado(calculo):
    global todos_valores
    global total
    total = eval(calculo)
    texto.set(total)
    todos_valores = total

#função de limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    texto.set('')


#criando label
texto = StringVar()
app_label = Label(Frame_tela, textvariable=texto, width=16, height=2, padx=7, anchor='e', relief=FLAT, font=('Ivy 26'), justify=RIGHT, bg=cor2, fg=cor4)
app_label.place(x=10, y=10)


#criando botões
b1 = Button(Frame_corpo, command=limpar_tela, text='C', width=38, height=3, bg=cor4, relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(Frame_corpo, command=lambda: add_valores('%'), text='%', width=11, height=3, bg=cor3, relief=RAISED, overrelief=RIDGE)
b2.place(x=260, y=0)

b3 = Button(Frame_corpo, command=lambda: add_valores('+'), text='+', width=11, height=3, bg=cor3, relief=RAISED, overrelief=RIDGE)
b3.place(x=260, y=55)
b4 = Button(Frame_corpo, command=lambda: add_valores('-'), text='-', width=11, height=3, bg=cor3, relief=RAISED, overrelief=RIDGE)
b4.place(x=260, y=110)
b5 = Button(Frame_corpo, command=lambda: add_valores('*'), text='x', width=11, height=3, bg=cor3, relief=RAISED, overrelief=RIDGE)
b5.place(x=260, y=165)
b6 = Button(Frame_corpo, command=lambda: add_valores('/'), text='/', width=11, height=3, bg=cor3, relief=RAISED, overrelief=RIDGE)
b6.place(x=260, y=220)

b7 = Button(Frame_corpo, command=lambda: add_valores('7'), text='7', width=11, height=3, bg=cor4, relief=RAISED, overrelief=RIDGE)
b7.place(x=0, y=55)
b8 = Button(Frame_corpo, command=lambda: add_valores('8'), text='8', width=11, height=3, bg=cor4, relief=RAISED, overrelief=RIDGE)
b8.place(x=87, y=55)
b9 = Button(Frame_corpo, command=lambda: add_valores('9'), text='9', width=11, height=3, bg=cor4, relief=RAISED, overrelief=RIDGE)
b9.place(x=173, y=55)

b10 = Button(Frame_corpo, command=lambda: add_valores('4'), text='4', width=11, height=3, bg=cor4, relief=RAISED, overrelief=RIDGE)
b10.place(x=0, y=110)
b11 = Button(Frame_corpo, command=lambda: add_valores('5'), text='5', width=11, height=3, bg=cor4, relief=RAISED, overrelief=RIDGE)
b11.place(x=87, y=110)
b12 = Button(Frame_corpo, command=lambda: add_valores('6'), text='6', width=11, height=3, bg=cor4, relief=RAISED, overrelief=RIDGE)
b12.place(x=173, y=110)

b13 = Button(Frame_corpo, command=lambda: add_valores('1'), text='1', width=11, height=3, bg=cor4, relief=RAISED, overrelief=RIDGE)
b13.place(x=0, y=165)
b14 = Button(Frame_corpo, command=lambda: add_valores('2'), text='2', width=11, height=3, bg=cor4, relief=RAISED, overrelief=RIDGE)
b14.place(x=87, y=165)
b15 = Button(Frame_corpo, command=lambda: add_valores('3'), text='3', width=11, height=3, bg=cor4, relief=RAISED, overrelief=RIDGE)
b15.place(x=173, y=165)

b16 = Button(Frame_corpo, command=lambda: add_valores('.'), text=',', width=11, height=3, bg=cor4, relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=220)
b17 = Button(Frame_corpo, command=lambda: add_valores('0'), text='0', width=11, height=3, bg=cor4, relief=RAISED, overrelief=RIDGE)
b17.place(x=87, y=220)
b18 = Button(Frame_corpo, command=lambda: resultado(todos_valores), text='=', width=11, height=3, bg=cor4, relief=RAISED, overrelief=RIDGE)
b18.place(x=173, y=220)


janela.mainloop()