from tkinter import *
from tkinter import ttk
import sys
import TelaDeLogin

janela = Tk()
janela.resizable(None, None)

altura = 500
largura = 500
x = (janela.winfo_screenwidth()//2) - (largura//2)
y = (janela.winfo_screenheight()//2) - (altura//2)
janela.geometry('{}x{}+{}+{}'.format(largura, altura, x, y))
janela.wm_attributes('-topmost', True)

janela.overrideredirect(1)
janela.config(background='white')

exit_btn = Button(janela, text='X', command=lambda: exit_window(), font=('yu gothic ui', 13, 'bold'), fg='black',
                  bg='white', bd=0, activebackground='black')
exit_btn.place(x=470, y=0)

bemvindo_label = Label(janela, text='BEM VINDO AO MEU APP', font=('yu gothic ui', 19, 'bold'), bg='white')
bemvindo_label.place(x=115, y=15)

imagem = PhotoImage(file='img//lgn.png')
bg_label = Label(janela, image=imagem, bg='white')
bg_label.place(x=180, y=85)

progresso_label = Label(janela, text='Carregando...', font=('yu gothic ui', 13, 'bold'), bg='white')
progresso_label.place(x=190, y=350)

progresso = ttk.Progressbar(janela, orient=HORIZONTAL, length=500, mode='determinate')
progresso.place(x=15, y=390, width=470, height=30)


def exit_window():
    sys.exit(janela.destroy())


def top():
    win = Toplevel()
    TelaDeLogin.LoginPage(win)
    janela.withdraw()
    win.deiconify()


i = 0


def load():
    global i
    if i <= 10:
        txt = 'Carregando...' + (str(10*i)+'%')
        progresso_label.config(text=txt)
        progresso_label.after(800, load)
        progresso['value'] = 10*i
        i += 1
    else:
        top()


load()
janela.mainloop()
