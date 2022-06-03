from tkinter import *
import customtkinter
from PIL import ImageTk, Image  # instalar o pillow -> pip install pillow


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0, 0)
        self.window.title("Página de Login")

        # ========================= Background Image =========================== #
        self.bg_frame = Image.open('img/back1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both')

        # ========================= Login Frame ================================ #
        self.lgn_frame = Frame(self.window, bg='white', width='950', height=600)
        self.lgn_frame.place(x=200, y=70)

        self.txt = 'SEJA BEM VINDO'
        self.heading = Label(self.lgn_frame, text=self.txt, font=('verdana', 25, 'bold'), bg='white', fg='black')
        self.heading.place(x=80, y=30, width=350, height=30)

        # ========================= Left side Image =========================== #
        self.side_image = Image.open('img/back2.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='white')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================= Sign In Image =========================== #
        self.sign_image = Image.open('img/lgn.png')
        photo = ImageTk.PhotoImage(self.sign_image)
        self.sign_image_label = Label(self.lgn_frame, image=photo, bg='white')
        self.sign_image_label.image = photo
        self.sign_image_label.place(x=620, y=75)

        self.sign_in_label = Label(self.lgn_frame, text='Sign In', bg='white', fg='black',
                                   font=('verdana', 17, 'bold'))
        self.sign_in_label.place(x=650, y=240)

        # ================================ Username ============================ #
        self.username_label = Label(self.lgn_frame, text='Username', bg='white', font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='white', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'))
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=550, y=359)

        # ================================ Username Icon ============================ #
        self.username_icon = Image.open('img/avatar.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='white')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ================================ Password ============================ #
        self.password_label = Label(self.lgn_frame, text='Password', bg='white', font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='white', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'), show='*')
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=550, y=440)

        # ================================ Password Icon ============================ #
        self.password_icon = Image.open('img/lock.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='white')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=413)

        # ======================= Login Button ======================================== #
        self.login = customtkinter.CTkButton(master=self.lgn_frame, text="LOGIN",
                                             text_color='WHITE', width=300, height=32,
                                             text_font=('verdana', 12, 'bold'), border_width=0, corner_radius=8,
                                             cursor='hand2')
        self.login.place(x=550, y=460)

        # ======================================= Forgot Password ======================= #
        self.forgot_button = Button(self.lgn_frame, text='Forgot Password ?',
                                    font=('yu gothic ui', 13, 'bold underline'), fg='black', width=25, bd=0,
                                    bg='white', activebackground='white', cursor='hand2')
        self.forgot_button.place(x=580, y=510)

        # ============================== Sign Up ======================================#
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=('yu gothic ui', 11, 'bold'),
                                background='white', fg='black')
        self.sign_label.place(x=550, y=560)

        self.signup_button = customtkinter.CTkButton(master=self.lgn_frame, text="SIGN UP",
                                             text_color='WHITE', width=80, height=32,
                                             text_font=('verdana', 10, 'bold'), border_width=0, corner_radius=8,
                                             cursor='hand2')
        self.signup_button.place(x=670, y=555)


        # ============================== Show/Hide Password =========================== #
        self.show_image = Image.open('img/eye.png')
        self.photo1 = ImageTk.PhotoImage(self.show_image)
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=860, y=420)

        self.hide_image = Image.open('img/invisible.png')
        self.photo = ImageTk.PhotoImage(self.hide_image)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.photo, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.hide)
        self.hide_button.image = self.photo
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg='white', activebackground='white',
                                  cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
